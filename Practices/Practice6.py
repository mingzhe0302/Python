#1. Total Sales
def main():

    dayInWeek = 7
    sales = []

    for currentDay in range(1, dayInWeek + 1, 1):

        storeSales = float(input("Please enter the sales for day " + str(currentDay) + ": "))
        sales.append(storeSales)

    
    total = sum(sales)
    
    print("The total sales of the week is: $", format(total, ",.2f"), sep="")


#2. Lottery Number Generator
import random

def main():
    lotteryNum = []

    for x in range(7):
        lotteryNum.append(random.randint(0, 9))

    print("Generated Lottery Number: ")
    for number in lotteryNum:
        print(number, end="")



#3. Rainfall Statistics
def getRainfallAmounts(namesOfMonths):
    NUMBER_OF_MONTH_IN_A_YEAR = 12
    totalRainFallList = []

    for currentMonth in range(NUMBER_OF_MONTH_IN_A_YEAR):
        monthlyRainfall = float(input("Please enter the rainfall amount for " + namesOfMonths[currentMonth] + ": "))
        totalRainFallList.append(monthlyRainfall)

    return totalRainFallList

def calcTotalRainfall(totalRainFallList):

    totalRainfall = 0

    for currentMonth in range(len(totalRainFallList)):
        totalRainfall += totalRainFallList[currentMonth]

    return totalRainfall

def calcAverageRainfall(totalRainfall, totalRainFallList):
    numberOfMonths = len(totalRainFallList)

    averageRainfall = totalRainfall / numberOfMonths

    return averageRainfall

def determineHigh(totalRainfallList):

    highest = max(totalRainfallList)

    return highest

def determineLow(totalRainfallList):

    lowest = min(totalRainfallList)

    return lowest


def main():

    namesOfMonths = ["January", "February", "March", "April", "May", "June", "July",\
                     "August", "September", "October", "November", "December"]
    
    totalRainfallList = []

    totalRainfallList = getRainfallAmounts(namesOfMonths)

    totalRainfall = calcTotalRainfall(totalRainfallList)

    averageRainfall = calcAverageRainfall(totalRainfall, totalRainfallList)

    highestRainfall = determineHigh(totalRainfallList)

    lowestRainfall = determineLow(totalRainfallList)

    print("The total rainfall for the year is", format(totalRainfall, ".2f"))
    print("The average rainfall of the year is", format(averageRainfall, ".2f"))
    print("The highest rainfall in the year is", format(highestRainfall, ".2f"))
    print("The lowest rainfall in the year is", format(lowestRainfall, ".2f"))




#4. Number Analysis Program
def getNum():

    seriesNumberList = []

    for currentIndex in range(1, 21, 1):
        num = float(input("Enter number" + str(currentIndex) + ": "))
        seriesNumberList.append(num)

    return seriesNumberList

def isHighest(numList):

    highestNum = max(numList)
    return highestNum

def isLowest(numList):

    lowestNum = min(numList)
    return lowestNum

def calcTotal(numList):

    total = 0

    for num in numList:
        total += num

    return total

def calcAvg(total, numList):

    average = total / len(numList)
    return average

def main():

    numberList = []

    numberList = getNum()

    highestNum = isHighest(numberList)
    lowestNum = isLowest(numberList)

    total = calcTotal(numberList)

    average = calcAvg(total, numberList)

    print("The highest number is", highestNum)
    print("The lowest number is", lowestNum)
    print("The total is", total)
    print("The average is", average)



#5. Larger than n
def isGreater(numList, n):

    for x in range(len(numList)):
        if numList[x] > n:
            print(numList[x], end=" ")

def main():

    numList = [23, 39, 39, 20, 48, 39, 85, 93]

    n = 55

    isGreater(numList, n)



#7. Driver's License Exam
def main():
    correctAnswer = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B',\
                     'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']
    
    incorrectQuestion = []

    numberOfCorrect = 0
    numberOfIncorrect = 0

    try:
        fp = open("stdAns.txt", "r")

        stdAns = list(fp.read().strip())

    except FileNotFoundError:
        print("File not found. Please make sure the file exists.")
        exit()

    for i in range(len(correctAnswer)):
        if stdAns[i] == correctAnswer[i]:
            numberOfCorrect += 1
        else:
            numberOfIncorrect += 1
            incorrectQuestion.append(i + 1)

    print("Results: ")
    print(f"Total correct answer: {numberOfCorrect}")
    print(f"Total incorrect answer: {numberOfIncorrect}")

    if numberOfCorrect > 15:
        print("Congratulation!")
        print("You passed the exam")
    else:
        print("You failed the exam.")

    if numberOfIncorrect > 0:
        print("Incorrect answered question:")
        print(incorrectQuestion)




#7. Lo Shu Magic Square
def getRowsAndColums(user2DList):

    numberOfRows = len(user2DList)
    numberOfColums = len(user2DList[0])

    return numberOfRows, numberOfColums

def getFirstRowSum(user2DList, numberOfColums):
    firstRowSum = 0

    for currentRowIndex in range(1):
        for currentColIndex in range(numberOfColums):
            firstRowSum += user2DList[currentRowIndex][currentColIndex]

    return firstRowSum

def hasEqualRowSum(user2DList, firstRowSum, numberOfRows, numberOfColumns):

    rowSum = 0

    for currentRow in range(numberOfRows):
        for currentCol in range(numberOfColumns):
            rowSum += user2DList[currentRow][currentCol]

        if rowSum != firstRowSum:
            return False

        rowSum = 0
    
    return True


def hasEqualColumnSum(user2DList, firstRowSum, numberOfRows, numberOfColumns):

    colSum = 0

    for currentRow in range(numberOfRows):
        for currentCol in range(numberOfColumns):
            colSum += user2DList[currentRow][currentCol]

        if colSum != firstRowSum:
            return False

        rowSum = 0
    
    return True

def hasEqualRowAndColSum(user2DList, firstRowSum, numberOfRows, numberOfColumns):

    if hasEqualRowSum(user2DList, firstRowSum, numberOfRows, numberOfColumns) and\
    hasEqualColumnSum(user2DList, firstRowSum, numberOfRows, numberOfColumns):
        return True
    else:
        return False


def hasFromLeftEqualDiagonalSum(user2DList, lengthOfAnyRowOrCol, firstRowSum):
    fromLeftDiagonalSum = 0

    for currentIndex in range(lengthOfAnyRowOrCol):
        fromLeftDiagonalSum += user2DList[currentIndex][currentIndex]

    if fromLeftDiagonalSum != firstRowSum:
        return False
    
    else:
        return True
    

def hasFromRightEqualDiagonalSum(user2DList, lengthOfAnyRowOrCol, firstRowSum):
    fromRightDiagonalSum = 0

    for currentIndex in range(lengthOfAnyRowOrCol):
        fromRightDiagonalSum += user2DList[currentIndex][currentIndex]

    if fromRightDiagonalSum != firstRowSum:
        return False
    
    else:
        return True

def hasEqualDiagonalSum(user2DList, lengthOfAnyRowOrCol, firstRowSum):

    if hasFromLeftEqualDiagonalSum(user2DList, lengthOfAnyRowOrCol, firstRowSum) and\
    hasFromRightEqualDiagonalSum(user2DList, lengthOfAnyRowOrCol, firstRowSum):
        
        return True
    
    else:

        return False
    

def isLoShuSquare(user2DList, firstRowSum, numberOfRows, numberOfColumns, lengthOfAnyRowOrCol):
    if hasEqualRowAndColSum(user2DList, firstRowSum, numberOfRows, numberOfColumns)\
    and\
    hasEqualDiagonalSum(user2DList, lengthOfAnyRowOrCol, firstRowSum):
            return True
    
    else:

            return False

def main():
    user2DList = [
        [4, 9, 2],
        [3, 5, 7],
        [8, 1, 6]
    ]

    numberOfRows, numberOfColumns = getRowsAndColums(user2DList)

    lengthOfAnyRowAndColumns = numberOfRows

    firstRowSum = getFirstRowSum(user2DList, numberOfColumns)

    if isLoShuSquare(user2DList, firstRowSum, numberOfRows, numberOfColumns, lengthOfAnyRowAndColumns):

        print("This list is a Lo Shu Magic Square.")

    else:

        print("This list is NOT a Lo Shu Magic Square.")


main()