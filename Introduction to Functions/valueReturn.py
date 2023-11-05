#1. Total_ages.py
#This program uses the return value of a function.

"""
def main():
    firstAge = int(input("Enter your age: "))
    secondAge = int(input("Enter your best friend's age: "))

    total = sum(firstAge, secondAge)

    print("Together you are", total, "years old.")

def sum(num1, num2):
    result = num1 + num2
    return result

main()

"""



#2. Sale_price.py
#This program calculates a retail item's sale price.

"""
DISCOUNT_PERCENTAGE = 0.2

def main():
    reg_price = getRegularPrice()

    salePrice = reg_price - discount(reg_price)

    print("The sale price is $", format(salePrice, ",.2f"), sep="")


def getRegularPrice():
    price = float(input("Enter the item's regular price: "))
    return price

def discount(price):
    return price * DISCOUNT_PERCENTAGE

main()

"""



#3. Modularizing with functions 
def main():
    sales = getMonthlySales()
    advance_pay = getAdvancePay()
    comm_rate = cal_CommissionRate(sales)

    pay = sales * comm_rate - advance_pay

    print("The pay is $", format(pay, ",.2f"), sep="")

    if pay < 0:
        print("The Salesperson must reimburse the company.")



def getMonthlySales():
    monthlySales = float(input("Enter the monthly sales: "))
    return monthlySales

def getAdvancePay():
    print("Enter the advance pay, or enter 0 if no advanced pay was given: ")
    advancePay = float(input("Enter the advanced pay: "))
    return advancePay

def cal_CommissionRate(sales):
    if sales < 10000:
        rate = 0.10
    elif sales >= 10000 and sales <= 14999.99:
        rate = 0.12
    elif sales >= 15000 and sales <= 17999.99:
        rate = 0.14
    elif sales >= 18000 and sales <= 21999.99:
        rate = 0.16
    else:
        rate = 0.18

    return rate



