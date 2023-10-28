#Perform calculation
'''
+ - * / 
//(Integer division)
%(remainder)
**(exponent)
'''

# #sale_price.py
originPrice = float(input("Enter the original price of the item: "))
discount = originPrice * 0.2
salePrice = originPrice - discount

print("The price of the item after discount is : RM ", salePrice)


# #floating point and integer division
# #test_Score_Average.py
test1 = float(input("Enter your first test score: "))
test2 = float(input("Enter your second test score: "))
test3 = float(input("Enter your third test score: "))

average = (test1 + test2 + test3) / 3

print("The average score is: ", average)

# #Remainder operator
# #time_converter.py
totalSeconds = float(input("Enter a number of seconds: "))

hours = totalSeconds // 3600
minutes = (totalSeconds // 60) // 60
seconds = totalSeconds % 60

print("Here is the time in hours, minutes, and seconds: ")
print("Hours: ", hours)
print("Minutes: ", minutes)
print("Seconds: ", seconds)


# #Converting Math formulas to programming statements
# #future_value.py
futureValue = float(input("Enter the desired future value: "))
rate = float(input("Enter the annual interest rate: "))
years = int(input("Enter the number of years the money will grow: "))
presentValue = futureValue / (1 + rate) ** years

print("You will need to deposit this amount: ", presentValue)


# #More about data output
# #Suppressing the print function's ending newline
print("One", end=" ")
print("Two", end=" ")
print("Three")

# #Specifying an Item Separator
print("One", "Two", "Three")
print("One", "Two", "Three", sep="")   #if don't want a space printed between the items, use sep=""
print("One", "Two", "Three", sep="*")  #print a * between the items
print("One", "Two", "Three", sep="~~~")


# #Escape characters
# #\n \t  \'  \"  \\
print("Your assignment is to read \"Hamlet\" by tomorrow.")
print('I\'m ready to begin.')
print("The path is C: \\temp\\data.")

# #Displaying Multiple Items with the + Operator
print("This is " + "one string")
print("Enter the amount of " + 
      "sales for each day and " + 
       "press Enter.")

#Formatting numbers
#formatting.py
amount_due = 5000.0
monthly_payment = amount_due / 12
print("The monthly payment is", format(monthly_payment, ".2f"))

#Scientific notation
print(format(12345.6789, "e"))
print(format(12345.6789, ".2e"))

#Inserting Comma Separators
print(format(12345.6789, ",.2f"))
print(format(123456789.456, ",.2f"))
print(format(12345.6789, ",f"))

#dollar_display.py
monthly_pay = 5000.0
annual_pay = monthly_pay * 12
print("Your annual pay is $", \
      format(annual_pay, ",.2f"), \
        sep='')

#Specifying a minumum field width
print("The number is ", format(12345.6789, "12,.2f"))
#The number is 12, 345.68

print("The number is ", format(12345.6789, "12.2f"))
#The number is     12345.68

#Formatting percentage
print(format(0.5, "%"))
#50.000000%
print(format(0.5, ".0%"))
#50%

#Formatting integers
print(format(123456, "d"))
#123456
print(format(123456, ",d"))
#123,456
print(format(123456, "10d"))
#    123456
print(format(123456, "10,d"))
#    123,456