import random

import time

def getRandomDate(startDate, endDate):

    print("Printing random date between", startDate, " and ", endDate)

    randomGenerator = random.random() # ✅ Add parentheses here

    dateFormat = '%m/%d/%Y' # ✅ Correct 4-digit year format

    startTime = time.mktime(time.strptime(startDate, dateFormat))

    endTime = time.mktime(time.strptime(endDate, dateFormat))

    randomTime = startTime + randomGenerator * (endTime - startTime)

    randomDate = time.strftime(dateFormat, time.localtime(randomTime))

    return randomDate

print("Random date = ", getRandomDate("1/1/2016", "12/12/2018"))