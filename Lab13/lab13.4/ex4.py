import json
import os
import random
from pathlib import Path

from flask import Flask, flash, redirect, render_template, request, session, url_for


BASE_DIR = Path(__file__).resolve().parent
QUESTIONS_FILE = BASE_DIR / "questions.json"
SCORE_HISTORY_FILE = BASE_DIR / "Score_History.txt"
NUM_QUESTIONS_PER_QUIZ = 5

with QUESTIONS_FILE.open(encoding="utf-8") as question_file:
    QUESTIONS = json.load(question_file)

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY") or os.urandom(32)


def prepare_questions():
    selected_questions = random.sample(
        list(QUESTIONS.items()),
        k=min(NUM_QUESTIONS_PER_QUIZ, len(QUESTIONS)),
    )
    return [
        {
            "question": question,
            "answers": random.sample(answers, k=len(answers)),
            "correct_answer": answers[0],
        }
        for question, answers in selected_questions
    ]


def record_score(score):
    previous_scores = []
    if SCORE_HISTORY_FILE.exists():
        for line in SCORE_HISTORY_FILE.read_text(encoding="utf-8").splitlines():
            if line.strip():
                previous_scores.append(int(line.rsplit(":", 1)[1].strip().split()[0]))

    previous_best = max(previous_scores, default=-1)
    attempt_number = len(previous_scores) + 1
    with SCORE_HISTORY_FILE.open("a", encoding="utf-8") as history_file:
        history_file.write(f"Attempt {attempt_number}: {score} correct\n")

    return max(previous_best, score), score > previous_best


@app.get("/")
def index():
    return render_template(
        "index.html",
        question_count=min(NUM_QUESTIONS_PER_QUIZ, len(QUESTIONS)),
    )


@app.post("/quiz/start")
def start_quiz():
    session["quiz_questions"] = prepare_questions()
    session["current_question"] = 0
    session["score"] = 0
    session.pop("quiz_result", None)
    return redirect(url_for("quiz"))


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    quiz_questions = session.get("quiz_questions")
    if not quiz_questions:
        return redirect(url_for("index"))

    question_index = session["current_question"]
    current_question = quiz_questions[question_index]

    if request.method == "POST":
        answer = request.form.get("answer")
        if answer not in current_question["answers"]:
            flash("Select an answer before continuing.")
            return redirect(url_for("quiz"))

        if answer == current_question["correct_answer"]:
            session["score"] += 1

        question_index += 1
        session["current_question"] = question_index
        if question_index == len(quiz_questions):
            score = session["score"]
            best_score, is_new_high_score = record_score(score)
            session["quiz_result"] = {
                "score": score,
                "total": len(quiz_questions),
                "best_score": best_score,
                "is_new_high_score": is_new_high_score,
            }
            session.pop("quiz_questions")
            session.pop("current_question")
            session.pop("score")
            return redirect(url_for("results"))

        return redirect(url_for("quiz"))

    return render_template(
        "quiz.html",
        question=current_question,
        question_number=question_index + 1,
        total_questions=len(quiz_questions),
    )


@app.get("/results")
def results():
    result = session.get("quiz_result")
    if not result:
        return redirect(url_for("index"))
    return render_template("results.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
