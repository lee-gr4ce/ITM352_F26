searchMe  = [ 2, 5, 7, 11, 15, 22, 27, 30, 34, 41, 55, 57, 58, 60, 77]

num = int(input("Enter a number to search for: "))

for i in range(len(searchMe)):
    if num == searchMe[i]:
        print(f"{num} is in the list.")
        break
else:
    print(f"{num} is not in the list.")