#1. Creating a dictionary
phonebook = {
    "Chris": "555-1111",
    "Katie": "555-2222",
    "Joanne": "555-3333"
}

#"Key": values
#Key cannot be list or any immutable object

#2. Retrieving the value from a dictionary
print(phonebook["Chris"])   #555-1111
print(phonebook["Joanne"])  #555-2222
print(phonebook["Katie"])   #555-3333


#3. Use the in and not in operators to test for a value in a dictionary
if "Chris" in phonebook:
    print(phonebook["Chris"])

if "Joanne" not in phonebook:
    print("Joanne is not found.")



#4. Adding elements to an existing dictionary
phonebook["Joe"] = "555-0123"
print(phonebook)

#if the key does not exist, it will be added to the dictionary


#5. Deleting elements
#del dictionary_name[key]
del phonebook["Chris"]
print(phonebook)


#6. getting the number of elements in a dictionary
num_items = len(phonebook)
print(num_items)  #3


#7. Mixing Data Types in a dictionary
testScore = {
    "Kayla": [88, 92, 100], 
    "Luis": [95, 74, 81],
    "Sophie": [72, 88, 91],
    "Ethan": [70, 75, 78]
}

print(testScore["Kayla"])


employee = {

    "name": "Kevin Smith",
    "id": 12345,
    "payRate": 25.75
}


#8. Create an empty dictionary
book = {}


#9. Using the for loop to iterate over a dictionary
for key in phonebook:
    print(key)         #Joanne
                       #Katie
                       #Joe

for key in phonebook:
    print(key, phonebook[key])  #Joanne 555-3333
                                #Katie  555-2222
                                #Joe    555-0123


#10. Some dictionary methods
#clear   phonebook.clear()
#get     phonebook.get("Katie", "Entry not found")  555-2222
#        phonebook.get("Andy", "Entry not found")   Entry not found
#items   phonebook.items()   [("Chris": 555-1111), .......]
#keys    phonebook.keys()    Chris, Joanne, Katie,  returns all the keys
#pop     phonebook.pop("Chris", "Element not found")  
#popitem k, v = dictionary.popitem()   after the statement executes, the key values pair removed from the dictionary
#values  return all the dictionary values(without their keys), phonebook.values()








