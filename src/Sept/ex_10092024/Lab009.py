"""Here will will learn reading CSV file"""

import csv

try:
    with open("myCSVFile.csv") as csvFile:
        reader = csv.reader(csvFile)
        for cl in reader:
            print(cl[0], cl[1], sep=" |")
except FileNotFoundError as fileN:
    print(fileN)
finally:
    try:
        csvFile.close()
    except NameError as Na:
        print(Na)

print("===================Second Method============================")


try:
    with open("myCSVFile.csv") as Yes:
        reader = csv.reader(Yes)
        for content in reader:
            print(content[0], content[1])
except Exception as FileF:
    print(FileF)
