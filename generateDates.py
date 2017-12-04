#Script used to generate dates from a very specific range, that is
#last mondays of months from September to June from this year and five years back

from datetime import date

endYear = 2017
startMonth = 9 #September
educationDuration = 10 #in Months
yearsToCover = 6 #current Year + 5 past
outputFileName = 'dates.txt'

datesList = []

def advanceMonths(dateToAdvance, monthsCount):
    advancedYear = dateToAdvance.year
    advancedMonth = dateToAdvance.month + monthsCount

    if (advancedMonth > 12):
        advancedYear = advancedYear + 1
        advancedMonth = advancedMonth - 12

    advancedDay = daysInMonth(advancedMonth, advancedYear)

    return date(advancedYear, advancedMonth, advancedDay)
    
def daysInMonth(month, year):
    nextMonth = month + 1
    yearAdvanced = 0

    if (nextMonth == 13):
         nextMonth = 1
         yearAdvanced = yearAdvanced + 1

    return (date(year + yearAdvanced, nextMonth, 1) - date(year, month, 1)).days #1 means First Day of The Month

def isMonday(date):
    if date.weekday() == 0:
        return True
    else:
        return False

#Generate list of Dates
for y in range(0, yearsToCover):
    currentYear = endYear - y
    lastDay = daysInMonth(startMonth, currentYear)
    startDate = date(currentYear, startMonth, lastDay)
        
    for m in range(0, educationDuration):
        currDate = advanceMonths(startDate, m)

        while(isMonday(currDate) == False):
            currDate = date(currDate.year, currDate.month, currDate.day - 1)
            
        datesList.append(currDate)

#Write sorted dates to file
datesList.sort()
with open(outputFileName, 'w') as outputFile:
    for currDate in datesList:
        outputFile.write(str(currDate.year) + '-' + str(currDate.month) + '-' + str(currDate.day) + '\n')
                    


