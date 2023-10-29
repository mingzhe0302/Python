# #Personal information
# print("Name   :Yeoh Ming Zhe")
# print("Address: Malaysia, Kedah, 05150" )
# print("Phone  : 012-5896448")
# print("Major  : Diploma In computer science")


# #Sales Prediction
# totalSales = float(input("Enter your total sales: RM "))
# profit = totalSales * 0.23

# print("Your profit is : RM ", totalSales)

# #Land Calculation
# squareFeet = int(input("Enter a number of squareFeets: "))
# acre = squareFeet / 43560

# print("Number of acres in the tract is ", acre)

# #Total Purchase
# item1 = float(input("Enter the price: RM "))
# item2 = float(input("Enter the price: RM "))
# item3 = float(input("Enter the price: RM "))
# item4 = float(input("Enter the price: RM "))
# item5 = float(input("Enter the price: RM "))

# subtotal = item1 + item2 + item3 + item4 + item5
# tax = 0.07
# total = subtotal * (1 + tax)

# print("Here is your sales details:")
# print("Subtotal: RM ", subtotal)
# print("Tax: " + format(tax, ".0%"))
# print("Total : RM ", format(total, ".2f"))


# #Distance Traveled
# speed = 70
# print("The distance the car will travel in 6 hours: ", speed * 6, "miles")
# print("The distance the car will travel in 10 hours:", speed * 10, "miles")
# print("The distance the car will travel in 15 hours:", speed * 15, "miles")


# #Sales Tax
# purAmount = float(input("Enter a number of purchase amount: RM "))
# stateTax = 0.05
# countryTax = 0.025
# totalTax = stateTax + countryTax
# totalAmount = purAmount + totalTax

# print("Sales Tax info:")
# print("Amount of the purchase: RM ", format(purAmount, ".2f"))
# print("State sales tax: ", format(stateTax, ".2%"))
# print("Country sales tax: ", format(countryTax, ".3%"))
# print("Total sale: RM ", format(totalAmount, ".2f"))


# #Miles-per-Gallon
# milesDriven = float(input("Enter the miles driven: "))
# gallonsOfGas = float(input("Enter the gallons of gas: "))

# MPG = milesDriven / gallonsOfGas

# print("The MPG = ", format(MPG, ".2f"))

# #Tip, Tax, and Total
# priceOfMeal = float(input("Enter the price of the meal: RM "))
# tip = 0.18
# tax = 0.07
# totalPrice = priceOfMeal * (1 + (tip + tax))

# print("Price of Meal: RM", format(priceOfMeal, ".2f"))
# print("Tip: ", format(tip, ".2%"))
# print("Tax: ", format(tax, ".2%"))
# print("Total Price: RM ", format(totalPrice, ".2f"))

# #Celsius to Fahrenheit Temperature Converter
# celsius = float(input("Enter a temperature: "))
# Fahrenheit = (9/5) * celsius + 32
# print(celsius, "C = ", Fahrenheit, "F")

# #Ingredient Adjuster
# cookiesNum = int(input("Enter a number of cookies you want to make: "))
# sugar = cookiesNum / 1.5
# butter = cookiesNum / 1
# flour = cookiesNum / 2.75

# print("Cookies Ingredients needed: ")
# print("Sugar needs: ", format(sugar, ".2f"))
# print("Butter needs: ", format(butter, ".0f"))
# print("Flour needs: ", format(flour, ".2f"))

# #Male and Female Percertage 
# male = int(input("Enter a number of male student in a class: "))
# female = int(input("Enter a number of male student in a class: "))

# total = male + female
# percentOfMale = male / total
# percentOfFemale = female / total

# print("Percentage of male in a class is: ", format(percentOfMale, ".2%"))
# print("Percentage of female in a class is: ", format(percentOfFemale, ".2%"))


#Stock Transaction Program
numOfSharedPurchased = 2000
amountPaidPerShared = 40.00
amountPaidForStock = numOfSharedPurchased * amountPaidPerShared
commissionForBuying = amountPaidForStock * 0.03

numOfSharedSold = 2000
amountSoldPerShared = 42.75
amountReceivedForStock = numOfSharedSold * amountSoldPerShared
commissionForSelling = amountReceivedForStock * 0.03

Profit = (amountReceivedForStock - commissionForSelling) - (amountPaidForStock - commissionForBuying)

print("Amount of money Joe paid for the stock: $"+ format(amountPaidForStock, ",.2f"))
print("Amount of commission Joe paid his broker when he bought the stock: $" + format(commissionForBuying, ",.2f"))
print("Amount that Joe sold the stock: $" + format(amountReceivedForStock, ",.2f"))
print("Amount of commission Joe paid his broker when he sold the stock: $" + format(commissionForSelling, ",.2f"))
print("Profit: $" + format(Profit, ",.2f"))
