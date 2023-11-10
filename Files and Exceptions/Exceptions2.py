#2. Gross_pay.py
def main():
    hours = int(input("How many hours did you work? "))

    payRate = float(input("Enter your hourly pay rate: "))

    gross_pay = hours * payRate

    print("Gross pay: $", format(gross_pay, ",.2f"), sep="")

main()
#if user enter fourty instead of 40, an exception will occured

#2.1 Gross_pay.py
def main():
    
    try:
        hours = int(input("How many hours did you work? "))

        payRate = float(input("Enter your hourly pay rate: "))

        gross_pay = hours * payRate

        print("Gross pay: $", format(gross_pay, ",.2f"), sep="")
    
    except ValueError:
        print("Error: Hours worked and hourly pay rate must be valid numbers.")

main()