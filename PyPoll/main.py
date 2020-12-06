# Import modules
import os
import csv


#Set variables
totalVotes = 0
votedCandidates = []
votePercentages = [0,0,0,0]
votesPerCandidate = [0, 0, 0, 0]
winningCandidate = ""
#read from csv
#assign filepath
csvDir = os.path.join("Resources","election_data.csv")
#open the csv in read mode
with open(csvDir) as csvFile:
    #create reader object
    csvReader = csv.reader(csvFile, delimiter=",")
    #store the header
    csvHeader = next(csvReader)
    #loop through reader object
    for x in csvReader:
        #get data / make calcs
        #The total number of votes cast #count
        totalVotes += 1
        #list of candidates who received votes
        #build list of unique candidates
        if str(x[2]) not in votedCandidates:
            votedCandidates.append(x[2])
        if str(x[2]) in votedCandidates:
                votesPerCandidate[votedCandidates.index(x[2])]  += 1         #int(votedCandidates[x[2]])] += 1

#find percentage of votes for each candidate
for n in range (0, len(votesPerCandidate)):
    votePercentages[n] = round((votesPerCandidate[n]/totalVotes) * 100, 3)

#find highest number and retrieve string from votedCandidates list at same index
winningCandidate = votedCandidates[votesPerCandidate.index(max(votesPerCandidate))]

#print results to console
print(f'Election Results')
print(f'-------------------------')
print(f'Total Votes: {totalVotes}')
print(f'-------------------------')
print(votedCandidates[0] + ": " + format(votePercentages[0], '.3f') + "% (" + str(votesPerCandidate[0]) + ")")
print(votedCandidates[1] + ": " + format(votePercentages[1], '.3f') + "% (" + str(votesPerCandidate[1]) + ")")
print(votedCandidates[2] + ": " + format(votePercentages[2], '.3f') + "% (" + str(votesPerCandidate[2]) + ")")
print(votedCandidates[3] + ": " + format(votePercentages[3], '.3f') + "% (" + str(votesPerCandidate[3]) + ")")
print(f'-------------------------')
print(f'Winner: {winningCandidate}')
print(f'-------------------------')

#write to txt file








#draft/ initial pseudocode
    #Import modules
    #Set variables
    #read from csv
        #get data / make calcs
            # The total number of votes cast
                #addition by iteration
            #list of candidates who received votes
                #conditional statement on counts, and pull item into list on condition
            #percentage of votes each candidate won
                #multi-list
            #total number of votes each candidate won
                #multi-list
            #winner of the election based on popular vote.
                #find max of all candidates with votes. x-reference btw lists
    #print to terminal
    #print to txt
#Notes on raw data
#there is a header (Voter ID,	County,	Candidate)

#notes for commits


#Todo