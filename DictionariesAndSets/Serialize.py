#Serialize objects
import pickle

phonebook = {
    "Chris": "555-1111",
    "Katie": "555-2222",
    "Joanne": "555-3333"
}

outputFile = open("phonebook.dat", "wb")
pickle.dump(phonebook, outputFile)
outputFile.close()


#retrive an object from the file and unpickle it
inputFile = open("phonebook.dat", "rb")
pb = pickle.load(inputFile)
print(pb)
inputFile.close()


#Sample code1
#pickel_objects.py
def main():
    again = "y"

    fp = open("info.dat", "wb")
    
    while again.lower() == "y":
        saveData(fp)

        again = input("Enter more data? (y/n): ")

    fp.close()

def saveData(file):

    person = {}

    person["name"] = input("Name: ")
    person["age"] = int(input("Age: "))
    person["weight"] = float(input("Weight: "))

    pickle.dump(person, file)


#Sample code2
#Unpickle_objects.py
def main():
    endOfFile = False

    fp = open("info.dat", "rb")

    while not endOfFile:
        try:
            person = pickle.load(fp)
            displayData(person)
        except EOFError:
            endOfFile = True
        
    fp.close()

def displayData(person):
    print("Name: ", person["name"])
    print("Age: ", person["age"])
    print("Weight: ", person["weight"])
    print()


