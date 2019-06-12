# Dependencies
import os
import csv

# Creating path to read the file
csv_file = os.path.join('pybank.csv')

# Declaring some variables out of habit
total_months = 0            # total months
sum_of_PL = 0               # the sume of profits and loses
changes = 0                 # the changes between two month
differences = []            # where the appended changes of revenue between months is added to
maxvalue = 0                # the max increase of change in profits
minvalue = 0                # the max decrease of change in profits
revenue =0                  # reference variable for appending values to differences, revenue for the month

# Opening and reading the file
with open(csv_file,newline ='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    
    csv_header = next(csvreader)
    for row in csvreader:                       # looping through the csvfile
        total_months=total_months+1             # finding the total months in the csvfile
        sum_of_PL = sum_of_PL + int(row[1])     # finding the sum of the profits/loses
        changes = int(row[1]) - (revenue)       # determining the changes between months
        differences.append(changes)             # appending the differences to a list for further calculation
        revenue = int(row[1])                   # using this as reference to find the differences

        # If the change is the largest increase/decrease, save it and comparing against other values
        # Also saving the dates for each time we receive the largest increase/decrease
        if changes > maxvalue :
            maxvalue=changes            # saving the value for the largest increase in profits
            maxvaluedate=row[0]         # the date for the largest increase in profits
        
        if changes < minvalue :
            minvalue = changes          # savings the value for the largest decrease in profits 
            minvaluedate=row[0]         # the date for the largest decrease in profits
        

        

# stating the average of changes
change = sum(differences[1:])/(total_months-1)

# Printing the results
print('-------------------------------')
print('Financial Analysis')
print('-------------------------------')
print(f'Total Months: {total_months}')
print(f'Total: {sum_of_PL}')
print(f'Average Change: ${round(change,2)}')
print(f'Greatest Increase in Profits: {maxvaluedate} ({maxvalue})')
print(f'Greatest Decrease in Profits: {minvaluedate} ({minvalue})')
print('-------------------------------')
