import numpy as np

hh_income = [
    (10, 14629),
    (20, 25600),
    (30, 37002),
    (40, 50000),
    (50, 63179),
    (60, 79542),
    (70, 100162),
    (80, 130000),
    (90, 184292),
]

hh_income_array = np.array(hh_income)

print(f"Dimensions of the array: {hh_income_array.ndim}")
print(f"Number of elements in the array: {hh_income_array.size}")

# Method 1
for i in range (hh_income_array.shape[0]):
    percentile = hh_income_array[i, 0]
    income = hh_income_array[i, 1]
    print(f"Percentile: {percentile}, Income: {income}")

# Method 2
for i in range(hh_income_array.shape[0]):
    print(hh_income_array[i,0], hh_income_array[i,1])