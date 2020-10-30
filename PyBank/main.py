# script for analyzing the financial records of your company 

# import the os module
import os

# module for reading the csv file
import csv
csvpath = os.path.join('C:\\Users\\19143\Desktop\\DataClass\\python-challenge\\PyBank\\Resources\\budget_data.csv')
with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    
    print(csvreader)

    # read the header row first (skip this if there is no header)
    csv_header = next(csvreader)    
    print(f"CSV Header: {csv_header}")

    # read each row of the data after the header
    for row in csvreader:
        print(row)

# calculate the total number of mons included in the dataset

# calculate the net total amount of "profits/losses" over the entire period

# calculate the average of the changes in "profits/losses over the entire period"

# calculate the greatest increase in profits (date and amount) over the entire period

# calculate the greatest decrease in losses (date and amount) over the entire period

 