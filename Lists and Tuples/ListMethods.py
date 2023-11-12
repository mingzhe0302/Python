#List methods and useful built-in method
#1. append(item)
#2. index(item)
#3. insert(index, item)
#4. sort()
#5. remove(item)
#6. reverse()
#7. del
#8. min/max



#Index method
def main():
    food = ["Pizza", "Burgers", "Chips"]

    print("Here are the items in the food list:")
    print(food)

    item = input("Which item should I change? ")

    try:
        item_index = food.index(item)   #Get the item index in the list

        newItem = input("Enter the new value: ")

        food[item_index] = newItem

        print("Here is the revised list: ")
        print(food)

    except ValueError:
        print("That item was not found in the list.")

main()


#The del statement
myList = [1, 2, 3, 4, 5]
print("Before deletion: ", myList)

del myList[2]

print("After deletion: ", myList)