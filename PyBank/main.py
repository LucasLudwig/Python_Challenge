import os
import csv

filename = "/Users/lucasludwig/Desktop/OSU-VIRT-DATA-PT-02-2023-U-LOLC/HomeWork/Module 3 Challenge/PyBank/Resources/budget_data.csv"

# Set path for file
csvpath = os.path.join(filename)
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    # Read each row of data after the header
    date = []
    profit = []
    for row in csvreader:
        date.append(row[0])
        profit.append(int(row[1]))
    
#The total number of months included in the dataset
total_months = len(date)
# The net total amount of "Profit/Losses" over the entire period
total_profit = sum(profit)
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
change = []
# The greatest increase in profits (date and amount) over the entire period
max_profit = max(profit)
# The greatest decrease in profits (date and amount) over the entire period
min_profit = min(profit)
# The average of the changes in "Profit/Losses" over the entire period
for i in range(1, len(profit)):
    change.append(profit[i] - profit[i-1])
    avg_change = sum(change)/len(change)
    avg_change = format(avg_change, '.2f')
    max_change = max(change)
    min_change = min(change)
    max_change_date = str(date[change.index(max(change))+1])
    min_change_date = str(date[change.index(min(change))+1])
# Print the analysis to the terminal   
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: {max_change_date} (${max_change})")
print(f"Greatest Decrease in Profits: {min_change_date} (${min_change})")
# Export a text file with the results  
output_file = "/Users/lucasludwig/Desktop/OSU-VIRT-DATA-PT-02-2023-U-LOLC/HomeWork/Module 3 Challenge/PyBank/Analysis/Financial_analysis.txt"
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Financial Analysis"])
    writer.writerow(["----------------------------"])
    writer.writerow([f"Total Months: {total_months}"])
    writer.writerow([f"Total: ${total_profit}"])
    writer.writerow([f"Average Change: ${avg_change}"])
    writer.writerow([f"Greatest Increase in Profits: {max_change_date} (${max_change})"])
    writer.writerow([f"Greatest Decrease in Profits: {min_change_date} (${min_change})"])
