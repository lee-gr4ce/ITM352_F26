# Try to append to a tuple. It won't work.
# Name: Grace Lee
# Date: 9/16/26

survey_respondants = (1012, 1015, 1021, 1053)
survey_respondants.append(1011) # this will not work because tuples are immutable
# output: AttributeError: 'tuple' object has no attribute 'append'

survey_respondants = survey_respondants + (1011,) # this will work because we are creating a new tuple
# the extra comma is needed to indicate that this is a tuple with one element, otherwise it will be interpreted as an integer
print("Updated survey respondants:", survey_respondants)
