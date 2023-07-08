import csv


def load():
    ipDict = {}
    with open('file.csv',"r") as csv_file:
        for row in csv_file:
            (key, val) = row.rstrip("\n").split(";")
            ipDict[key]=val
    print(ipDict)    


load()
