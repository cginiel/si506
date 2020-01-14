# SI 506 2019F - Problem Set 08

# In this problem set, you will combine data on a variety of superheroes and run some
# simple querying of the data.
#
# You will work with two data files. They are described below, but we encourage you to
# open each in your text editor in order to see exactly how they are structured.
#
# "sh_info.csv" :
#       A structured data file that contains rows of information about superheroes.
#       Each row is a different hero, and the information is separated by commas.
#       The first line of this file is called a "header" and serves as a legend for
#       the data stored in each row. The header is also separated by commas, and each
#       string in the header coresponds to the title of the data stored at that location
#       in each of the subsequent rows. For example, if "name" is the first item of the
#       comma-separated strings, then the first comma-separated item in each of the rows
#       is a name.
# "sh_powers.json" :
#       This is a simple one-layered (i.e. not nested) .json file that contains the names
#       and powers of the same superheroes that were featured in "sh_info.csv". Note that
#       the order of the superheroes in sh_powers.json is different than the order of the
#       superheroes in "sh_info.csv".


# PROBLEM 1
# Learning Objectives:
# 1. Introduce the idea of a "header" line from a .csv file.
# 2. Using the python standard library csv module to read a .csv file.

# Using a <with> statement and the csv module of the python standard library, open and read
# the file "sh_info.csv". Save the contents of the first line of "sh_info.csv" as a list called
# <info_header>, where each string separated by commas in the first line is an element of
# <info_header>.
#
# Then, for each other line in "sh_info.csv", create a list of all of the information from
# each hero. The information is once again separated by commas.
#
# Collect each of the non-header lists into another list called <info_data> in the order
# that they appear in the file.
#
# In other words, the final contents of <info_data> should look like this (we have provided
# the code to test Problem 1 below; you will simply need to uncomment it):

'''
[['Gambit', 'Remy Etienne LeBeau', 'X-men', 'New Orleans - Louisiana', 'Red', 'Brown',
'(current) Xavier Institute; Salem Center; Westchester County; New York; (former) New Orleans;
Louisiana; Paris; France; Cairo; Illinois;'], ['Black Panther', "T'Challa", 'Avengers', 'Wakanda - Africa',
'Brown', 'Black', 'Wakanda; Mobile'], ...etc]
'''

# HINT: You will need to keep track of the line numbers somehow when you loop through them.

# BEGIN PROBLEM 1 (can be accomplished in 10-15 lines of code)
import csv

sh_csv = "sh_info.csv"
info_header = None
info_data = None

# header

def read_csv_header(filename):
    """read a csv file, return header"""
    with open(filename, 'r', encoding='utf-8-sig') as file_obj:
        reader = csv.reader(file_obj, delimiter = ',')
        i = next(reader)
    return i

info_header = read_csv_header(sh_csv)

# contents

def read_csv_contents(filename):
    """read a csv file, return contents"""
    data = []
    with open(filename, 'r', encoding='utf-8-sig') as file_obj:
        reader = csv.reader(file_obj, delimiter = ',')
        next(reader)
        for row in reader:
            data.append(row)
    return data

info_data = read_csv_contents(sh_csv)

# BEGIN TEST FOR PROBLEM 1 (Uncomment me when you're ready!)
print(f"\n\nProblem 1 test a: {info_header} \n\nProblem 1 test b:{info_data} \n")
# END TEST FOR PROBLEM 1

# END PROBLEM 1


# PROBLEM 2
# Learning Objective:
# Using the json module to open and parse a .json file

# Use a <with> statement and the json module to open and read "sh_powers.json". Using the
# <json.loads> method, create a dictionary object called <powers> that contains the names
# of the heroes as keys and a list of their powers as values.
#
# We have provided a testing code (you'll need to uncomment it), which should result in the following:
#
# {'name': 'Nick Fury', 'powers': ['weapons_master', 'longevity']}

# BEGIN PROBLEM 2 (can be accomplished in 3-5 lines of code)
import json

sh_powers = "sh_powers.json"
powers = None

def read_json(filename):
    """reads JSON, makes dictionary"""
    with open(filename, 'r') as file_obj:
        data = json.load(file_obj)
    return data

powers = read_json(sh_powers)

# END PROBLEM 2

# BEGIN TEST FOR PROBLEM 2 (Uncomment me when you're ready!)
print(f"\nProblem 2 test: {powers['Nick Fury']} \n")
# END TEST FOR PROBLEM 2


# PROBLEM 3
# Learning Objectives:
# 1. Gain more practice building functions to perform useful, repetitive operations.
# 2. Gain more practice working with nested lists and dictionaries.

# Write a function called <get_info> that accepts two arguments, <row> and <header>. Both
# <row> and <header> should be lists. <get_info> should return a dictionary, where the items
# contained in <header> are the keys and the items contained in <row> are the values, in the
# same order.

# We have provided a testing code (you'll need to uncomment it), which should result in the following:
#
# {'name': 'Nick Fury', 'full_name': 'Nicholas Joseph Fury', 'team': 'Unaffiliated',
# 'place_of_birth': 'New York City', 'eye_color': 'Brown', 'hair_color': 'Brown / White', 'base': '-'}

# BEGIN PROBLEM 3 (can be accomplished in 3 - 5 lines of code)

def get_info(row, header):
    """takes two lists, outputs as a dictionary where header is key and row is value"""
    new_dict = {}
    y = 0
    # COUNTERS ARE YOUR FRIEND, BRO
    for x in header:
        new_dict[x] = row[y]
        y = y + 1
    return new_dict

# END PROBLEM 3

# BEGIN TEST FOR PROBLEM 3 (Uncomment me when you're ready!)
print(f"\n\nProblem 3 test: {get_info(info_data[27],info_header)} \n")
# END TEST FOR PROBLEM 3


# PROBLEM 4
# Learning Objectives:
# 1. Practice building complex, nested dictionaries
# 2. Practice developing methods to combine two datasets (you'll do a lot of this with SQL in si507)
# 3. Practice writing .json files using the python json library

# For this problem, create a dictionary called <heroes> and write it to a .json file called
# "heroes.json". Populate the <heroes> dictionary with the information
# about each hero. The keys should be the hero names, and the values should be another dictionary
# that contains the following key/value pairs for each hero:
#
# "name" : (str) the name of the hero
# "full_name" : (str) the full name of each hero
# "team" : (str) the team that the hero is affiliated with
# "place_of_birth" : (str) where the hero was born
# "eye_color" : (str) the eye color of the hero
# "hair_color" : (str) the hair color of the hero
# "base" : (str) where the hero lives
# "powers" : (list of strs) a list of the hero's powers.
#
# The end result of <heroes> should be a nested dictionary like below (maybe not in this order):
#
# {"Nick Fury":
#    {'name': 'Nick Fury', 'full_name': 'Nicholas Joseph Fury', 'team': 'Unaffiliated',
#    'place_of_birth': 'New York City', 'eye_color': 'Brown', 'hair_color': 'Brown / White', 'base': '-',
#    'powers': ['weapons_master', 'longevity']},
#  "Captain America": ....
# }
#
# To accomplish this problem, follow these general steps:
# 1. Create an empty dictionary called <heroes>
# 2. Loop through each line in <info_data>
# 3. Call your function <get_info> to retrieve a dictionary of the info for the hero on
#       each line of <info_data>
# 4. Assign the info dictionary you got from <get_info> to be a value in <heroes> associated with a key that
#       is the name of the hero.
# 5. Start a new for-loop to loop through each key-value pair in <powers>.
# 6. Assign the list of powers contained in <powers> to the correct hero in
#       the <heroes> dictionary (i.e. the names should be the same).
#
#
# Check your <heroes> dictionary with our provided code. Make sure it produces the entry for Nick Fury
# as we show above (make sure to uncomment our test code first).
#
# # # DON'T FORGET THE BELOW STEP # # # # # # # #
# Finally, use the json library to write <heroes> to a new file called "heroes.json".

# START PROBLEM 4 (can be accomplished in 7-10 lines of code)
heroes = {} # This should be your first line of code for this problem.

# Write your first for-loop below (see the instructions for clarification):

for row in info_data: 
    # never forget the temp variable, bro!!!
    name = row[0]
    heroes[name] = get_info(row, info_header)
    heroes[name]['powers'] = powers[name]

# Finally write out the whole dictionary as a .json file:
with open('heroes.json', 'w') as file_obj:
    json.dump(heroes, file_obj, indent = 2)

# END PROBLEM 4

# BEGIN TEST FOR PROBLEM 4 (Uncomment me when you're ready!)
print(f"\n\nProblem 4 test: {heroes['Nick Fury']} \n")
# END TEST FOR PROBLEM 4


# PROBLEM 5
# Learning Objectives:
# 1. Practice querying data from nested dictionaries
# 2. Practice building complex, nested data structures

# Write a function called <get_team> that takes two arguments:
# <teamname> : a string
# <data> : a dictionary containing hero data; give this a default value of your <heroes> dictionary
#
# <get_team> should return a tuple of two elements. The first element should be a
# string of the team name, and the second should be a list which contains the names of the heroes that are
# affiliated with the <teamname> (i.e. the value associated with the key 'team'
# for the hero's info should be the same as <teamname>).
#
# The test written below (uncomment it below when you are ready) should result in a tuple
# containing the following heroes (not necessarily in this order):
#
# ('Defenders', ['Iron Fist', 'Jessica Jones', 'Daredevil', 'Luke Cage'])

# BEGIN PROBLEM 5 (can be accomplished in 6-9 lines of code)

def get_team(teamname, data=heroes):
    pass


heroes_lst = heroes.items()

for v in heroes.values():
    if v['team'] == "Defenders":
        team_defenders = v['team']

for k,v in heroes_lst:
    if v['team'] == "Defenders":
        heroes_defenders = v['name']
        print(team_defenders)

# END PROBLEM 5

# BEGIN TEST FOR PROBLEM 5 (Uncomment me when you're ready!)
#print(f"\n\nProblem 5 test: {get_team('Defenders')}")
# END TEST FOR PROBLEM 5


# PROBLEM 6
# Learning Objective:
# 1. Practice querying complex, nested data structures

# A supervillain named Rubblebuster is terrorizing New York City! She has the superpower of
# super-strength. Find all the superheroes that have a base in New York City and have
# super-strength in order to subdue Rubblebuster! Append these hero names to a list
# called nyc_strong_heroes.
#
# Hint: look for heroes that have 'super_strength' in their list of powers.
# Hint: in addition, make sure that the heroes have the string "New York City" in the value
#       assigned to the 'base' key. Note that some heroes have several locations as their base,
#       so you'll need to check if New York City is anywhere in that string (use the <in> condition).
# Final hint: Use .lower() to make sure that you are checking if there are any instances of "New
#       York City" that might be spelled with different capitalization.
#
# Your resultant list should include 'Vision', 'Thing', and two others.

# BEGIN PROBLEM 6 (can be completed with 5-8 lines of code)

nyc_strong_heroes = [] # This should be the first line of code you write for this problem.

# END PROBLEM 6

# BEGIN TEST FOR PROBLEM 6 (Uncomment me when you're ready!)
#print(f"\n\nProblem 6 test: {nyc_strong_heroes}\n")
# END TEST FOR PROBLEM 6


# END PROBLEM SET 08
