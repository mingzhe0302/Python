#1. File Display
"""
def main():

    numberFile = open("numbers.txt", "r")

    fileContent = numberFile.read()

    numberFile.close()

    print(fileContent)

main()
"""


#2. File Head Display
"""
def main():
    askForFile = input("Enter a filename: ")

    try:
        with open(askForFile, "r") as fp:
            lines = fp.readlines()

            if len(lines) < 5:
                print("File Contents:")
                print("".join(lines))    #is the string method, which is used to concatenate the elements of a list of strings into a single string.
            else:
                print("First five lines of the file:")
                for i in range(5):
                    print(lines[i])
    except FileNotFoundError:
        print(f"File '{askForFile}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

main()
"""


#3. Line Numbers
"""
def main():

    filename = input("Enter the filename: ")

    fp = open(filename, "r")

    line = fp.readline()

    lineNumber = 1

    while line != "":
        print(str(lineNumber) + ": ", line.strip("\n"))  #Remove line breaks at the beginning and end (\n)
        line = fp.readline()
        lineNumber += 1
    
    fp.close()

main()
"""

#4. Item Counter
"""
def main():

    fp = open("names.txt", "r")

    record = 0

    line = fp.readline()

    while line != "":
        line = fp.readline()
        record += 1

    print("There are", record, "numbers of names stored in the file.")

    fp.close()
main()
"""



#5. Sum of Numbers
"""
def main():

    fp = open("numbers.txt", "r")

    total = 0

    for line in fp:

        total += int(line)


    print("The total is", format(total, ".2f"))

    fp.close()

main()
"""



#6. Average of the numbers
"""
def main():

    fp = open("numbers.txt", "r")

    total = 0
    count = 0

    for line in fp:

        total += int(line)
        count += 1
    
    average = total / count

    print("The total is", format(average, ".2f"))

    fp.close()

main()
"""


#7. Random Number File Writer
"""
import random

def main():

    fp = open("random.txt", "w")

    hold = int(input("Enter a numbers of file wants to hold: "))

    for x in range(hold):
        randomNum = random.randint(1, 500)
        fp.write(str(randomNum) + "\n")

    print("The numbers written to the file.")

    fp.close()

main()
"""

#8. Random Number File Reader
"""
def main():

    fp = open("random.txt", "r")

    total = 0
    count = 0

    for x in fp:
        total += int(x)
        count += 1

    print("The total of random numbers is", total)
    print("The number of random numbers read from the file:", count)

    fp.close()

main()
"""


#9. Exception Handing
"""
def main():

    try: 
        fp = open("numbers.txt", "r")

        total = 0
        count = 0

        for line in fp:

            total += int(line)
            count += 1
        
        average = total / count

        print("The total is", format(average, ".2f"))

        fp.close()

    except IOError:
        print("This code caused an IOError.")
    except ValueError:
        print("Please enter a correct value.")


main()
"""


#10. Golf scores
"""
def getPlayerName():
    playerName = input("Enter the player name: ")
    return playerName

def getPlayerScore(playerName):
    playerScore = input("Enter a player score of " + playerName + ": ")
    return playerScore


def main():

    fp = open("golf.txt", "w")

    anotherRecord = "y"

    while anotherRecord == "y" or anotherRecord == "Y":
        playerName = getPlayerName()
        playerScore = getPlayerScore(playerName)

        fp.write(playerName + "\n" + playerScore + "\n")

        anotherRecord = input("Do you want to add another record? [Y = yes, N = no] ")

    fp.close()


    fp = open("golf.txt", "r")

    playerName = fp.readline().rstrip("\n")

    while playerName != "":
        playerScore = float(fp.readline().rstrip("\n"))

        print(playerName, "scored", playerScore, "points")

        playerName = fp.readline().rstrip("\n")

    fp.close()

main()
"""