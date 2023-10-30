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
