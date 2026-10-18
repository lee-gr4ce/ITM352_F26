def gcd(num1, num2):
    for i in range(min(num1, num2), 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i


num1 = 48
num2 = 18
print(gcd(num1, num2))
