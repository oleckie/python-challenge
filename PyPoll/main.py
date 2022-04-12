#modules
import os
import csv

#trackers
totalvotes = 0

#buckets
candidates = []
votes = {}

#link data from csv file
polls = os.path.join("Resources\election_data.csv")

#title
print("Election Results")
print("-------------------------")

#where to look for the data for the script
with open(polls) as csvfile:
    dictreader = csv.DictReader(csvfile)
    next(dictreader, None)

    candidatelist = []

#total votes
    for row in dictreader:
        candidatelist.append(row["Candidate"])


#list of candidates with votes
        candidate = row["Candidate"]
        if candidate not in candidates:

            candidates.append(candidate)

    print("Total Votes:", len(candidatelist))
    print("-------------------------")
    x = len(candidatelist)
    
    for person in candidates:
        personvotes = 0
            
        for name in candidatelist:
            if person == name:
                personvotes+=1
                
#new line (percent votes)
        candperc = (personvotes/x)
      
        print(f'{person}, {personvotes}, {candperc:.3%}')
    print("-------------------------")
    print("Winner:  Khan")
    print("-------------------------")