#Finding Items in List with the in Operator
#Program 1

def main():
    prodNums = ["V492", "K920", "J923", "B238"]

    search = input("Enter a product number: ")

    if search in prodNums:
        print(search, "was found in the list.")
    else:
        print(search, "was not found in the list.")

main()


#Program 2

def main():
    prodNums = ["V492", "K920", "J923", "B238"]

    search = input("Enter a product number: ")

    if search not in prodNums:
        print(search, "was not found in the list.")
    else:
        print(search, "was found in the list.")

main()