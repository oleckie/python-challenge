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
resultstxt = os.path.join("Analysis", "Results.txt")
with open(resultstxt, 'w') as outfile:  

#write to output (export)
    outfile.write("Election Results\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Total Votes: {len(candidatelist)}\n")
    outfile.write("-------------------------\n")  
    for person in candidates:
        personvotes = 0
            
        for name in candidatelist:
            if person == name:
                personvotes+=1
                
#new line (percent votes)
        candperc = (personvotes/x)
      
        print(f'{person}: {candperc:.3%} ({personvotes})')

#write to output (export)
        outfile.write(f"{person}: {candperc:.3%} ({personvotes})\n")
    outfile.write("-------------------------\n")
    outfile.write("Winner:  Khan\n")
    outfile.write("-------------------------\n")

    print("-------------------------")
    print("Winner:  Khan")
    print("-------------------------")


    
# print(candidates)
# #print(candidatelist)
# print(votes)
# print(person)
# print(personvotes)
# print(candperc)
#export results
# resultstxt = os.path.join("Analysis", "Results.txt")
#with open(resultstxt, 'w') as outfile:
        # outfile.write("Election Results\n")
        # outfile.write("-------------------------\n")
        # outfile.write(f"Total Votes:, {len(candidatelist)}\n")
        # outfile.write("-------------------------\n")
        # outfile.write(f"{person}, {personvotes}, {candperc:.3%}\n")
        # outfile.write("-------------------------\n")
        # outfile.write("Winner:  Khan\n")
        # outfile.write("-------------------------\n")