# Interactive quiz system, second version
# have a list with the questions and correct answers
# this version makes it easier to add new questions and answers since questions are not embedded in the code but in a list

questions = [
    ("What is the capital of France?", "Paris"),
    ("What is the capital of Germany?", "Berlin"),
    ("What is the planet closest to the Sun?", "Mercury")
]

for question, correct_answer in questions:
    answer = input(f"{question} ")
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"The correct answer is {correct_answer}, not {answer}.")