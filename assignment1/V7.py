# Interactive quiz system, sixth version
# Make a dictionary with the questions and correct answers
# Allow the user to choose the option by its label
# Improve the look and usability. Keep track of correct answers.
# Randomize the order of the questions and the order of the answers for each question.
# Refactor the code to use functions.

from string import ascii_lowercase
import random
import json

question_file = open("questions.json", "r")
questions = json.load(question_file)


NUM_QUESTIONS_PER_QUIZ = 5

def prepare_questions(questions, num_questions): # Question Setup 
    num_questions = min(num_questions, len(questions))
    return random.sample(list(questions.items()), k=num_questions)


def get_answer(question, alternatives): # Answer Option Setup (a,b,c, or d)
    labeled_answers = dict(zip(ascii_lowercase, alternatives))

    for label, answer in labeled_answers.items():
        print(f"{label}. {answer}")
        
    while (answer_label := input("Choice? ").lower()) not in labeled_answers:
        print(f"Invalid choice. Please select one of {', '.join(labeled_answers.keys())}.")

    answer = labeled_answers.get(answer_label)
    return labeled_answers[answer_label]

def ask_question(question, alternatives): # Answer comparison setup
    correct_answer = alternatives[0] # correct answer is the first option listed in the .json file
    ordered_alternatives = random.sample(alternatives, k=len(alternatives))
    answer = get_answer(question, ordered_alternatives)
    if answer == correct_answer:
        print("Correct!")
        return 1
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}.")
        return 0


# Main program logic starts here
questions = prepare_questions(questions, NUM_QUESTIONS_PER_QUIZ)

num_correct = 0

# Main Loop

for num, (question, answers) in enumerate(questions, start=1):
    print(f"\nQuestion {num}: {question}")
    num_correct += ask_question(question, answers)

try:  # ADDITIONAL REQUIREMENT #1 creates a text file that will keep track of quiz attempts
    with open("Score_History.txt", "r") as file: # if the txt file exists, it'll read for previous attempts
        previous_attempts = file.readlines()
    count = len(previous_attempts) + 1
except FileNotFoundError: # if not it will create a new file
    count = 1
    with open("Score_History.txt", "a") as file:
        pass

scores = open("Score_History.txt", "r") # ADDITIONAL REQUIREMENT #2
attempts = scores.readlines()
previous_attempts = []

for attempt in attempts: # extract score number for the previous attempts recorded in the text file
    if ":" in attempt:
        score_part = attempt.split(":")[-1].strip()
        score = int(score_part.split()[0])
        previous_attempts.append(score) # append extracted score to a list for comparison

previous_best = max(previous_attempts) if previous_attempts else -1 # determine highest score; if none then previous attempt = -1

with open("Score_History.txt", "a") as output:
    output.write(f"Attempt {count}: {num_correct} correct\n")

print(f"\nYou got {num_correct} correct.")

if num_correct > previous_best: # ADDITIONAL REQUIREMENT #2, prints a message if there is a new high score
    print("You got a new high score!")