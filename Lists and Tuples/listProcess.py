#Processing Lists
#1. 
NUM_EMPLOYEES = 6

def main():
    hours = [0] * NUM_EMPLOYEES

    for index in range(NUM_EMPLOYEES):
        print("Enter the hours worked by employee", index + 1, ": ", sep="", end="")

        hours[index] = float(input())

    payRate = float(input("Enter the hourly pay rate: "))

    for index in range(NUM_EMPLOYEES):
        grossPay = hours[index] * payRate
        print("Gross Pay for employee", index + 1, ": $", format(grossPay, ",.2f"), sep="")

    


#2. Totaling the values in a list
def main():
    numbers = [2, 4, 6, 8, 10]

    total = 0

    for value in numbers:
        total += value

    print("The total of the elements is", total)



#3. Average value in a list
def main():
    scores = [2.5, 7.3, 6.5, 4.0, 5.2]

    total = 0

    for value in scores:
        total += value

    average = total / len(scores)

    print("The average of the score is", average)



#4. Passing a list as an argument to a function
def main():
    numbers = [2, 4, 6, 8, 10]

    print("The toal is", getTotal(numbers))

def getTotal(valueList):
    total = 0

    for value in valueList:
        total += value

    return total


#5. Returning a List from the function
def main():
    numbers = getValues()

    print("The numbers in the list are: ")
    print(numbers)

def getValues():
    values = []

    again = "y"

    while again == "y":
        num = int(input("Enter a number: "))
        values.append(num)

        print("Do you want to add another number? ")
        again = input("y = yes, anything else = no: ")
        print()

    return values



#Working with list and file
def main():
    cities = ["New York", "Boston", "Atlanta", "Dallas"]

    outfile = open("cities.txt", "w")

    outfile.writelines(cities)

    outfile.close()

#OR
def main():
    cities = ["New York", "Boston", "Atlanta", "Dallas"]

    outfile = open("cities.txt", "w")

    for item in cities:
        outfile.write(item + "\n")
    

    outfile.close()


#Read list from file
def main():

    infile = open("cities.txt", "r")

    cities = infile.readlines()

    infile.close()

    index = 0

    while index < len(cities):
        cities[index] = cities[index].rstrip("\n")
        index += 1

    print(cities)




