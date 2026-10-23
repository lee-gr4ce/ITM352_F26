# Read a file of quiz quesitons and save as a directory

import json

filename = "quiz_questions.json"
with open(filename, "r") as file:
    questions = json.load(file)

print(questions)