import pandas as pd
import csv, json

path = input("Enter the csv file you want to convert : ")

data = pd.read_csv(path)
print(data)
print("Converted json file below : ")
print(json.dumps(list(csv.reader(open(path)))))