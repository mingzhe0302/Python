#Processing records
#This program gets employee data from the user and saves it as records in the employee.txt file.

"""
def main():
    numOFEmp = int(input("How many employee records do you want to create > "))

    empFile = open("Employee.txt", "w")

    for count in range(1, numOFEmp + 1):
        print("Enter the data for employee #", count, sep="")
        name = input("Name: ")
        idNum = input("ID number: ")
        dept = input("Department: ")

        #write the data as a record to the file
        empFile.write(name + "\n")
        empFile.write(idNum + "\n")
        empFile.write(dept + "\n")

        print()

    empFile.close()
    print("Employee records written to employees.txt.")

main()
"""


#Add and displaying records
"""
def main():
    another = 'y'

    empFile = open("Employee.txt", "a")

    while another == 'y' or another == 'Y':
        print("Enter the following employee records: ")
        name = input("Name: ")
        idNum = input("ID number: ")
        dept = input("Department: ")

        empFile.write(name + "\n")
        empFile.write(idNum + "\n")
        empFile.write(dept + "\n")

        print("Do you want to add another record? ")
        another = input("Y = yes, anything else = no: ")

    empFile.close()
    print("Data appended to Employee.txt.")

main()
"""


#Searching records
"""
def main():
    search = input("Enter a description to search for: ").strip()
    found = False

    try:
        with open("coffee.txt", "r") as coffeeFile:
            for record in coffeeFile:
                description = record.strip()
                qty = coffeeFile.readline().strip()
                
                if description.lower() == search.lower():   #converts all the characters in the string to lowercase.
                    print(f"Description: {description}")    #perform a case-insensitive comparison
                    print(f"Quantity: {qty}")
                    print()
                    found = True
                    break  # if you want to stop at the first match, otherwise remove this line

    except FileNotFoundError:
        print("The file coffee.txt was not found.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    if not found:
        print("That item was not found in the file.")

main()

"""


#Modifying Record
    
