import csv
import statistics
PyBankpath = r"/Users/Lopez/UA-PHX-DATA-PT-08-2019-U-C/02-Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv"
with open(PyBankpath, newline='') as PybankCSV:
   Pybank = csv.reader(PybankCSV, delimiter = ",")
   PyBheader = next(Pybank, None)
   months=[]
   profit = []
   change = []
   for row in Pybank:
       months.append(row[0])
       profit.append(int(row[1]))
   for i in range(1,len(profit)):
       change.append(int(profit[i]-profit[i-1]))
avgchange = statistics.mean(change)
print(f'Total Months: {len(months)}')
print(f'Total: ${sum(profit)}')
print(f'Average Change: ${round(avgchange,2)}')
print(f'Greatest increase in profits: {months[change.index(max(change))+1]} ${max(change)}')
print(f'Greatest decrease in profits: {months[change.index(min(change))+1]} ${min(change)}')
