# Save the dictionary of questions to a JSON

import json

questions = {
  "How many ponies are in the main group of My Little Pony: Friendship is Magic?": ["6","5","4","8"],
  "Which ponies are NOT an alicorn?": ["Starlight Glimmer","Twilight Sparkle","Princess Luna","Princess Celestia"],
  "What is the name of the town Twilight Sparkle moves to?": ["Ponyville","Canterlot","Cloudsdale","Fillydelphia"],
  "How many seasons does My Little Pony: Friendship is Magic have?": ["9","8","7","6"],
  "What is the name of Apple Jack's pet animal?": ["Winona","Angel","Tank","Gummy"],
  "What is the name of Princess Cadence and Shining Armor's child?": ["Flurry Heart","Princess Skyla","Sweetie Belle","None of the above"],
  "Which of the following is an element of harmony?": ["Honesty","Trust","Empathy","Love"],
  "What are the names of the main characters in My Little Pony: Friendship is Magic?": ["Twilight Sparkle","Rainbow Dash","Pinkie Pie","Sunset Shimmer"]
}

filename = "quiz_questions.json"

with open(filename, "w") as file:
    json.dump(questions, file, indent=4)

print(f"Quiz questions saved to {filename}.")