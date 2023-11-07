#1. Kilometer Converter
"""
def getDistance():
    distance = float(input("Enter the distance in kilometer: "))

    return distance

def converToMiles(kilometers):
    miles = kilometers * 0.6214

    return miles

def main():
    distanceInKilo = getDistance()
    convertedMiles = converToMiles(distanceInKilo)
    print(format(convertedMiles, ".2f"), "miles", sep=" ")


main()

"""


#2. Sales Tax Programming Refactoring
"""
def askAmountOfPurchase():
    purAmount = float(input("Enter a number of purchase amount: RM "))
    return purAmount

def calStateTax(purAmount):
    stateTax = 0.05 * purAmount
    return stateTax

def calCountryTax(purAmount):
    countryTax = 0.025 * purAmount
    return countryTax

def calTotalTax(stateTax, countryTax):
    totalTax = stateTax + countryTax
    return totalTax

def calTotalAmount(totalTax, purAmount):
    totalSale = purAmount + totalTax
    return totalSale

def main():
    purAmount = askAmountOfPurchase()
    stateTax = calStateTax(purAmount)
    countryTax = calCountryTax(purAmount)
    totalTax = calTotalTax(stateTax, countryTax)
    totalSale = calTotalAmount(totalTax, purAmount)

    print("Sales Tax info:")
    print("Amount of the purchase: RM ", format(purAmount, ".2f"))
    print("State sales tax: ", format(stateTax, ".2%"))
    print("Country sales tax: ", format(countryTax, ".3%"))
    print("Total sale: RM ", format(totalSale, ".2f"))

"""

#3. How much Insurance?
"""
def getReplaceCost():
    replaceCost = float(input("Enter the amount of replacement of the building: $"))
    return replaceCost

def calInsurance(replaceCost):
    insurance = replaceCost * 0.8
    return insurance

def main():
    replaceCost = getReplaceCost()
    insurance = calInsurance(replaceCost)
    print("You must pay $", format(insurance, ",.2f"), sep="")

main()

"""


#4. Automobile Costs
"""
def getMonthlyExpenses():
    loanPayment = float(input("Enter your expenses amount for loan payment: "))
    insurance = float(input("Enter your expenses amount for insurance: "))
    gas = float(input("Enter your expenses amount for gas: "))
    oil = float(input("Enter your expenses amount for oil: "))
    tires = float(input("Enter your expenses amount for tires: "))
    maintenance = float(input("Enter your expenses amount for maintenance: "))

    return loanPayment, insurance, gas, oil, tires, maintenance

def calMonthCost(loanPayment, insurance, gas, oil, tires, maintenance):
    monthlyCost = loanPayment + insurance + gas + oil + tires + maintenance
    return monthlyCost

def calYearCost(monthlyCost):
    yearlyCost = monthlyCost * 12
    return yearlyCost

def printDetails(monthlyCost, yearlyCost):
    print("Total monthly cost of loanPayment, insurance, gas, oil, tires, maintenance"\
          "= $", format(monthlyCost, ",.2f"), sep="")
    
    print("Total yearly cost of loanPayment, insurance, gas, oil, tires, maintenance"\
          "= $", format(yearlyCost, ",.2f"), sep="")

def main():
    loanPayment, insurance, gas, oil, tires, maintenance = getMonthlyExpenses()
    monthlyCost = calMonthCost(loanPayment, insurance, gas, oil, tires, maintenance)
    yearlyCost = calYearCost(monthlyCost)
    printDetails(monthlyCost, yearlyCost)

main()

"""



#5. Property Tax
"""
def getPropertyActualValue():
    propertyValue = float(input("Enter a actual value of property: $"))
    return propertyValue

def calAssessmentValue(propertyValue):
    assessmentValue = propertyValue * 0.6
    return assessmentValue

def calPropertyTax(assessmentValue):
    propertyTax = (assessmentValue / 100) * 0.72
    return propertyTax

def main():
    propertyValue = getPropertyActualValue()
    assessmentValue = calAssessmentValue(propertyValue)
    propertyTax = calPropertyTax(assessmentValue)

    print("The assessment value is $", format(assessmentValue, ",.2f"), sep="")
    print("The property tax is $", format(propertyTax, ",.2f"), sep="")


main()

"""



#6. Calories from fat and carbohhydrates

"""
def getFat_Carb_Grams():
    fatGrams = float(input("Enter your fat grams consumed in a day: "))
    carbGrams = float(input("Enter yout carbohydrate grams consumed in a day: "))
    return fatGrams, carbGrams

def calCaloriesFromFat(fatGrams):
    caloFromFat = fatGrams * 9
    return caloFromFat

def calCaloriesFromCarbs(carbGrams):
    caloFromCarbs = carbGrams * 4
    return caloFromCarbs

def main():
    fatGrams, carbGrams = getFat_Carb_Grams()
    caloFromFat = calCaloriesFromFat(fatGrams)
    caloFromCarbs = calCaloriesFromCarbs(carbGrams)
    print("Calories from fat =", format(caloFromFat, ".2f"))
    print("Calories from carbs =", format(caloFromCarbs, ".2f"))

main()
"""



#7. Stadium Seating
"""
def menu():
    print("Seating categories")
    print("==================")
    print("Class A: $20")
    print("Class B: $15")
    print("Class C: $10")

    classA = int(input("Enter a number of ticket that you want to buy for class A: "))
    classB = int(input("Enter a number of ticket that you want to buy for class B: "))
    classC = int(input("Enter a number of ticket that you want to buy for class C: "))

    return classA, classB, classC


def calTicketIncome(classA, classB, classC):
    incomeOfA = classA * 20
    incomeOfB = classB * 15
    incomeOfC = classC * 10

    totalIncome = incomeOfA + incomeOfB + incomeOfC

    return totalIncome

def main():
    classA, classB, classC = menu()
    totalIncome = calTicketIncome(classA, classB, classC)
    print("Total amount of income generated from ticket sales: $", format(totalIncome, ",.2f"), sep="")

main()

"""



#8. Paint job Estimator
"""
CHARGEPERHOURS = 35
def getSquareFeet_WallSpace():
    squareFeet = float(input("Enter a square feet of wall space to be painted and the price of the paint per gallon: "))
    return squareFeet

def getPriceOfPaint():
    priceOfPaint = float(input("Enter a price of the paint: "))
    return priceOfPaint

def calPaintRequired(squareFeet):
    paintRequired = (squareFeet / 112) * 1
    return paintRequired

def calHoursOfLabor(squareFeet):
    hoursRequires = (squareFeet / 112) * 8
    return hoursRequires

def calCostOfPaint(priceOfFeet, paintRequired):
    costOfPaint = priceOfFeet * paintRequired
    return costOfPaint

def calLaborCharges(hoursRequires):
    laborCharges = hoursRequires * CHARGEPERHOURS
    return laborCharges

def calTotalCost(costOfPaint, laborCharges):
    totalCost = costOfPaint + laborCharges
    return totalCost

def main():
    squareFeet  = getSquareFeet_WallSpace()
    priceOfPaint = getPriceOfPaint()
    paintRequired = calPaintRequired(squareFeet)
    hoursRequired = calHoursOfLabor(squareFeet)
    costOfPaint = calCostOfPaint(priceOfPaint, paintRequired)
    laborCharges = calLaborCharges(hoursRequired)
    totalCost = calTotalCost(costOfPaint, laborCharges)

    print("The number of gallons of paint required: ",format(paintRequired, ".1f"), sep="")
    print("The hours of labor required: ", hoursRequired)
    print("Cost of the paint: $", format(costOfPaint, ",.2f"), sep="")
    print("The labor charges: $", format(laborCharges, ",.2f"), sep="")
    print("The total cost of the paint job: $", format(totalCost, ",.2f"), sep="")


main()

"""


#9. Monthly Sales Tax
"""
def getTotalSalesOfMonth():
    sales = float(input("Enter a total sales for the month: $"))
    return sales

def calCountryTax(sales):
    countryTax = sales * 0.025
    return countryTax

def calStateTax(sales):
    stateTax = sales * 0.05
    return stateTax

def calTotalSalesTax(countryTax, stateTax):
    totalTax = countryTax + stateTax
    return totalTax

def main():
    sales = getTotalSalesOfMonth()
    countryTax = calCountryTax(sales)
    stateTax = calStateTax(sales)
    totalTax = calTotalSalesTax(countryTax, stateTax)

    print("The amount of country sales tax: $", format(countryTax, ",.2f"), sep="")
    print("The amount of state sales tax: $", format(stateTax, ",.2f"), sep="")
    print("The amount of total sales tax: $", format(totalTax, ",.2f"), sep="")

main()

"""



#10. Feet to inches
"""
def feet_to_inches(numOfFeet):
    inches = numOfFeet * 12
    return inches

def main():
    numOfFeet = int(input("Enter a number of feet: "))
    inches = feet_to_inches(numOfFeet)
    print(numOfFeet, "feets equals", inches, "inches")

main()

"""



#11. Math Quiz
"""
import random

num1 = random.randint(1, 250)
num2 = random.randint(1, 250)

def calSum(num1, num2):
    sum = num1 + num2
    return sum

def getAnswer():
    answer = int(input("Enter the answer: "))
    return answer

def main():

    print(num1)
    print("+")
    print(num2)
    
    answer = getAnswer()
    sum = calSum(num1, num2)

    if answer == sum:
        print("Congratulation!, you are correct.")
    else:
        print("The correct answer is", sum)

main()

"""


#12. Maximum of two values

"""
def max(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2
    
def main():
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter a number: "))

    maxNum = max(num1, num2)

    print("The largest number is", maxNum)

main()

"""



#13. Falling Distance
"""
def falling_distance(fallingTime):
    distance = (0.5 * 9.8) * fallingTime ** 2
    return distance

def main():
    for x in range(1, 11):
        distance = falling_distance(x)
        print("In", x, "second, the distance is", format(distance, ".2f"))

main()

"""



#14. Kinetic Energy
"""
def kinetic_energy(mass, velocity):
    KE = 0.5 * mass * velocity ** 2

    return KE

def main():
    mass = float(input("Enter a mass: "))
    velocity = float(input("Enter a velocity: "))
    KE = kinetic_energy(mass, velocity)
    print("The kinetic energy is", format(KE,".2f"))

main()
"""



#15. Test Average and Grade
"""
def calc_average(num1, num2, num3, num4, num5):
    average = (num1 + num2 + num3 + num4 + num5) / 5
    return average

def determine_grade(average):
    if average >= 90 and average <= 100:
        letterGrade = 'A'
    elif average >= 80 and average <= 89:
        letterGrade = 'B'
    elif average >= 70 and average <= 79:
        letterGrade = 'C'
    elif average >= 60 and average <= 69:
        letterGrade = 'D'
    else:
        letterGrade = 'F'
    
    return letterGrade


def main():
    num1 = float(input("Enter your score: "))
    num2 = float(input("Enter your score: "))
    num3 = float(input("Enter your score: "))
    num4 = float(input("Enter your score: "))
    num5 = float(input("Enter your score: "))

    average = calc_average(num1, num2, num3, num4, num5)
    letterGrade = determine_grade(average)

    print("Your letter grade is", letterGrade + ".")

main()

"""



#16. Odd/Even Counter
"""
import random

def generateRandomNumber():
    randomNumber = random.randint(1, 10)
    return randomNumber

def isOdd(number):
    if number % 2 == 1:
        return True
    return False

def main():
    numberOfOdd = 0
    numberOfEven = 0

    for x in range(1, 101):
        randomNumber = generateRandomNumber()
        if(isOdd(randomNumber)):
            numberOfOdd += 1
        else:
            numberOfEven += 1
    
    print("The number of odd: ", numberOfOdd)
    print("The number of even: ", numberOfEven)
    
main()
"""


#17. Prime Numbers
"""
import math

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    for currentNum in range(3, int(math.sqrt(num)) + 1, 2):
        if num % currentNum == 0:
            return False
    return True

def main():
    num = int(input("Enter an integer: "))
    if is_prime(num):
        print("The number is a prime number.")
    else:
        print("The number is not a prime number.")        

main()

"""

#18. Prime Number List
"""
import math
    
def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    for currentNum in range(3, int(math.sqrt(num)) + 1, 2):
        if num % currentNum == 0:
            return False
    return True

def displayPrimeNum():
    for number in range(1, 101):
        if is_prime(number):
            print(number, end=" ")

displayPrimeNum()

"""



#19. Future Value
"""
def getAccountPresentValue():
    accountPresentValue = float(input("Enter your account present value: $"))
    return accountPresentValue

def getMonthlyInterestRate():
    monthlyInterestRate = float(input("Enter a monthly interest rate: "))
    return monthlyInterestRate

def getMoneyLeft():
    months = float(input("Enter a number of months: "))
    return months

def calcFutureValue(accountPresentValue, monthlyInterest, numOfMonths):
    futureValue = accountPresentValue * (1 + monthlyInterest) ** numOfMonths
    return futureValue

def main():
    accountPresentValue = getAccountPresentValue()
    monthlyInterest = getMonthlyInterestRate()
    numOfMonths = getMoneyLeft()
    futureValue = calcFutureValue(accountPresentValue, monthlyInterest, numOfMonths)

    print("Your account future value is $", format(futureValue, ",.2f"), sep="")

main() 
"""



#20. Random number guessing game
"""
import random

def generate_random_num():
    return random.randint(1, 100)

def determine_num(num):
    attempts = 0  # Track the number of attempts

    while True:
        try:
            guess_num = int(input("Guess the number (1-100): "))
            attempts += 1
            if guess_num > num:
                print("Too high, try again.")
            elif guess_num < num:
                print("Too low, try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break  # Exit the loop if the correct number is guessed
        except ValueError:
            print("Please enter a valid integer.")

def main():
    num = generate_random_num()
    determine_num(num)

main()
"""


#21. Rock, Paper Scissors Game
"""
import random

def generateRandomNum():
    randomNum = random.randint(1, 3)

    if randomNum == 1:
        chosen = "rock"
    elif randomNum == 2:
        chosen = "paper"
    elif randomNum == 3:
        chosen = "scissors"

    return chosen

def getUserChoice():
    userChoice = input("Enter your choice (rock, paper, scissors): ")
    return userChoice

def determineWhoWin(userChoice, pcChosen):
    if userChoice == "rock" and pcChosen == "scissors":
        print("The user win.")
    elif pcChosen == "rock" and userChoice == "scissors":
        print("The computer win.")
    elif userChoice == "scissors" and pcChosen == "paper":
        print("The user win.")
    elif pcChosen == "scissors" and userChoice == "paper":
        print("The computer win.")
    elif userChoice == "paper" and pcChosen == "rock":
        print("The user win.")
    elif pcChosen == "paper" and userChoice == "rock":
        print("The computer win.")

def main():
    pcChoice = generateRandomNum()
    choice = getUserChoice()
    determineWhoWin(choice, pcChoice)

main()
"""