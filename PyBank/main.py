# Import modules
import os
import csv

#function for terminal output

#Set variables
# PLNet = 
# averagePL = 
# incPL = 
# decPL = 

#Read the csv
csvDir = os.path.join("Resources","budget_data.csv")
#open the csv in read mode
with open(csvDir) as csvFile:
    #create reader object
    csvReader = csv.reader(csvFile, delimiter=",")
    #skip the header
    csvHeader = next(csvReader)
    #loop through reader object to find the 
    for x in csvReader:
    #get values to output
    #total months     
        totalMonths = x

# PLNet = 
# averagePL = 
# incPL = 
# decPL = 

#write to the terminal
#print total months
print(totalMonths)
#print net PL
#print(PLNet)
#print average PL
#print(averagePL)
#print biggest increase of PL
#pring(incPL)
#print biggest decrease of PL
#print decPL


#write to the txt file
#write total months
#write net PL
#write average PL
#write biggest increase of PL
#write biggest decrease of PL



#notes for commits
#pseudocoded
#added reader