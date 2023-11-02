#1. Day of the Week
numberOfDays = int(input("Enter a number in range of 1 through 7: "))

if numberOfDays == 1:
    print("Monday")
elif numberOfDays == 2:
    print("Tuesday")
elif numberOfDays == 3:
    print("Wednesday")
elif numberOfDays == 4:
    print("Thursday")
elif numberOfDays == 5:
    print("Friday")
elif numberOfDays == 6:
    print("Saturday") 
elif numberOfDays == 7:
    print("Sunday")
else:
    print("The number is out of the range of 1 through 7.")


#2. Areas of Rectangles
length1 = float(input("Enter a length of rectangle 1: "))
width1 = float(input("Enter a width of rectangle 1: "))

length2 = float(input("Enter a length of rectangle 2: "))
width2 = float(input("Enter a width of rectangle 2: "))

area1 = length1 * width1
area2 = length2 * width2

if area1 == area2:
    print("Their areas are the same.")
elif area1 > area2:
    print("Area of rectangle 1 is greater than rectangle 2")
else:
    print("Area of rectangle 2 is greater than rectangle 1")



#3. Age Classifier
years = int(input("Enter your age: "))
 
if years <= 1:
    print("He/She is an infant")
elif years > 1 and years < 13:
    print("He or She is child")
elif years >= 13 and years < 20:
    print("He or She is a teenager")
elif years >= 20:
    print("He or She is an adult")



#4. Roman Numerals
num = int(input("Please enter a number 1 through 10: "))
if num == 1:
    print("I")
elif num == 2:
    print("II")
elif num == 3:
    print("III")
elif num == 4:
    print("IV")
elif num == 5:
    print("V")
elif num == 6:
    print("VI")
elif num == 7:
    print("VII")
elif num == 8:
    print("VIII")
elif num == 9:
    print("IX")
elif num == 10:
    print("X")
else:
    print("The number is out of range: ")




#5. Mass and weight
objectMass = float(input("Enter a mass of the object: "))

weight = objectMass * 9.8

if weight > 500:
    print("The object is too heavy.")
elif weight < 100:
    print("The object is too light.")



#6. Magic dates
month = int(input("Enter a month: "))
day = int(input("Enter a day: "))
year = int(input("Enter a two-digit year: "))

if month * day == year:
    print("The date is magic.")
else:
    print("The date is not magic.") 





#7. Color Mixer
color1 = input("Enter a first primary color: ")
color2 = input("Enter a second primary color:")


if color1 == "red" and  color2 == "blue":
    print("You get purple.")
elif color1 == "red" and  color2 == "yellow":
    print("You get orange.")
elif color1 == "blue" and  color2 == "yellow":
    print("You get green.")
else:
    print("The color cannot mixed.")



#8. Hot Dog Cookout Calculator
HOTDOGS= 10
HOTDOGS_BUN = 8
numOfPeopleAttend = int(input("Enter a number of people: "))
numOfHotdogsGiven = int(input("Enter a number of hot dogs each person will be given: "))

totalNumOfHotdogs = numOfPeopleAttend * numOfHotdogsGiven
numOfHotdogsInPackage = totalNumOfHotdogs / HOTDOGS
numOfHotdogsBunInPackage = totalNumOfHotdogs/ HOTDOGS_BUN

numberOfHotdogsLeftOver = totalNumOfHotdogs % HOTDOGS
numberOfHotdogsBunLeftOver = totalNumOfHotdogs % HOTDOGS_BUN

print("Minimum number of packages of hot dogs required = ", numOfHotdogsInPackage)
print("Minimum number of packages of hot dogs bun required = ", numOfHotdogsBunInPackage)
print("Number of hot dogs that will be left over = ", numberOfHotdogsLeftOver)
print("Number of hot dogs bun that will be left over = ", numberOfHotdogsBunLeftOver)



#9. Roulette wheel colors
pocketNum = int(input("Enter a pocket number: "))

if(pocketNum == 0):
    print("The pocket number is green.")

elif(pocketNum >= 1 and pocketNum <= 10):
    if(pocketNum % 2 == 0):
        print("The even-numbered pockets are black.")
    elif(pocketNum % 2 == 1):
        print("The odd-numbered pockets are red.")

elif(pocketNum >= 11 and pocketNum <= 18):
    if(pocketNum % 2 == 0):
        print("The even-numbered pockets are red.")
    elif(pocketNum % 2 == 1):
        print("The odd-numbered pockets are black.")

elif(pocketNum >= 19 and pocketNum <= 28):
    if(pocketNum % 2 == 0):
        print("The even-numbered pockets are black.")
    elif(pocketNum % 2 == 1):
        print("The odd-numbered pockets are red.")
    
elif(pocketNum >= 29 and pocketNum <= 36):
    if(pocketNum % 2 == 0):
        print("The even-numbered pockets are red.")
    elif(pocketNum % 2 == 1):
        print("The odd-numbered pockets are black.")
else:
    print("The pocket number is out of range, should inside the range of 0 through 36.")



#10. Money Counting game
pennies = int(input("Please enter a number of pennies: "))
nickels = int(input("Please enter a number of nickels: "))
dimes = int(input("Please enter a number of dimes: "))
quarters = int(input("Please enter a number of quarters: "))

valueOfPennies = pennies * 1
valueOfNickels = nickels * 5
valueOfDimes = dimes * 10
valueOfQuarters = quarters * 25

totalValue = valueOfPennies + valueOfNickels + valueOfDimes + valueOfQuarters

ONEDOLLAR = 100

if(totalValue == ONEDOLLAR):
    print("Congratulation, You win a game.")
elif(totalValue < ONEDOLLAR):
    print("The amount entered was less than one dollar.")
else:
      print("The amount entered was more than one dollar.")




#11. Book Club Points
bookPurchase = int(input("Enter a number of book purchased this month: "))

if bookPurchase == 0:
    points = 0
elif bookPurchase == 2:
    points = 5
elif bookPurchase == 4:
    points = 15
elif bookPurchase == 6:
    points = 30
elif bookPurchase >= 8:
    points = 60

print("The number of points awarded this month: " + format(points, ".2f"))




#12. Software sales
packagePurchased = int(input("Enter a number of package purchased: "))

PACKAGE_PRICE = 99

if packagePurchased < 10:
    discount = 0.0
elif packagePurchased >= 10 and packagePurchased <= 19:
    discount = 0.1
elif packagePurchased >= 20 and packagePurchased <= 49:
    discount = 0.2
elif packagePurchased >= 50 and packagePurchased <= 99:
    discount = 0.3
elif packagePurchased >= 100:
    discount = 0.4
    
totalPrice = packagePurchased * PACKAGE_PRICE * (1 - discount)
print("The amount of discount is RM " + format(discount, ".2%"))
print("The total amount of the purchase after the discount is RM " + format(totalPrice, ".2f"))



#13. Shipping Charges
packageWeight = float(input("Enter a pounds of a packages: "))

if packageWeight <= 2:
    ratePerPound = 1.5
elif packageWeight > 2 and packageWeight <= 6:
    ratePerPound = 3.0
elif packageWeight > 6 and packageWeight <= 10:
    ratePerPound = 4.0
elif packageWeight > 10:
    ratePerPound = 4.75

print("The shipping charges is $ " + format(ratePerPound, ".2f"))



#14. Body Mass Index
weightOfBody = float(input("Enter your weight: "))
heightOfBody = float(input("Enter your height: "))

BMI = (weightOfBody * 703) / heightOfBody ** 2

if BMI >= 18.5 and BMI <= 25:
    print("Your weight consider as a optimal weight.")
elif BMI < 18.5:
    print("Your weight consider as a underweight.")
elif BMI > 25:
    print("Your weight consider as a overweight.")




#15. Time Calculator
second = float(input("Enter a number of seconds: "))

ONE_MINUTE = second / 60
ONE_HOUR = second / 3600
ONE_DAY = second / 86400

if second >= 60:
    print("The number of ", format(ONE_MINUTE, ".2f"), "minutes in that ", second, "second.")
elif second >= 3600:
    print("The number of ", format(ONE_HOUR, ".2f"), "hours in that ", second , "second.")
elif second >= 86400:
    print("The number of ", format(ONE_DAY, ".2f"),  "days in that ", second , "second.")

