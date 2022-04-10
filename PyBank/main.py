#modules
import os
import csv

#trackers
totalmonths = 0
totalrev = 0
pastrev = 0
highestrev = 0
lowestrev = 0

#create revenue bucket
revchange = []
proffitloss = []

#link data
budgetdata = os.path.join("Resources", "budget_data.csv")

#title
print("Financial Analysis")
print("------------------")

#where to look for data for everytjing below
with open(budgetdata) as csvfile:
    csvreader=csv.reader(csvfile)
    next(csvreader, None)    
    

#total months
    for row in csvreader:
        totalmonths+=1
    

#total amount of "Profit/Losses" over the entire period
        totalrev = totalrev + (int(row[1]))
    

#revenue change
        monthlychange = int(row[1])-pastrev
        pastrev = int(row[1])
        revchange.append(monthlychange)
        averagechange = round(sum(revchange)/totalmonths)

#greatest increase in revenue
        if(monthlychange > highestrev):
            highestmonth = row[0]
            highestrev = monthlychange

#greatest decrease in revenue
        if (monthlychange < lowestrev):
            lowestmonth = row[0]
            lowestrev = monthlychange

#results with labels    
    print("Total Months:", totalmonths)
    print(f"Total Revenue: ${totalrev}")
    print(f"Average Change: ${averagechange}")
    print(f"Greatest Increase in Revenue: {highestmonth} (${highestrev})")
    print(f"Greatest Decrease in Revenue: {lowestmonth} (${lowestrev})")

#export results to a text file
resultstxt = os.path.join("Analysis", "Results.txt")
with open(resultstxt, 'w') as outfile:
        outfile.write("Financial Analysis\n")
        outfile.write("-------------------\n")
        outfile.write(f"Total Revenue: ${totalrev}\n")
        outfile.write(f"Average Change: ${averagechange}\n")
        outfile.write(f"Greatest Increase in Revenue: {highestmonth} (${highestrev})\n")
        outfile.write(f"Greatest Decrease in Revenue: {lowestmonth} (${lowestrev})\n")