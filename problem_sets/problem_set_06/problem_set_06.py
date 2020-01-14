# SI 506 2019F - Problem Set 06

# [Note] Please keep and do not modify any of the setup sections. Keep everything between each pair of Setup Start and Setup End intact.

# Setup Start
import os
# Setup End

"""

The following 6 problems are designed to help you review topics covered in the first half of the semester and prepare you to start working locally 
on your own devices.

All the testings performed on Gradescope will be done in a similar fashion as what has been done in prior problem sets.

[Note] You are recommended to do this problem set on your laptop and verify that they behave correctly before uploading to Gradescope for grading.

[Note] Unless specified otherwise, all the file operations and hence, their outcomes, are assumed to be in the same order as to how the file 
content is stored in the file. For instance, if a problem asks you to convert lines in a file all into lower case and store in another 
file, the order of the lines should be the same in both the original file and the new file.

"""


"""
Problem 0: Prepare folders and files

[Instructions] 

1. Create a folder named problem_set_06.
2. Move this python script (problem_set_06.py) into the folder problem_set_06
3. Download a file named source.txt, from Github/Canvas as part of this problem set, into the folder.
4. After you have completed the above steps, check the output of the provided print statements to verify the outcomes.
5. [Note] No code will be written for this problem.

[Explanations & Hints]

We highly highly recommend that you use the terminal commands that we cover this week to create all the folders.

* display the current folder
* switch to another folder
* create a folder

"""

# Setup Start
"""
If you have set up the folder correctly, you should see at least the following strings displayed on the terminal when you uncomment 
displayFolderAndFile('.') and execute the script in your terminal.
[File] problem_set_06.py
[File] source.txt

"""
def displayFolderAndFile(file_path):
    print("------------ Listing files and folders at a given path: {}".format(file_path))
    with os.scandir('.') as entries:
        for entry in entries:
            if entry.is_file():
                print("[File] {}".format(entry.name))
            elif entry.is_dir():
                print("[Folder] {}".format(entry.name))
    print("------------ End Listing ------------")

#displayFolderAndFile('.')
# Setup End

"""
Problem 1: Read a file and convert the content into a list

[Instructions] 

1. Assign the variable source_path a string that contains the name of the file, "source.txt".

2. Open the file using source_path, and read each line within the file as a separate string. Store these strings 
in sequence into a list named file_lines_list.

3. Assign the first two lines within file_lines_list as a list with two elements into a variable first_two_lines_list

[Explanations & Hints]

You are likely to use some of the following concepts or functions to solve this problem:
* file operation and function
* list slicing

"""

# Setup Start
file_lines_list = []
first_two_lines_list = []
source_path = ""
# Setup End


# Problem 1 Solution Start
# Write your code here
source_path = "source.txt"
data_123 = open(source_path, 'r')
file_lines_list = data_123.readlines()
first_two_lines_list = file_lines_list[:2]

# Problem 1 Solution End

# Setup Start
print("------------")
print("file_lines_list: {}".format(file_lines_list))
print("------------")
print("first_two_lines_list: {}".format(first_two_lines_list))
print("------------")
# Setup End


"""
Problem 2: Define a function that can transform a list into a new list

[Instructions] 

1. Define two functions named transform_a_list_even() and transform_a_list_odd(). Each function will take a list of strings as the
first and only argument, and return a transformed list of strings as the returned value

[A] For transform_a_list_even():
2.1 The function will store the even string (e.g., 2nd, 4th, ...) in the original list into the new list, discarding
the odd string (e.g., 1st, 3rd, 5th, ...)

2.2 Before storing any string into the new list, transform each string by 1) removing the following 1 substring: "- ".

2.3 Return the new list as the returned value of this function.

[B] For transform_a_list_odd():
3.1 The function will store the odd string (e.g., 1st, 3rd, 5th, ...) in the original list into the new list,
discarding the even string (e.g., 2nd, 4th, ...)

3.2 Before storing any string into the new list, transform each string by
1) remove the following 6 substrings: "-", "...", ",",".", "?", "!", and 2) convert into all lower case.

3.3 Return the new list as the returned value of this function.



[Explanations & Hints]

1. Look at the content of source.txt to see what's inside. It will help you contextualize what these functions can do.

2. You are likely to use some of the following concepts or functions to solve this problem:
* for
* if
* def
* arithmetic operator (e.g.,  the modulus operator %)
* boolean expression
* string operation & function
* list slicing

"""

# Problem 2 Solution Start

# Write your code here
def transform_a_list_even(list_of_strings):
    """
    takes the authors from source.txt and adds them to their own list, removes "- "
    """
    new_list_indices = []
    new_list = []
    for index in range(len(list_of_strings)):
        if index%2 == 1:
            new_list_indices.append(index)
    for index in new_list_indices:
        new_list.append(list_of_strings[index][2:])
    return new_list

def transform_a_list_odd(list_of_strings):
    """
    takes quotes from the source.txt and adds them to their own list, removes punctuation
    """
    new_list_indices = []
    new_list = []
    for index in range(len(list_of_strings)):
        if index%2 == 0:
            new_list_indices.append(index)
    for index in new_list_indices:
        new_list.append(list_of_strings[index].lower().replace(",", "").replace(".", "").replace("-", "").replace("...", "").replace("?", "").replace("!", ""))
    return new_list

# Problem 2 Solution End


# Setup Start

"""
Using the following test case, you should expect to see the following strings displayed on the terminal.

For transform_a_list_even():
["Meryl Streep", "Tom Hanks"]

For transform_a_list_odd():
['the minute you start caring about what other people think is the minute you stop being yourself', 
"if it wasn't hard everyone would do it it's the hard that makes it great"]

"""
test_case_problem_2_1 = ["The minute you start caring about what other people think, is the minute you stop being yourself.", "- Meryl Streep", "If it wasn't hard, everyone would do it. It's the hard that makes it great.", "- Tom Hanks"]
print("------------")
print("transform_a_list_odd(test_case_problem_2_1) outcome: {}".format(transform_a_list_odd(test_case_problem_2_1)))
print("------------")
print("transform_a_list_even(test_case_problem_2_1) outcome: {}".format(transform_a_list_even(test_case_problem_2_1)))
print("------------")
# Setup End


"""
Problem 3: 
[Instructions] 

1.1 Call the function transform_a_list_odd(), which you defined in Problem 2, 
with the argument file_lines_list, which you have assigned a value in Problem 1.

1.2 Assign the returned value of the function call to a variable named transformed_file_lines_list_odd.

2.1 Call the function transform_a_list_even(), which you defined in Problem 2, 
with the argument file_lines_list, which you have assigned a value in Problem 1.

2.2 Assign the returned value of the function call to a variable named transformed_file_lines_list_even.

[Explanations & Hints]

You are likely to use some of the following concepts or functions to solve this problem:
* variable assignment
* function call
* arguments

"""

# Setup Start
transformed_file_lines_list_odd = []
transformed_file_lines_list_even = []
# Setup End


# Problem 3 Solution Start
# Write your code here
transformed_file_lines_list_odd = transform_a_list_odd(file_lines_list)
transformed_file_lines_list_even = transform_a_list_even(file_lines_list)
# Problem 3 Solution End

# Setup Start
print("------------")
print("transformed_file_lines_list_odd: {}".format(transformed_file_lines_list_odd))
print("------------")
print("transformed_file_lines_list_even: {}".format(transformed_file_lines_list_even))
print("------------")
# Setup End


"""
Problem 4: 
[Instructions] 

1. Assign the variable target_path a string that contains the name of the file, "target.txt".

2. Combine the strings from transformed_file_lines_list_odd and transformed_file_lines_list_even 
into a list of strings and write them as a sequence of lines into the file target.txt, using target_path.

2.1 Each string will be in the format of "<nth odd string>|<nth even string>". 
For instance, the 1st string in target.txt will be the result of combining the 1st odd string 
and the 1st even string into "<1st odd string>|<1st even string>".

2.2 Before combining two strings, remember to remove the newline character, "\n", 
from the string in transformed_file_lines_list_odd, so that the new string will only have one newline character at the end.

3. Check the content of the target.txt to see if your code behaves correctly. 
The target.txt should contain a number of lines that is half of the source.txt.

[Explanations & Hints]

You are likely to use some of the following concepts or functions to solve this problem:
* file operation and function
* string operation or function
* list
* string formatting

"""



# Setup Start
target_path = ""
# Setup End


# Problem 4 Solution Start
# Write your code here
target_path = "target.txt"

fout = open(target_path, 'w')
len_odd = len(transformed_file_lines_list_odd)
len_even = len(transformed_file_lines_list_even)

for i in range(len_odd):
    #if i < len_even:
    fout.write("{0}|{1}".format(transformed_file_lines_list_odd[i].replace("\n", ""), transformed_file_lines_list_even[i]))
    #else:
        #fout.write("{0}".format(transformed_file_lines_list_odd[i]) + "\n")

#Test Failed: Lists differ: [] != ['you cannot find peace by avoiding life l[3141 chars]t\n"]

#Second list contains 24 additional elements.
#First extra element 0:
#'you cannot find peace by avoiding life leonard|Virginia Woolf, The Hours\n'

#Diff is 3439 characters long. Set self.maxDiff to None to see it. : Failed against provided data set!



# Problem 4 Solution End

# You should look at target.txt to see whether your code has behaved correctly.
# Each line should have the following format "<string>|<string>".
# Example of expected string in the file:
# you cannot find peace by avoiding life leonard|Virginia Woolf, The Hours



"""
Problem 5: Define a function that will calculate the frequency of a set of selected words in a file

[Instructions]

1. Define a function output_words_frequency_from_file() that takes three arguments, 
a source file name (source_file_path), a target file name (target_file_path), 
and a list of topic words (topic_words_list). The function will record the aggregated 
frequency of all topic words in the source file into the target file.

2. Use the function transform_a_list_odd() defined in problem 2 to transform the content from the 
source file before calculating the frequency of each word.

2.1 When checking whether a topic word exists in the list, remember to remove any 
whitespace characters (e.g., " " or "\n")  in the list content before making any comparison. 
For instance, a string "dream\n" (from the list) will not be the same as "dream" (from the topic word list), 
but "dream" (after removing the newline character from the list content) will be the same as "dream", and should be counted.

3. Append a newline character, \n,  at the end when you write the frequency into the target file

[Explanations & Hints]

You are likely to use some of the following concepts or functions to solve this problem:
* file operation and function
* for
* function call
* string function
* if
* boolean expression
* string formatting

"""

# Setup Start

we_family = ["we", "our", "ourselves"]
they_family = ["they", "their", "themselves"]
# Setup End

# Problem 5 Solution Start

# Write your code here
source_path = "source.txt"

def output_words_frequency_from_file(source_file_path, target_file_path, topic_words_list):
    data_file = open(source_file_path, 'r')
    data_123 = data_file.readlines()
    data_file.close()
    new_file = open(target_file_path, 'w')
    clean_list = transform_a_list_odd(data_123)
    cleaner_list = []

    for word in clean_list:
        if "\n" or " " in word:
            cleaner_list.append(word.replace("\n", "").replace(" ", ""))

    count = 0
    for line in clean_list:
        temp_list = line.split()
        for word in temp_list:
            if word in topic_words_list:
                count += 1

    new_file.write(str(count) + "\n")
    new_file.close()
    return count

# Problem 5 Solution End

# Setup Start
# Uncomment the following function calls and execute the code.
# Check the content of the files to see if your function behaves correctly.

# 13, using we_family as the topic_words_list
output_words_frequency_from_file(source_path, "test_output_frequency1.txt", we_family)

# 7, using they_family as the topic_words_list
output_words_frequency_from_file(source_path, "test_output_frequency2.txt", they_family)

# Setup End
