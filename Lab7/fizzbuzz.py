for i in range (1,51):
    if i % 3 == 0 and i % 5 == 0: # or elif i % 15 == 0
        # this is the most contraining condition, so it must come first
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)