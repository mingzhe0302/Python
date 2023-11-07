#Opening a file
#general format: 
#       file_variable = open(filename, mode)
#mode:
#   1. 'r' = read only
#   2. 'w' = writing, if file exists, erase its contents. If it does not exist, create it.
#   3. 'a' = writing, all the data written to the file will be appended to its end. If the file
#            does not exist, create it.


#1. opening file
# customer_file = open("customer.txt", "w")
# customer_file = open("customer.txt", "r")


#2. writing data to the file
"""
def main():
    outfile = open("philosphers.txt", "w")

    outfile.write("John Locke\n")
    outfile.write("David Hume\n")
    outfile.write("Edmund Burke\n")

    outfile.close()

main()
"""

#3. Read data from a file
"""
def main():
    infile = open("philosphers.txt", "r")

    file_contents = infile.read()

    infile.close()

    print(file_contents)

main()
"""


#4. Reads the contents one lines at a time
"""
def main():
    infile = open("philosphers.txt", "r")

    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()

    infile.close()

    print(line1)
    print(line2)
    print(line3)

main()
"""


#5. Concatenating a Newline to a String
"""
def main():
    print("Enter the names of the three friends.")
    name1 = input("Friend #1: ")
    name2 = input("Friend #2: ")
    name3 = input("Friend #3: ")

    myFile = open("friends.txt", "w")

    myFile.write(name1 + "\n")
    myFile.write(name2 + "\n")
    myFile.write(name3 + "\n")

    myFile.close()
    print("The names were written to friends.txt.")

main()
"""


#6. Reading a String and Stripping the Newline from it
#use rstrip("\n") method
#As a result, the extra blank lines do not appear in the output

"""
def main():
    infile = open("philosophers.txt", "r")

    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()

    line1 = line1.rstrip("\n")
    line2 = line2.rstrip("\n")
    line3 = line3.rstrip("\n")

    infile.close()

    print(line1)
    print(line2)
    print(line3)

main()
"""


#Writing and Reading Numeric Data
#number must be converted to strings before they are written to a text file
"""
def main():
    outfile = open("numbers.txt", "w")

    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    num3 = int(input("Enter another number: "))

    outfile.write(str(num1) + "\n")
    outfile.write(str(num2) + "\n")
    outfile.write(str(num3) + "\n")

    outfile.close()
    print("Data written to numbers.txt")

main()
"""



#Numbers that are read from a file must be converted from strings before they are used in a math operation.
"""
def main():
    infile = open("numbers.txt", "r")

    num1 = int(infile.readline())
    num2 = int(infile.readline())
    num3 = int(infile.readline())

    infile.close()

    total = num1 + num2 + num3

    print("The numbers are: ", num1, num2, num3)
    print("Their total is: ", total)

main()
"""




