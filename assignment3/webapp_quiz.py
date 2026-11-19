
import json
import math
import os
import random
import sqlite3
import time
from contextlib import contextmanager
from pathlib import Path

from flask import Flask, redirect, render_template, request, session, url_for

# Keep the question file beside this script so loading doesn't depend on the
# directory from which Flask is started.
QUESTIONS_FILE = Path(__file__).resolve().with_name("questions.json")

NUM_QUESTIONS_PER_QUIZ = 5
TIMER_SECONDS = 15
DATABASE = Path(__file__).with_name("leaderboard.db")


def load_question_bank():
    # Each JSON entry must map a question to a list of answer strings.
    with QUESTIONS_FILE.open(encoding="utf-8") as question_file:
        question_bank = json.load(question_file)
    if not isinstance(question_bank, dict) or not question_bank:
        raise ValueError(f"{QUESTIONS_FILE} must contain a non-empty JSON object")
    for question, answers in question_bank.items():
        if (
            not isinstance(question, str)
            or not question.strip()
            or not isinstance(answers, list)
            or len(answers) < 2
            or any(not isinstance(answer, str) for answer in answers)
        ):
            raise ValueError(
                "Each question must map to a list of at least two answer strings"
            )
    return question_bank


QUESTION_BANK = load_question_bank()


def prepare_questions():
    # The first answer in the JSON list is correct; shuffle only for display.
    selected_questions = random.sample(
        list(QUESTION_BANK.items()),
        k=min(NUM_QUESTIONS_PER_QUIZ, len(QUESTION_BANK)),
    )
    return [
        {
            "question": question,
            "options": random.sample(answers, k=len(answers)),
        }
        for question, answers in selected_questions
    ]


app = Flask(__name__)
# Flask uses this key to sign session data; set SECRET_KEY outside development.
app.secret_key = os.environ.get("SECRET_KEY", "assignment3-development-key")


@contextmanager
def connect_database():
    # Commit successful work, roll back failures, and always release the connection.
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    try:
        yield connection
        connection.commit()
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()


def initialize_database():
    # Create the shared leaderboard table the first time the app runs.
    with connect_database() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS leaderboard (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                score INTEGER NOT NULL,
                max_score INTEGER NOT NULL,
                submitted_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
            """
        )


def render_current_question():
    # Keep the original start time so refreshing the page can't reset the timer.
    session.setdefault("question_started_at", time.time())
    index = session["question_index"]
    question = session["quiz_questions"][index]
    remaining_seconds = max(
        0,
        math.ceil(
            TIMER_SECONDS - (time.time() - session["question_started_at"])
        ),
    )
    return render_template(
        "quiz.html",
        question=question["question"],
        question_number=index + 1,
        total_questions=len(session["quiz_questions"]),
        options=question["options"],
        timed=session["timed"],
        timer_seconds=remaining_seconds,
    )


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/start")
def start_quiz():
    # Flask's session keeps each player's quiz progress separate.
    session["question_index"] = 0
    session["score"] = 0
    session["timed"] = request.args.get("mode") == "timed"
    session["quiz_questions"] = prepare_questions()
    session.pop("question_started_at", None)
    session.pop("score_id", None)
    session.pop("score_saved", None)
    return redirect(url_for("quiz"))


@app.route("/quiz")
def quiz():
    if (
        "question_index" not in session
        or session["question_index"] >= len(session.get("quiz_questions", []))
    ):
        return redirect(url_for("index"))
    return render_current_question()


@app.route("/quiz/answer", methods=["POST"])
def answer():
    if "question_index" not in session:
        return redirect(url_for("index"))

    index = session["question_index"]
    quiz_questions = session.get("quiz_questions", [])
    if index >= len(quiz_questions):
        return redirect(url_for("results"))

    timed_out = session["timed"] and (
        time.time() - session.get("question_started_at", 0) >= TIMER_SECONDS
    )
    if timed_out:
        session["question_index"] = len(quiz_questions)
        return redirect(url_for("results"))

    selected_answer = request.form.get("answer")
    # Check against the JSON's original order, not the shuffled display order.
    correct_answer = QUESTION_BANK[quiz_questions[index]["question"]][0]
    if selected_answer == correct_answer:
        session["score"] += 1

    session["question_index"] = index + 1
    if session["question_index"] == len(quiz_questions):
        return redirect(url_for("results"))
    session.pop("question_started_at", None)
    return redirect(url_for("quiz"))


@app.route("/results")
def results():
    max_questions = len(session.get("quiz_questions", []))
    if "question_index" not in session or session["question_index"] < max_questions:
        return redirect(url_for("index"))
    return render_template(
        "results.html",
        score=session["score"],
        max_questions=max_questions,
        score_saved=session.get("score_saved", False),
        name=session.get("player_name", ""),
    )


@app.route("/leaderboard/submit", methods=["POST"])
def submit_score():
    max_questions = len(session.get("quiz_questions", []))
    if "question_index" not in session or session["question_index"] < max_questions:
        return redirect(url_for("index"))

    name = request.form.get("name", "").strip()
    if not name:
        return render_template(
            "results.html",
            score=session["score"],
            max_questions=max_questions,
            score_saved=False,
            name="",
            error="Please enter your name.",
        )

    if not session.get("score_saved"):
        initialize_database()
        with connect_database() as connection:
            # Parameters keep user-provided names separate from the SQL command.
            cursor = connection.execute(
                "INSERT INTO leaderboard (name, score, max_score) VALUES (?, ?, ?)",
                (name[:50], session["score"], max_questions),
            )
            session["score_id"] = cursor.lastrowid
        session["player_name"] = name[:50]
        session["score_saved"] = True
    return redirect(url_for("leaderboard"))

# LEADERBOARD
@app.route("/leaderboard")
def leaderboard():
    initialize_database()
    with connect_database() as connection:
        scores = connection.execute(
            """
            SELECT id, name, score, max_score
            FROM leaderboard
            ORDER BY score DESC, submitted_at ASC, id ASC
            """
        ).fetchall()
    player_rank = None
    player_score = None
    score_id = session.get("score_id")
    # Rank by the same sorted order used for the top-10 list.
    for rank, score in enumerate(scores, start=1):
        if score["id"] == score_id:
            player_rank = rank
            player_score = score
            break
    return render_template(
        "leaderboard.html",
        scores=scores[:10],
        player_rank=player_rank,
        player_score=player_score,
    )

# Starts the quiz game if true
if __name__ == "__main__":
    initialize_database()
    app.run(debug=True)
