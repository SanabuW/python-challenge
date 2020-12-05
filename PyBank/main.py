# Import modules
import os
import csv


#Set variables
totalMonths = 0
monthsList = []
PLNet = 0
PLList = []
changeList=[]

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
        totalMonths += 1
        #populate months list
        monthsList.append(x[0])
        #get net PL
        PLNet += int(x[1])
        #get average PL
        #populate list of all PL values
        PLList.append(x[1])
    
    #use new list to create a list of all PL value changes
    for val in range(1, len(PLList)):
        changeList.append(int(PLList[val]) - int(PLList[val-1]))
    #find average PL
        averagePL = sum(changeList)/(len(changeList))
    #find largest incresing/decreasing PL values
    #use list comprehensions to make positive and negative lists and find the max/min of those lists
    incPL = max([val for val in changeList if val > 0])
    decPL = min([val for val in changeList if val < 0])
    
#write to the terminal
print(f'Total Months: {totalMonths}')
print(f'Total: ${PLNet}')
print(f'Average Change: ${round(averagePL, 2)}')
print(f'Greatest Increase in Profits: {monthsList[changeList.index(incPL)+1]} (${incPL})')
print(f'Greatest Decrease in Profits: {monthsList[changeList.index(decPL)+1]} (${decPL})')

#write to a txt file


#write total months
#write net PL
#write average PL
#write biggest increase of PL
#write biggest decrease of PL



#notes for commits
#pseudocoded
#added reader