# SI 506 2019F - Problem Set 03

# SETUP
# We provide you with a selection of famous love quotes and who wrote them.
# In the future, such data will be provided in a file which you will read into python with some useful functions.
# However, for today, the teaching team has provided this list for you to use.

love_quotes = [
	"Love is not love which alters when it alteration finds",
	"Love, the itch, and a cough cannot be hid",
	"That love is all there is, Is all we know of love",
	"I am two fools, I know, for loving, and saying so",
	"Love lives on propinquity, but dies on contact",
	"You really have to love yourself to get anything done in this world",
	"The irony of love is that it guarantees some degree of anger, fear and criticism",
	"I see you everywhere, in the stars, in the river",
	"Respect is love in plain clothes",
	"If you want to be loved, be lovable",
]

authors = [
	"William Shakespeare",
	"Thomas Fuller",
	"Emily Dickinson",
	"John Donne",
	"Thomas Hardy",
	"Lucille Ball",
	"Harold H. Bloomfield",
	"Virginia Woolf",
	"Frankie Byrne",
	"Ovid",
]

# END SETUP


# PROBLEM 1
# Extract the indices of all the quotes which begin with "Love" into a new list named love_quotes_indices. Print love_quotes_indices.
# Note: You're not allowed to change the original quotes.
# Hint: Use for loop, if statement and string slicing.



# BEGIN PROBLEM 1 SOLUTION

love_quotes_indices = [] # new index for quotes with "Love" as first word
love_quotes = love_quotes

for index in range(len(love_quotes)):
	if "Love" in love_quotes[index].split(' ')[0]:
		love_quotes_indices.append(index)


print("Problem 1: \n", love_quotes_indices, "\n")


# END PROBLEM 1 SOLUTION


# PROBLEM 2
# Create quote-author pairs by concatenating the quotes in love_quotes with the author in authors.
# As long as love_quotes was created correctly the authors should correctly align with their quote.
# Concatenate the values using the format "<quote> - <author>" (the <text> are placeholders that your code should replace).
# Save these strings into the list quotes_with_author. Print quotes_with_author.


# BEGIN PROBLEM 2 SOLUTION
love_quotes = love_quotes
authors = authors
quotes_with_author_full = []
quotes_with_author = [] # new list with our combined lists

for index in range(len(love_quotes)):
	
# finds range of list (0-9), and moves through the list one item at a time
	
	quotes_with_author_full.append(love_quotes[index] + " - " + authors[index])
	
for index in love_quotes_indices:
	quotes_with_author.append(quotes_with_author_full[index])
	

	
# the index attached to "authors" and "love_quotes" corresponds the item of the list that it's sorting through. So if index is
# on item 2, it will be looking at the second item in authors and love_quotes. Since the lists are
# the same length, they'll all be aligned. We concatenate a hyphen between the two items in the respective lists and append those items
# as strings to our empty list.

print("Problem 2: \n", quotes_with_author, "\n")

# END PROBLEM 2 SOLUTION


# PROBLEM 3
# Write a function named who_wrote_it which will return the author of a quote when given the combined string "<quote> - <author>".
# Apply the function to quotes_with_author and store the result in the list i_wrote_it.
# Sort the list i_wrote_it based on alphabetic order. Print i_wrote_it.
# BEGIN PROBLEM 3 SOLUTION

author = " " # loops through quotes_with_author to pull authors
alphabetical_author = " " # loops through the function that pulled authors
i_wrote_it = [] # new list with alphabetical order of authors

def who_wrote_it(quote_string): # function needs an input "quote_string" and a definition (to use when you "call" it).
	author = quote_string.split(" - ")[1] # to isolate your author from the list, use list slicing
	return author # function needs to be returned to produce output

for quote in quotes_with_author: # for loop to move through each item in list quotes_with_author
	i_wrote_it.append(who_wrote_it(quote)) # use our function to append each author to our new list. We "called" the function and applied it to each item in our quotes_with_author list (which "quote" moves through).

i_wrote_it = sorted(i_wrote_it) # alphabetize your list

print("Problem 3: \n", i_wrote_it, "\n")

# END PROBLEM 3 SOLUTION


# PROBLEM 4
# Write a function named count_words_in_quote which will return the number of words in a given quote.
# Apply the function to the quotes indexed by the first and the last elements in love_quotes_indices.
# Assign the word count values to the variables first_word_count and last_word_count as appropriate.
# Print first_word_count and last_word_count.
# Note: Words in quotes are not only separated by blanks, but also by comma.
# Hint: Use split(), if-else statement, len() or sum().


# BEGIN PROBLEM 4 SOLUTION
words = " "


def count_words_in_quote(quote): # define word-counter function 
	words = quote.split(' ') # we find the number of words in a given quote
	return len(words) # produces the amount of words in a quote


first_word_count = count_words_in_quote(love_quotes[love_quotes_indices[0]]) # apply the function to count words
last_word_count = count_words_in_quote(love_quotes[love_quotes_indices[-1]]) # apply the function to count words

print("Problem 4: \n", first_word_count, last_word_count, "\n")

# END PROBLEM 4 SOLUTION


# PROBLEM 5
# Love quotes don't necessarily use "love"!
# Write a function named is_quote_with_love, which will determine whether the given quote contains the words
# "love", "loving", "loved", "lovable", "Love" or not.
# If the quote contains one of the words the function should return True otherwise return False.
# Use a while loop and is_quote_with_love to identify all quotes without "love", "loving", "loved", "lovable", "Love"
# Once identified append the quote to the no_love_quotes list.
# Print no_love_quotes
# Hint: You can search on the characters 'lov' if you use a built-in string function to convert quote to lower case.

# BEGIN PROBLEM 5 SOLUTION

luv_words = ["love", "loving", "loved", "lovable", "Love"]
i = 0
no_love_quotes = []

def is_quote_with_love(x): # function to find "love" in a given quote
		if 'lov' in x.lower(): # defensive coding to find 'lov'
			return True 
		else:
			return False
		
	
while i < len(love_quotes): # set i to less than so that the list stays within range
	status = is_quote_with_love(love_quotes[i]) # set status variable for if statement below
	if status == True: # status equivalence, if it works, brings "True == True"
		i += 1 # always add 1 to i after the condition
		
	else:
		no_love_quotes.append(love_quotes[i]) # grabs the "False" index from our list and adds it to no_love_quotes list.
		i += 1

	
print("Problem 5: \n", no_love_quotes, "\n")

# END PROBLEM 5 SOLUTION


# PROBLEM 6
# Finally, put all you've learned together.
# Reuse functions created above to sum up the word counts of quotes which contain "love", "loving", "loved", "lovable"
# or "Love" in love_quotes.
# Assign the total word count to the variable total_word_count.
# Print total_word_count.

# BEGIN PROBLEM 6 SOLUTION
total_word_count = 0

for quote in love_quotes:
	if is_quote_with_love(quote) == True:
		total_word_count += count_words_in_quote(quote)

print("Problem 6: \n", total_word_count)

# END PROBLEM 6 SOLUTION

# END PROBLEM SET