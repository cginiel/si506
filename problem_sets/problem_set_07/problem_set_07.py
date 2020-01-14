# SI 506 2019F - Problem Set 07

# The following 6 problems cover dictionaries. If a problem
# includes a setup section do not modify, delete or otherwise ignore the setup
# code.

# Functions that you are asked to write will be called directly by the
# auto grader when scoring your submission. Make sure all required statements
# are included in the function body.

# PROBLEM 1
# Working with the empty dictionary <dict_one>, demonstrate your understanding of
# the following concepts and operations:
# 1) adding key-value pairs into the dictionary
# 2) updating the value for a specific key in the dictionary


# INSTRUCTIONS:
# 1) Add following key-value pairs into <dict_one>
# KEY       VALUE
# "name"    "William Shakespeare"
# "born"    1564
# "died"    1616
# "age"     2

# 2) Update <age> with <died> - <born>
# 2) Update the value of <age> through calculation using -, (i.e. <died> - <born>) .
# You are required to obtain the values through the dictionary for calculation, instead of using the numbers directly

# PROBLEM 1 SETUP
dictionary_one = {}

# END PROBLEM 1 SETUP

# START PROBLEM 1 SOLUTION
# Add key-value pairs into <dict_one>

dict_one = {
    "name":"William Shakespeare",
    "born":1564,
    "died":1616,
    "age":2
}

dictionary_one = dict_one

new_age = dict_one["died"] - dict_one["born"]

dict_one["age"] = new_age

print(dict_one["age"])

# Update <age> with <died> - <born>
# e.g. <died> = 2019, <born> = 2000, then <age> = 19


print(f"Problem 1:\ndict_one = {dictionary_one} \n")
# END PROBLEM 1 SOLUTION


# PROBLEM 2
# Working with the dictionary <golds>, demonstrate your understanding of
# the following concepts and operations:
# 1) working with keys and values of a dictionary
# 2) implementing a for loop
# 3) using dictionary methods such as dictionary.values()
# 4) using built-in functions such as sum()


# INSTRUCTIONS:
# The dictionary <golds> consists of <country> - <gold medal number> key-value pairs
# Sum all the <gold medal number> in <golds> and assign the value into <golds_sum>
# PROBLEM 2 SETUP
golds = {"Italy": 12,
         "USA": 33,
         "Brazil": 15,
         "China": 27,
         "Spain": 19,
         "Canada": 22,
         "Argentina": 8,
         "UK": 29}
golds_sum = 0
# END PROBLEM 2 SETUP


# START PROBLEM 2 SOLUTION
# You are encouraged to use a for loop to sum up all the gold medal numbers
x = golds.values()

for item in x:
    golds_sum += item

print(f"Problem 2:\ngolds_sum = {golds_sum} \n")
# END PROBLEM 2 SOLUTION

# PROBLEM 3
# Working with <countries_golds>, demonstrate your understanding of
# the following concepts and operations:
# 1) working with keys, values of a dictionary
# 2) implementing a for loop
# 3) using dictionary methods such as dictionary.items()
# 4) using list methods such as list.append()


# INSTRUCTIONS:
# The dictionary <countries_golds> consists of <country> - <gold medal number> key-value pairs
# Concatenate <country> - <gold medal number> into a string
# with following format "<country> won <gold medal number> gold medals."
# For example, given "USA": 33, the formatted string should be "USA won 33 gold medals"
# Append each formatted string to the list <countries_golds_list>


# PROBLEM 3 SETUP
countries_golds = {"Italy": 12,
                   "USA": 33,
                   "Brazil": 15,
                   "China": 27,
                   "Spain": 19,
                   "Canada": 22,
                   "Argentina": 8,
                   "UK": 29}
countries_golds_list = []
# END PROBLEM 3 SETUP

# START PROBLEM 3 SOLUTION
isolate_keys = countries_golds.keys()
#print(isolate_keys)
isolate_values = countries_golds.values()
#print(isolate_values)
dicttolist = countries_golds.items()
#print(dicttolist)

countries_golds_list = []

for key,value in dicttolist:
    new_string = f"{key} won {value} gold medals."
    countries_golds_list.append(new_string)


print(f"Problem 3:\ncountries_golds_list = {countries_golds_list} \n")
# END PROBLEM 3 SOLUTION

# PROBLEM 4
# Working with <lyrics>, demonstrate your understanding of
# the following concepts and operations:
# 1) working with sequences such as strings and lists
# 2) using string methods such as string.lower(), string.split()
# 3) implementing a for loop
# 4) adding new key-value pairs into dictionary
# 5) updating the value for a specific key in the dictionary


# INSTRUCTIONS:
# The string <lyrics> consists of words separated by " "
# You are given a dictionary called <words_frequency>
# Each key in <words_frequency> is a word in <lyrics> and its associated value is set to 0 initially.
# Please update the value of each key, so it can correctly describe how many times each word(key) appears in the <lyrics>
# e.g. "when" appears twice in <lyrics>, so words_frequency["when"] = 2

# For consistency, all the keys in <words_frequency> should be in lowercase
# (i.e., the frequencies of both "When" and "when" should be aggregated in the dictionary using the key "when")
# Don't worry about KeyErrors, since <words_frequency> includes all the words appear in <lyrics>
# A Python KeyError exception is what is raised when you try to access a key that isn't in a dictionary

# PROBLEM 4 SETUP
lyrics = "When I am down and oh my soul so weary When troubles come my heart burdened be"

words_frequency = {'when': 0,
                   'i': 0,
                   'am': 0,
                   'down': 0,
                   'and': 0,
                   'oh': 0,
                   'my': 0,
                   'soul': 0,
                   'so': 0,
                   'weary': 0,
                   'troubles': 0,
                   'come': 0,
                   'heart': 0,
                   'burdened': 0,
                   'be': 0}

# END PROBLEM 4 SETUP

# START PROBLEM 4 SOLUTION
lyrics_words = lyrics.split()
# split the string "lyrics" and make it a list with each word as an element in the list
#print(lyrics_words)

for wrd in lyrics_words:
    # loop through each word in the list
    wrd = wrd.strip().lower()
    # temporarily make each word lower case and remove any whitespace between words
    #print(wrd)
    if wrd in words_frequency:
        # check if the word is in our dictionary...
        words_frequency[wrd] = words_frequency[wrd] + 1
        # if it is, take that key and update its value by 1 every time it appears

print(f"Problem 4:\nwords_frequency = {words_frequency} \n")
# END PROBLEM 4 SOLUTION

# PROBLEM 5A
# Working with <long_lyrics>, demonstrate your understanding of
# the following concepts and operations:
# 1) working with sequences such as strings and lists
# 2) using string methods such as string.lower(), string.split()
# 3) implementing a nested for loop
# 4) adding new key-value pairs into dictionary
# 5) updating the value for a specific key in the dictionary


# INSTRUCTIONS:
# The string <long_lyrics> consists of words separated by " " and "\n"
# Create a dictionary called <char_frequency> so that each key in <char_frequency> is a character (i.e. "a","b"..."z")
# in <lyrics> and its associated value is how many times that character appears in the <long_lyrics>

# For consistency, all the characters should be in lowercase
# (i.e., the frequencies of both "A" and "a" should be aggregated in the dictionary using the key "a")
# " " and "\n" are NOT valid characters.
# Valid characters are limited to the 26 letters that comprise the English alphabet from "a" to "z"
# Be careful of KeyErrors, since <char_frequency> is an empty dictionary.


# PROBLEM 5A SETUP
long_lyrics = '''
When I am down and oh my soul so weary
When troubles come, and my heart burdened be
Then I am still and wait here in the silence
Until you come and sit awhile with me
You raise me up so I can stand on mountains
You raise me up to walk on stormy seas
I am strong when I am on your shoulders
You raise me up to more than I can be
You raise me up so I can stand on mountains
You raise me up to walk on stormy seas
I am strong when I am on your shoulders
You raise me up to more than I can be
'''
char_frequency = {}
# END PROBLEM 5A SETUP

# START PROBLEM 5A SOLUTION
long_lyrics_list = long_lyrics.split()
# we assign the string to a list, splitting it on whitespace
#print(long_lyrics_list)

for wrd in long_lyrics_list:
    # loops through each word in the list
    wrd = wrd.strip().lower()
    # we temporarily strip the word of whitespace and make it lowercase
    for char in wrd:
        # loops through each character in each word
        if char not in char_frequency:
            char_frequency[char] = 1
            # if the character is not in the dictionary, add a count
        else:
            char_frequency[char] = char_frequency[char] + 1
            # if the character is in the dictionary and it's found again, add another count

print(f"Problem 5a:\nchar_frequency = {char_frequency} \n")
# END PROBLEM 5A SOLUTION

# PROBLEM 5B
# Working with <char_frequency>, demonstrate your understanding of
# the following concepts and operations:
# 1) designing a function that accepts a single argument and returns a value
# 2) working with strings as sequences
# 3) implementing a for loop
# 4) using dictionary methods such as dictionary.items()
# 5) evaluating values using a conditional statement


# INSTRUCTIONS:
# Write a function named <find_most_common_char> that takes one argument: <long_string>,
# (each string consists of words separated by " " and "\n")
# and returns a string, which contains a single character that has the highest frequency count in <long_string>.

# You are encouraged to reuse the code in PROBLEM 5A
# Note: there is only ONE most common character


# For consistency, all the characters should be in lower case
# (i.e., the frequencies of both "I" and "i" should be aggregated in the dictionary using the key "i")
# " " and "\n" are NOT valid characters.
# Valid characters only include 26 alphabets from "a" to "z"

# Sample case
# If <long_lyrics> was passed into <find_most_common_char> as an argument, <find_most_common_char> should return "e"

# Hints:
# In problem 5A, you are asked to create a dictionary that records the word frequencies.
# With a dictionary that records word frequencies, you can find a word with the highest frequency by
# looping through each dictionary entry and compare the value to the highest frequency being seen so far.
#
# Recommended Step 1: Inside the function, create a dictionary with the correct word frequencies (similar to 5A).
# Recommended Step 2: Next, loop through the dictionary to find the word(key) with the highest frequency.
# Recommended Step 3: return the word as the returned value for the function.

# START PROBLEM 5B SOLUTION

def find_most_common_char(long_string):
    """
    isolates and counts all characters in a string, returns the character with the highest count
    """
    char_frequency = {}
    long_string_list = long_string.split()
    # we assign the string to a list, splitting it on whitespace
    #print(long_string_list)
    for wrd in long_string_list:
        # loops through each word in the list
        wrd = wrd.strip().lower()
        # we temporarily strip the word of whitespace and make it lowercase
        for char in wrd:
            # loops through each character in each word
            if char not in char_frequency:
                char_frequency[char] = 1
                # if the character is not in the dictionary, add a count
            else:
                char_frequency[char] = char_frequency[char] + 1
                # if the character is in the dictionary and it's found again, add another count
    
    isolate_keys = char_frequency.keys()
    isolate_values = char_frequency.values()
    dicttolist = char_frequency.items()
    newstring = ""
    
    for key,value in dicttolist:
        # since key and value are paired, we can loop through each pair in our dictionary list (dicttolist)
        newstring = f"{max(char_frequency, key=char_frequency.get)}"
        # we make an f string literal for our output, which finds the max integer of a value and its corresponding key
    return newstring
    # essentially returns our key

# You can use "long_string_test1", "long_string_test2" to test your function
# Note: passing these two tests doesn't guarantee your function is correct.
# We will use other test cases to verify the correctness of your implementation

long_string_test1 = "away from joy you walk a little missing a tooth discussing famous black dogs on the dead"
print(find_most_common_char(long_string_test1))
# <find_most_common_char> should return "a" if <long_string_test1> was passed into as an argument
long_string_test2 = "smiling grip on what you want would never let me down I know you we say after never having met"
# <find_most_common_char> should return "e" if <long_string_test2> was passed into as an argument
print(find_most_common_char(long_string_test2))


# END PROBLEM 5B SOLUTION


# END PROBLEM SET
