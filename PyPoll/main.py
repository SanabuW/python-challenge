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
#open the csv
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
        #count votes for each candidate by findinding the index of the candidate that the 
        #reader is on in the candidates list and pass it to the votes per candidate list at that index
        if str(x[2]) in votedCandidates:
                votesPerCandidate[votedCandidates.index(x[2])]  += 1 

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
#removed f'string notation to allow formatting of percentages to the .000 position
print(votedCandidates[0] + ": " + format(votePercentages[0], '.3f') + "% (" + str(votesPerCandidate[0]) + ")")
print(votedCandidates[1] + ": " + format(votePercentages[1], '.3f') + "% (" + str(votesPerCandidate[1]) + ")")
print(votedCandidates[2] + ": " + format(votePercentages[2], '.3f') + "% (" + str(votesPerCandidate[2]) + ")")
print(votedCandidates[3] + ": " + format(votePercentages[3], '.3f') + "% (" + str(votesPerCandidate[3]) + ")")
print(f'-------------------------')
print(f'Winner: {winningCandidate}')
print(f'-------------------------')


#write output to a txt file
#assign output path to variable
txtOutDir = os.path.join("analysis","PyPollAnalysis.txt")
#create writer object
with open(txtOutDir, 'w', newline='') as txtFile:
    #write results
    txtFile.write(f'Election Results\n')
    txtFile.write(f'-------------------------\n')
    txtFile.write(f'Total Votes: {totalVotes}\n')
    txtFile.write(f'-------------------------\n')
    txtFile.write(votedCandidates[0] + ": " + format(votePercentages[0], '.3f') + "% (" + str(votesPerCandidate[0]) + ")\n")
    txtFile.write(votedCandidates[1] + ": " + format(votePercentages[1], '.3f') + "% (" + str(votesPerCandidate[1]) + ")\n")
    txtFile.write(votedCandidates[2] + ": " + format(votePercentages[2], '.3f') + "% (" + str(votesPerCandidate[2]) + ")\n")
    txtFile.write(votedCandidates[3] + ": " + format(votePercentages[3], '.3f') + "% (" + str(votesPerCandidate[3]) + ")\n")
    txtFile.write(f'-------------------------\n')
    txtFile.write(f'Winner: {winningCandidate}\n')
    txtFile.write(f'-------------------------')