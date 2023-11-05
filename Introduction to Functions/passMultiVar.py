#1.
"""
def main():
    print("The sum of 12 and 45 is")
    showSum(12, 45)

def showSum(num1, num2):
    result = num1 + num2
    print(result)

main()

"""

#2. 
"""
def main()
    firstName = input("Enter your first name: ")
    lastName = input("Enter your last name: ")
    print("Your name reversed is ")
    reverseName(firstName, lastName)

def reverseName(first, last):
    print(first, last)

main()

"""


#3. Making changes to parameters
"""
def main():
    value = 99
    print("The value is", value)
    change_me(value)
    print("Back in main the value is", value)


def change_me(arg):
    print("I am changing the value.")
    arg = 0
    print("Now the value is", arg)

main()

"""


#4. Keywords Arguments 
#This program demonstrates keyword arguments.
"""
def main():
    showInterest(rate = 0.01, periods = 10, principle = 10000.0)

def showInterest(rate, periods, principle):
    interest = principle * rate * periods
    print("The simple interest will be $", format(interest, ",.2f"), sep="")

main()
"""


#5. Global variable and global constants
#Create a global variable
"""
my_value = 10

def showValue():
    print(my_value)

showValue()
"""

#Global constant
#Create global constant
"""
CONTRIBUTION_RATE = 0.05

def main():
    grossPay = float(input("Enter the gross pay: "))
    bonus = float(input("Enter the amount of bonuses: "))
    show_pay_contrib(grossPay)
    show_bonus_contrib(bonus)

def show_pay_contrib(gross):
    contrib = gross * CONTRIBUTION_RATE
    print("Contribution for gross pay: $", format(contrib, ",.2f"),sep="")

def show_bonus_contrib(bonus):
    contrib = bonus * CONTRIBUTION_RATE
    print("Contribution for bonuses: $", format(contrib, ",.2f"), sep="")

main()
"""



