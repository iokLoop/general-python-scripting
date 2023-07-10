import csv

# for a csv file with the following structure
# l1   value1, value2
# l2   value3, value4
# l3   value5, value6

def load():
    listInY = []
    with open('file.csv', "r") as csv_file:
        for row in csv_file:
            (var1, var2) = row.rstrip("\n").split(",")
            tuplaInX = (var1, var2)
            listInY.append(tuplaInX)

    print(listInY)
    # [('value1', ' value2'), ('value3', ' value4'), ('value5', ' value6')]
    print(listInY[0])
    # ('value1', ' value2')
    print(listInY[2][1])
    #  value6

load()
