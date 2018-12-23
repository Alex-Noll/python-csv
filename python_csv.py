""" Example Python program for Python CSV Assignment

This walks through defining some CSVs and reading them. And then goes through some CSV writing.

"""

# The primary purpose for this assignment is to learn how to leverage the python csv module
import csv

# CSV stands for Comma Separated Values. Most basic spreadsheets can be saved in this format.
# You can define a single row for column headers and then a row for different values for each row.
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
# Don't worry too much about the indexing; the header row is technically the 3rd row and there are two returns at the end of the string
my_animals_lines = my_animals.split("\n")
headers = my_animals_lines[2:3]
data = my_animals_lines[3:-2]

print("The headers:",headers)
print("The data:",data)

# Using the csv module helps to parse comma delimited data in a standardized way.
for row in csv.reader(data):
    print("Single line of data:",row)

# So, we can create a list of dictionaries fairly easily:
my_animal_dicts = []

# Get headers first:
header_row = None
for row in csv.reader(headers):
    header_row = row

for row in csv.reader(data):
    dict_row = []
    for i,item in enumerate(row):
        dict_row.append({ header_row[i]: item })
    my_animal_dicts.append(dict_row)
        
print("CSV to Dictionaries: ", my_animal_dicts)

