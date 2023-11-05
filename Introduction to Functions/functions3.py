#Generating random number
import random     #library

"""
def main():
    #Get a random number
    number = random.randint(1, 10)
    print("The number is", number, sep=" ")

main()
"""

"""
def main():
    for count in range(5):
        print(random.randint(1,100))

main()
"""

#Dice.py
"""
MIN = 1
MAX = 6

def main():
    #Create a variable to control the loop.
    again = 'y'

    #Simulate rolling the dice.
    while again == 'y' or again == 'Y':
        print("Rolling the dice...")
        print("Their values are: ")
        print(random.randint(MIN, MAX))
        print(random.randint(MIN, MAX))

        again = input("Roll them again? (y = yes): ")

main()
"""


#Using random number to represent other values
#coin_toss.py
"""
HEADS = 1
TAILS = 2
TOSSES = 10

def main():
    for toss in range(TOSSES):
        if random.randint(HEADS, TAILS) == HEADS:
            print("Heads")
        else:
            print("Tails")

main()

"""


