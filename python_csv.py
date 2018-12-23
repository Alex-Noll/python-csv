""" Example Python program for Python CSV Assignment

This walks through defining some CSVs and reading them. And then goes through some CSV writing.

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

# For our string, we'll manually split the headers and data
# Don't worry too much about the splitting and indexing.
# The header row is technically the 3rd row and there are two line breaks at the end.
my_animals_lines = my_animals.split("\n")
headers = my_animals_lines[2:3]
data = my_animals_lines[3:-2]

print("The headers:",headers)
print("The data:",data)

# Using the csv module helps to parse comma delimited data in a standardized way.
for row in csv.reader(data):
    print("Single line of data:",row)

# So, we can create a list of ordered dictionaries fairly easily:
my_animal_dicts = []

# Get headers first:
header_row = None
for row in csv.reader(headers):
    header_row = row

for row in csv.reader(data):
    dict_row = OrderedDict()
    for i,item in enumerate(row):
        dict_row[header_row[i]] = item 
    my_animal_dicts.append(dict_row)
        
print("CSV to Dictionaries: ", my_animal_dicts)

# Let's take a moment and make the list easier to use -- so that once a CSV is loaded,
# it is easier to use. Consider this function:
def build_data_dict(list_of_dicts,key):
    keyed_data = {}
    for item in list_of_dicts:
        keyed_data[item[key]] = item
    return keyed_data

useful_dict = build_data_dict(my_animal_dicts,'name')

print("A more useful dictionary: ",useful_dict)
