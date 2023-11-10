#An exception is an error that occurs while a program is running, causing the program to abruptly halt.
#You can use the >>> try/except  <<< statement to gracefully handle exceptions.

#1. division.py 
def main():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    result = num1 / num2

    print(num1, "divided by", num2, "is", result)

main()


#if the user enter 0 in num2, it will causes an exception because it is mathematically impossible.
#1.2 division.py
def main():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    if num2 != 0:
        result = num1 / num2
        print(num1, "divided by", num2, "is", result)
    else:
        print("Cannot divided by zero.")
        
main()
