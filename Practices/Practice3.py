#1. Bug Collector
startDay = 1
dayOfCollectBug = 5
totalBugs = 0

while startDay <= dayOfCollectBug:
    print("Day: ", startDay)
    bugsCollected = int(input("Enter a number of bugs collected in five days: "))
    totalBugs += bugsCollected
    startDay += 1


print("Total number of bugs collected in five days: " , totalBugs)



#2. Calories burned
caloriesBurnedPerMinute = 4.2
time = 10

while time <= 30:
    caloriesBurnedPerMinute *= time
    print("The number of calories burned after", time, "minutes is", format(caloriesBurnedPerMinute, ".2f"))
    time += 5



#3. Budget Analysis
userBudgets = float(input("Enter your budgets per month: "))
moreExpenses = 'y'
totalExpenses = 0.0

while moreExpenses == 'y':
    expenses = float(input("Enter your expenses: "))
    totalExpenses += expenses

    moreExpenses = input("Do you have more expenses: [Y for yes, N for no]: ")


if totalExpenses > userBudgets:
    print("You is over budget.")
elif totalExpenses < userBudgets:
    print("You is under budget.")
else:
    print("You used exactly your budgets of RM", format(userBudgets, ",.2f"))




#4. Distance Traveled
speed = float(input("What is a speed of the vehicle in mph? "))
time = int(input("How many hours has it traveled? "))

print("Hour\t\tDistance Traveled")
print("--------------------------")
for hour in range(1, time + 1):
    distanceTraveled = speed * hour
    print(format(hour + 1, ".0f"), "\t\t", format(distanceTraveled, ".0f"))




#5. Average Rainfall
numberOfyears = int(input("Enter a number of years: "))
totalInches = 0
totalMonth = 0


for currentYear in range(1, numberOfyears + 1):
    for currentMonth in range(1, 13):
            inchesOfRainfall = float(input("Enter a inches of a rainfall: "))
            totalInches += inchesOfRainfall
            totalMonth += 1

averageRainfall = totalInches / totalMonth

print("The number of months: ", format(totalMonth, ".0f"))
print("The total inches of rainfall: ", format(totalInches, ".2f"))
print("The average rainfall per month for the entire period: ", format(averageRainfall, ".2f"))





#6. Celsius to Fahrenheit Table
print("Celsius\t\tFahrenheit")
print("---------------------")
for currentCelsius in range(1, 21):
    fahrenheit = (9/5)*currentCelsius + 32
    print(format(currentCelsius, ".2f"), "\t\t", format(fahrenheit, ".2f"))
    currentCelsius += 1



#7. Pennies for Pay
penny = 0.01
dayPeriod = int(input("Enter a number of days: "))
totalPay = 0
totalPennies = 0

print("Day\t\tPennies Earned")
for currentDay in range(dayPeriod):
    pennyEarned = penny
 
    print(currentDay + 1, "\t\t$", pennyEarned)

    totalPennies += pennyEarned
    penny *= 2

print("Total pay: $", format(totalPennies, ".2f"))



#8. Sum of numbers
total = 0
number = float(input("Enter a number: "))

while number > 0.0:
    number = float(input("Enter a number [negative num to end]: "))
    total += number

print("The sum of all number is: ", format(total, ".2f"), sep="")




#9. Ocean levels
risingLevel = 1.6

print("Next year\t\tMillimeters")
for currentLevel in range(1, 26):
    millimeters = currentLevel * risingLevel
    print(currentLevel,"\t\t\t",format(millimeters, ".2f"))
    currentLevel + 1



#10. Tuition Increase
semesterFee = 8000
increaseRate = 0.03

for currentYear in range(1, 6):
    semesterFee += semesterFee * increaseRate
    print(currentYear,"\t",format(semesterFee, ".2f"))
    currentYear += 1




#11. Calculating the factorial of a number
num = int(input("Enter a positive number: "))
factorial = 1

while num < 0:
    num = int(input("Enter a positive number: "))

for x in range(1, num + 1):
    factorial *= x
    

print(num,"! =",format(factorial, ".0f"))



#12. Population
startingOrganisms = float(input("Enter a starting number of organisms: "))
avgDailyInc = float(input("Enter a average daily increase: "))
numberOfDays = int(input("Enter a numberof day to multiply: "))


print("Day Approximate    Population")

for currentDay in range(1, numberOfDays + 1):
    print(currentDay,"\t  \t",format(startingOrganisms, ".2f"))
    startingOrganisms = startingOrganisms * (1 + avgDailyInc)
    currentDay += 1




#13. Pattern(*) drawing
for row in range(7, 0, -1):
    for col in range(row, 0, -1):
        print("*", end="")
    print()



#14. Pattern(*) drawing
for row in range(6):
    print("#", end="",sep="")
    for spaces in range(row):
        print(" ", end="", sep="")
    print("#", sep="")





