# Ask the user for a sentence (using import())
# Turn the sentence into a list of strings (using split())
# Reverse the list
# Join the list back into a string (using join())

# Name: Grace Lee
# Date: 9/18/26

sentence = input("Enter a sentence: ")
words = sentence.split()
words.reverse()
reversed_sentence = " ".join(words)
print("Reversed Sentence: ", reversed_sentence)

joined_sentence = sentence + " " + reversed_sentence
print("Joined Sentence: ", joined_sentence)