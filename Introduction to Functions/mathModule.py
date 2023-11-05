import math
#1. square root

"""
def main():
    number = float(input("Enter a number: "))
    squareRoot = math.sqrt(number)
    print("The square root of", number, "is", squareRoot)

main()

"""



#2. hypotenuse.py
def main():
    a = float(input("Enter the length of side A: "))
    b = float(input("Enter the length of side B: "))

    c = math.hypot(a,b)

    print("The length of the hypotenuse is",format(c,".2f"), sep=" ")

main()




