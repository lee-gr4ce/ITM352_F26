import random

requirements = [1,2,3,4,5,6,7,8,9,10]

r1 = random.choice(requirements)
requirements.remove(r1)
r2 = random.choice(requirements)

print(f"Assigned additional requirements: {r1}, {r2}")
