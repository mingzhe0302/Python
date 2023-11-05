#An argument is any piece of data that is passed into a function when the function is called. 
#A parameter is a variable that receives an argument that is passed into a function.


#Program (pass_arg.py)
# def main():
#     value = 5
#     showDouble(value)

# def showDouble(number):
#     result = number * 2
#     print(result)


# main()
def main():
    intro()
    cups_needed = int(input("Enter the number of cups: "))
    cups_to_ounces(cups_needed)

#Program (cups_to_ounces.py)
def intro():
    print("This program converts measurements in cups to fluid ounces.")
    print("Four your reference the formula is 1 cup = 8 fluid ounces.")
    print()

def cups_to_ounces(cups):
    ounces = cups * 8
    print("That converts to", ounces, "ounces.")


main()