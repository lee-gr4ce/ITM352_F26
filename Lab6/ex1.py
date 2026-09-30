emotions = ("happy", "sad", "fear", "surprise")

is_it_true = emotions[len(emotions)-1] == "happy" and len(emotions) > 3
is_it_true = emotions[3] == "happy" and len(emotions) > 3
print(is_it_true)
print(emotions[3] == "happy" and len(emotions) > 3)

if emotions[3] == "happy" and len(emotions) > 3:
    print(True)
else: print(False)

