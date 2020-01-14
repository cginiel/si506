# SI 506 2019F - Problem Set 05

# The following 6 problems constitute a pre-midterm exam review. If a problem
# includes a setup section do not modify, delete or otherwise ignore the setup
# code.

# Functions that you are asked to write will be called directly by the
# auto grader when scoring your submission. Make sure all required statements
# are included in the function body.

# PROBLEM 1
# Working with the list named elements, demonstrate your understanding of
# the following concepts and operations:
# 1) creating values and determining types
# 2) making assignment statements
# 3) working with lists and list elements
# 4) using list indices and list slicing
# 5) using built-in functions such as type()

# INSTRUCTIONS: for each variable listed below assign the appropriate
# return value as directed below.

# PROBLEM 1 SETUP
elements = ['hello', 2, 4, 6.0, 7.5, 234352354, 99, [506, 507], 'goodbye']

print(f"Problem 1: \nelements = {elements}")

# END PROBLEM 1 SETUP

# START PROBLEM 1 SOLUTION
# Return the list element 234352354 by its index position (i.e., elements[?]).
# Assign the value to the variable named element_234352354.
element_234352354 = elements[5]

print(f"element_234352354 = {element_234352354}")

# Using the appropriate built-in function, return the type of the list element
# "hello" by its index position (i.e., elements[?]).
# Assign the value to the variable named element_hello_type.
element_hello_type = type(elements[0])

print(f"element_hello_type = {element_hello_type}")

# Use list slicing to return the list elements 6.0 and 7.5 (i.e., elements[?:?]).
# Assign the value to the variable named elements_six_seven_half.
elements_six_seven_half = elements[3:5]

print(f"elements_six_seven_half = {elements_six_seven_half}")

# Use list slicing to return the the last three list elements (i.e., elements[?:?]).
# Assign the value to the variable named elements_last_three.
elements_last_three = elements[6:]

print(f"elements_last_three = {elements_last_three}")

# Use list indices to return the last element in the nested list (i.e., elements[?][?]).
# Assign the value to the variable nested_element.
nested_element = elements[7][1]

print(f"nested_element = {nested_element} \n")

# END PROBLEM 1 SOLUTION


# PROBLEM 2:
# Working with the string named test_str demonstrate your understanding
# of the following concepts and operations:
# 1) working with sequences such as strings and lists
# 2) implementing a for loop
# 3) using string methods such as str.split()
# 4) using list methods such as list.append()
# 5) using built-in functions such as len()

# INSTRUCTIONS: write code that returns the length of each word contained in the string named test_str.
# Append each integer value returned to the list named word_lengths.

# START PROBLEM 2 SETUP
rhino_str = "The quick brown rhino jumped over the extremely lazy fox."

print(f"Problem 2: \ntest_str = {rhino_str}")

# END PROBLEM 2 SETUP

# START PROBLEM 2 SOLUTION
word_lengths = []

for word in rhino_str.split(" "):
	#if "." in word:
		#word = word[:-1]
	word_lengths.append(len(word))


print(f"word_lengths = {word_lengths}\n")

# END PROBLEM 2 SOLUTION


# PROBLEM 3:
# Working with two strings (single line and multi-line), demonstrate your understanding of
# the following concepts and operations:
# 1) designing a function that accepts a single argument and returns a value
# 2) working with strings as sequences
# 3) implementing a for loop
# 4) using a list to hold lookup values
# 5) implementing a counter to hold a running count (e.g., i = 0, i += 1)
# 6) evaluating values using a conditional statement (e.g., one line if statement)

# INSTRUCTIONS: Write a function named count_vowels that accepts a single string argument.
# Design the function to count the number of vowels (a,e,i,o,u) in any string
# passed to it. Create a list inside the function to hold the vowels.
# Create a counter to hold the vowel count (initialize as i = 0). Iterate over
# the string and check if characters encountered are vowels. If a match occurs
# increment the vowel count by 1. Return the total vowel count.

# NOTE: multi-line strings are denoted in Python by use of triple double-quotes ("""...""").
# The string will be processed as a single string despite spanning multiple lines.

# START PROBLEM 3 SETUP
one_line_str = "The cat climbed the tree." # vowel count is 7


print(f"Problem 3:\none_line_str = {one_line_str}")

multi_line_str = """Nature's first green is gold,
Her hardest hue to hold.
Her early leaf's a flower;
But only so an hour.
Then leaf subsides to leaf,
So Eden sank to grief,
So dawn goes down to day
Nothing gold can stay.""" # vowel count is 56

print(f"multi_line_str = {multi_line_str}")

# END PROBLEM 3 SETUP

# START PROBLEM 3 SOLUTION
vowels = ["a", "e", "i", "o", "u"]

def count_vowels(some_string):
	count = 0
	for character in some_string:
		if character.lower() in vowels:
			count += 1
	return count

# TESTING: use the two sample strings provided to test your function.
# Call the function and pass to it the string named one_line_str. Assign the
# return value to the variable named one_line_str_vowel_count. Call the
# function again and pass to it the string named multi_line_str. Assign the
# return value to the variable named multi_line_str_vowel_count.
# The auto grader will run your function twice, checking both of the expected
# return values.

one_line_str_vowel_count = count_vowels(one_line_str)
print(f"one_line_str_vowel_count = {one_line_str_vowel_count}")

multi_line_str_vowel_count = count_vowels(multi_line_str)
print(f"multi_line_str_vowel_count = {multi_line_str_vowel_count}")

# END PROBLEM 3 SOLUTION


# PROBLEM 4:
# Working with a list, demonstrate your understanding of the following
# concepts and operations:
# 1) designing a function that accepts two arguments and returns a value
# 2) using lists and list indices

# INSTRUCTIONS: Write a function named get_element that accepts two arguments:
# a list and an integer. The function will return a list element
# by its index position using the supplied integer as the index
# position value.

# We have provided a list named more_elements that you should use
# to test your function.

# HINT: calling get_element(more_elements, 0) will return "salad".
# If you test with an integer >= len(more_elements), e.g.,
# get_element(more_elements, 10), you will throw a list index out of range error.

# START PROBLEM 4 SETUP
more_elements = ["salad", 33, 3.14, ['dog','cat'], "fish", 19, 18]

print(f"more_elements = {more_elements}")

# END PROBLEM 4 SETUP

# START PROBLEM 4 SOLUTION

def get_element(a_list, a_int):
	element_got = a_list[a_int] 
	return element_got

# initially you were writing a while loop to iterate through the list
# because you thought you needed to move through all items of said list 
# but this function is a simple matter of indexing from a list 
# rather than "collecting" info by iterating over it

print(f"Problem 4: \nget_element = {get_element(more_elements, 0)}")

# END PROBLEM 4 SOLUTION

# PROBLEM 5
# Working with a list of strings, demonstrate your understanding of the following
# # concepts and operations:
# 1) using the with statement and the built-in function open(path, 'mode')
# 2) selecting the correct parameter mode for the desired file operation
#    (e.g., read or write)
# 3) implementing a for loop
# 4) writing data to a file

# INSTRUCTIONS: Use the with statement and the built-in function open(path, 'mode')
# to obtain a writable file object associated with the file named problem_4.txt.
# Then write the elements of the list named recipe to the file. Each element must be
# written to a separate line in the same sequence as the element appears in the list.

# START PROBLEM 5 SETUP
recipe = [
	'Preheat oven to 350 degrees F (175 degree C).\n',
	'Place the sliced apples in a 9x13 inch pan.\n',
	'Mix the white sugar, 1 tablespoon flour and ground cinnamon together, and sprinkle over the apples.\n',
	'Pour water evenly over all.\n',
	'Combine the oats, 1 cup of flour, brown sugar, baking powder, baking soda and melted butter together.\n',
	'Crumble evenly over the apple mixture.\n',
	'Bake at 350 degrees F (175 degrees C) for about 45 minutes.'
]

# END PROBLEM 5 SETUP

# BEGIN PROBLEM 5 SOLUTION

path = "problem_4.txt"
fout = open(path, 'w')

with fout as file_obj:
	for line in recipe:
		fout.write(line)
fout.close()

# END PROBLEM 5 SOLUTION


# PROBLEM 6
# Working with the function below, demonstrate the following skills:
# 1) ability to read code
# 2) ability to debug and fix broken code
# 3) ability to test code

# INSTRUCTIONS: The function get_counts() accepts two arguments:
# a file name and a list of characters. Fix the function so that it
# performs the following operations:
# 1) opens a file in read mode and returns a file object
# 2) iterates over each line in the file object (outer loop),
# 3) iterates over each character in the line (inner loop),
# 4) checks if the character matches a character in the list characters
# 5) increments the counter by 1 if a match is made
# 6) returns the count

# HINT: Use the file problem_4.txt created earlier to test the function as you work on it.
# For example if pass in a list of vowels to match on you should return a count of 118.
# Also, try using print() to visualize the values in the outer and inner loops as you
# work to fix this code.

# BEGIN PROBLEM 6 SOLUTION
def get_counts(file_name, characters):
	counter = 0
	with open(file_name, "r") as file_obj:
		for line in file_obj:
			for char in line: 
				if char in characters:
					counter += 1						
	return counter

# FIX ME (for char in xyz statement throws NameError. Replace xyz with correct sequence.)
# FIX ME (add missing conditional statement)
# FIX ME (do something with the counter)
matches = get_counts('problem_4.txt', ['a', 'e', 'i', 'o', 'u'])

print(f"matches = {matches}")

# END PROBLEM 6 SOLUTION

# END PROBLEM SET