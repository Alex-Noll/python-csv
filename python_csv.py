""" Example Python program for Python CSV Assignment

This walks through defining some CSVs and reading them. And then goes through some CSV writing.
Finally, this leads to an assignment where the student will create her own CSV file and load
the file into a useful data structure that handles a fundamental problem.

Read through the comments and code. Be sure you also execute the code using python3:

`python3 python_csv.py`

"""

# The primary purpose for this assignment is to learn how to leverage the python csv module
import csv
# We will also leverage an ordered dictionary from collections
from collections import OrderedDict

# CSV stands for Comma Separated Values. Most basic spreadsheets can be saved in this format.
# You can define a single row for column headers and then a row for each set of values.
# If you have some familiarity with databases, you can think of a single set of CSVs as a single database table.
# Consider the following CSV:

my_animals = """

name,type,color,age
Oliver,cat,grey and white,6
Penny,dog,white,2
Henry,goat,brown,1
Charlie,cat,grey and white,15

"""

## For our string, we'll manually split the headers and data
## Don't worry too much about the splitting and indexing.
## The header row is technically the 3rd row and there are two line breaks at the end.

# First, break up the string into lines
my_animals_lines = my_animals.split("\n")

# Next, separate the column headers (which are only on line 3)
headers = my_animals_lines[2:3]

# And finally the data: take all the lines after 3, but not including the last two lines.
data = my_animals_lines[3:-2]


print("The headers:",headers)
print("The data:",data)


## Using the csv module helps to parse comma delimited data in a standardized way.
## We can take the csv data above, and convert it to a list of dictionaries

# Initialize a list for the data
my_animal_dicts = []

# Get headers first. We are just reading the one line
header_row = None
for row in csv.reader(headers):
    # Even though this is in a loop, we know that headers is only one row
    header_row = row

# Finally, use the csv reader to read in the data, one row/line at a time
for row in csv.reader(data):
    # For every row, we initialized and Ordered Dictionary
    dict_row = OrderedDict()
    for i,item in enumerate(row):
        # Now, for every field in the row, we are using that field's header to
        # set the dictionary key. Because the order of the data in each row will
        # match the order of the headers, I can use 'i' to select the correct
        # header and use that as the key for the field.
        dict_row[header_row[i]] = item
        # Review above carefully and consider the first row of data and the second
        # field in that row. The above statement will be:
        # dict_row["type"] = "cat"

    # Simply append the ordered dictionary for each row to the list
    my_animal_dicts.append(dict_row)

print()            
print("CSV to Dictionaries: ", my_animal_dicts)
print()

# Let's take a moment and make the list easier to use -- we want to find a row by name.
# Consider this function:
def build_data_dict(list_of_dicts,key):
    """Given a list of dictionaries, return a containing dictionary keyed by 'key'.
    Note, key must be a key in every dictionary in the list_of_dicts. 
    """
    # Initialize the dictionary to return
    keyed_data = {}
    for item in list_of_dicts:
        # For every item (which will be a dictionary), add it to the keyed_data dictionary
        # keyed by the value found for the passed in key
        keyed_data[item[key]] = item
        # Take a second to review the above to understand what is happening. Consider
        # the third row of data with a key "type", the above line would be:
        # keyed_data["goat"] = { "name":"Henry","type":"goat","color":"brown", "age":"1" }
    return keyed_data

# Now, call the above method to convert the list of dictionaries to a dictionary
# of dictionaries.
useful_dict = build_data_dict(my_animal_dicts,'name')

# Examine what this looks like
print()
print("A more useful dictionary: ",useful_dict)
print()

# Why is this a useful dictionary? Well, because now you can "look up" a "row" of data
# by the name.
print("Looking up what type of animal Charlie is...")
charlie_type = useful_dict["Charlie"]["type"]
print("Charlie is a " + charlie_type)
print("Penny is a " + useful_dict["Penny"]["type"])
print("And, Oliver is " + useful_dict["Oliver"]["age"] + " years old.")
print()

## Ok, typically, you will actually have your csv in a separate file that your program will
## read in using the csv module. So, jump over to the csv file in this repo and follow the
## code below to see how easy it is to read the file into a useful data structure.

with open('songs.csv') as csvfile:
    # This loads the file directly into a list of Ordered Dictionaries (like we did above)
    reader_list = csv.DictReader(csvfile)

    # Now, we can reuse our function from above to get this list into a useful dictionary
    useful_dict = build_data_dict(reader_list,'title')

# Here are some lookups from our csv file:
print("Humility is sung by " + useful_dict["Humility"]["artist"])
print("'How are you true' is on " + useful_dict["How are you true"]["album"])

###
## The Assignment!!
###

## Maybe you have already found some issues with the examples above?
## Essentially, in our "useful dictionaries" we are not handling duplicate keys (key collisions).
## Consider our first example, what if you are collecting pet information for more than one
## family. You will certainly run into pets with the same name. So, our solution would not
## work in that case -- which pet would be selected if you have a cat named "Oliver" and also
## a dog named "Oliver". This is a HUGE problem with the song CSV. We know there are many songs
## that share the same name, so this would cause key collisions.
##
## Therefore, your assignment is:
##
## 1) Create your own csv file to load into a useful dictionary.
##
## 2) Come up with a scheme to overcome key collision.
##
## Hint, when you load the csv into your useful data structure, you can create what we call a
## "multi-part" key. Often times, you can add column(s) of data to help with this. Consider the
## animals data above. If we add pets from other families, we would likely also add a column
## for the family name so that you can find a pet by family name AND pet name.
## A lookup could be something like:  useful_dict["Penny-Mills"]
