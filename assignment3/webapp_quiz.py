# Application to engage the quiz webapp
# Name: Grace Lee
# Date: Nov 13, 2026

from flask import Flask, render_template, request, redirect, url_for

#Global Variables
score = 0
question_number = 0
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Berlin", "Madrid", "Paris"]
    },
    {
        "question": "What planet is known as the Red Planet?",
        "options": ["Earth", "Saturn", "Jupiter", "Mars"]
    }
]
max_questions = len(questions)

app = Flask(__name__)

@app.route('/')
def index():
    global score, question_number # global allows us to access variables outside of the function
    score = 0
    question_number = 0
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    global score, question_number, max_questions, questions

    if request.method == 'POST':
        # Capture the answer from the form
        answer = request.form.get('answer') # request is a variable that flask creates to handle requests from the user
        # it looks at the form data and gets the value of the input with name 'answer'

        # Check if the answer is correct
        if answer == questions[question_number]['options'][-1]: # the correct answer is always the last option in the list
            score += 1

        question_number += 1

        if question_number < max_questions:
            # Render the next question
            return render_template('quiz.html',
                                   question=questions[question_number]['question'],
                                   question_number=question_number,
                                  options=questions[question_number]['options'])
        else:
            # Quiz is over, redirect to the result page
            return render_template("results.html", score=score, max_questions=max_questions) 
            # render_template is a function that takes in the name of the html file and any variables we want to pass to it

@app.route('/result')
def result():
    # Display the final score
    global score, max_questions
    return render_template("result.html", score=score, max_questions=max_questions)

def main():
    app.run(debug=True) # debug=True allows us to see errors in the console

if __name__ == '__main__':
    main()