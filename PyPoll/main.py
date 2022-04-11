#modules
import os
import csv

#buckets
totalvotes = 0

#link data from csv file
polls = os.path.join("Resources\election_data.csv")

#title
print("Election Results")
print("-------------------------")

#where to look for the data for the script
with open(polls) as csvfile:
    dictreader = csv.DictReader(csvfile)
    next(dictreader, None)

#total votes
    for row in dictreader:
        totalvotes+=1

    print("Total Votes:", totalvotes)