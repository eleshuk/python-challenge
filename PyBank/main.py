# import the os module
import os
import sys
# module for reading the csv file
import csv
csvpath = os.path.join('C:\\Users\\19143\\Desktop\\DataClass\\python-challenge\\PyBank\\Resources\\budget_data.csv')
# this didn't work, not sure why...
#csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

# set starting value for the month_count and the total
month_count = 0
total = 0

# set max and min
max_profit = 0
max_month = ""
min_profit = 0
min_month = ""
total_profit = 0 
sum_change = 0
total_change = 0
last_profit = 0

# previous_revenue

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
        if month_count ==1:
            last_profit = profit
        else:
            # if profit - last profit
            if (profit - last_profit) > max_profit:
                # maximum profit = profit - last profit
                max_profit = profit- last_profit
                # maximum month = month
                max_month = month
            # if profit - profits is less than the min_profit 
            if (profit - last_profit) < min_profit:
                # minimum profit is equal to the profit - the last profit
                min_profit = profit - last_profit
                # min month = month 
                min_month = month
            sum_change += profit - last_profit
            total_profit += profit
            last_profit = profit
        # update total
        total= profit + total
    # calculate average change
    average_change = sum_change/(month_count-1)


print("Financial Records")
print("-----------------------------")
# print the total number of months included in the dataset 
print(f'Total Months: {month_count}')
# print the net total amount of "profits/losses" over the entire period
print(f'Total: ${total:0,.0f}')
print(f'Average Change: ${average_change:0,.2f}')
print(f'Greatest Increase in Profits: {max_month}, (${max_profit})')
print(f'Greatest Decrease in Profits: {min_month}, (${min_profit})')

stdoutOrigin=sys.stdout 
text_path = os.path.join('Analysis', 'PyBank_analysis.txt')
sys.stdout = open(text_path, "w")

print("Financial Records")
print("-----------------------------")
# print the total number of months included in the dataset 
print(f'Total Months: {month_count}')
# print the net total amount of "profits/losses" over the entire period
print(f'Total: ${total:0,.0f}')
print(f'Average Change: ${average_change:0,.2f}')
print(f'Greatest Increase in Profits: {max_month}, (${max_profit})')
print(f'Greatest Decrease in Profits: {min_month}, (${min_profit})')

sys.stdout.close()
sys.stdout=stdoutOrigin
