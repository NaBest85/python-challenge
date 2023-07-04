import os
import csv
with open(r'C:\Users\nicho\OneDrive\Desktop\budget_data.csv') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        print(len('Date'))