# import the os module
import os

# module for reading the csv file
import csv
csvpath = os.path.join('C:\\Users\\19143\\Desktop\\DataClass\\python-challenge\\PyBank\\Resources\\budget_data.csv')
# this didn't work, not sure why...
#csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

# set starting value for the month_count and the total
month_count = 0
total = 0

# set max and min
max_increase = -999999999
max_month = ""
max_decrease = 999999999
min_month = ""
total_change = 0
last_profit = 0
change = []

with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    print(csvreader)

    # read the header row first (skip this if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # read each row of the data after the header and set profits, total, and month_count
    # calculate the total number of months included in the dataset   
    for row in csvreader:
        month = row[0]
        profit = int(row[1])
        month_count += 1
        if month_count ==0:
            last_profit = profit 
        #else:
            # calculate the change
            profit_change = profit - prev_profit 
            # update last_profit
            last_profit = profit_change 
        # calculate the net profits over the entire period
        total= total + profit
        # add another month

print("Financial Records")
print("-----------------------------")
# print the total number of months included in the dataset 
print(f'Total Months: {month_count}')
# print the net total amount of "profits/losses" over the entire period
print(f'Total: ${total:0,.0f}')

print(f'Total Change: ${last_profit:0,.0f}')

# calculate the average of the changes in "profits/losses over the entire period"

# calculate the greatest increase in profits (date and amount) over the entire period
# greatest_increase = 
# calculate the greatest decrease in losses (date and amount) over the entire period
# greatest_decrease = 
 