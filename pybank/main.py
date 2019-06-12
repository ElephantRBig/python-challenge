import os
import csv


csv_file = os.path.join('pybank.csv')

total_months = 0 #Total months
sum_of_PL = 0 #The sume of profits and loses
changes = 0
differences = []
maxvalue = 0
minvalue = 0

revenue =0

with open(csv_file,newline ='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    
    csv_header = next(csvreader)
    for row in csvreader:
        total_months=total_months+1
        sum_of_PL = sum_of_PL + int(row[1])
        changes = int(row[1]) - (revenue)
        differences.append(changes)
        if changes > maxvalue :
            maxvalue=changes
            maxvaluedate=row[0]
        
        if changes < minvalue :
            minvalue = changes
            minvaluedate=row[0]
        




        revenue = int(row[1])

print(sum_of_PL)
print(revenue)
print(changes)
print(differences)

change = sum(differences[1:])/(total_months-1)

print(change)
print(maxvalue)
print(minvalue)
print(maxvaluedate)
print(minvaluedate)

print('Financial Analysis')
print('-------------------------------')
print(f'Total Months: {total_months}')
print(f'Total: {sum_of_PL}')
print(f'Average Change: ${change}')
print(f'Greatest Increase in Profits: {maxvaluedate} ({maxvalue})')
print(f'Greatest Decrease in Profits: {minvaluedate} ({minvalue})')
