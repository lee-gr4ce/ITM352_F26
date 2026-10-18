word = input("Enter a word: ")
"""
def ispalindrome():
    for x in range(len(word),0, -1):
       if word[x-1] == (word[len(word)-x-1]):
        print(True)
       else:
        print(False)
"""

for i in range(len(word),0, -1):
  if word[i-1] == word[len(word)-i]:
    print(True)
  else:
    print(False)