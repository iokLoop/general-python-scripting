import csv

# for a csv file with the following structure 
# l1   value1, value2 
# l2   value3, value4
# l3   value5, value6

def load():
    dict = {}
    with open('file.csv',"r") as csv_file:
        for row in csv_file:
            # using string manipulation and unpacking style for the row variable
            (key, value) = row.rstrip("\n").split(",")
            # adding key:value pair into the dictionary
            dict[key]=value
    return dict    


print(load())
#{'value1': ' value2', 'value3': ' value4', 'value5': ' value6'}
