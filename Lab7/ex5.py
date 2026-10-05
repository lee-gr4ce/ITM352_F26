"""
celebs = ("Yuqi", "Shuhua", "Soyeon", "Minnie", "Miyeon")
ages = (27, 26, 28, 28, 29)

celeb_list = []
for celeb in celebs:
    celeb_list.append(celeb)

ages_list = [age for age in ages]

celebs_dict = {"celebs": celeb_list, "ages": ages_list}
print(celebs_dict)
"""

# WITHOUT LOOPS
celebs = ("Yuqi", "Shuhua", "Soyeon", "Minnie", "Miyeon")
ages = (27, 26, 28, 28, 29)

celeb_list = list(celebs)
ages_list = list(ages)

celebs_dict = {"celebs": celeb_list, "ages": ages_list}
print(celebs_dict)