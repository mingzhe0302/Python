#In Python, the code you've provided for the courses dictionary has an issue. 
#Dictionaries cannot have duplicate keys. 
#Instead, you can use a list of dictionaries to represent each course. 
#Here's the corrected code:

#1. Course Information
def main():
    courses = {
        "CS101": 3004,
        "CS102": 4501,
        "CS103": 6755,
        "NT110": 1244,
        "CM241": 1411
    }

    instructor = {
        "CS101": "Haynes",
        "CS102": "Alvarado",
        "CS103": "Rich",
        "NT110": "Burke",
        "CM241": "Lee"
    }

    meetingTime = {
        "CS101": "8:00a.m.",
        "CS102": "9:00a.m.",
        "CS103": "10:00a.m.",
        "NT110": "11:00p.m.",
        "CM241": "1.00p.m."
    }


    courseNum = input("Enter your course number to show the course informations: ")

    if courseNum in courses:
        print("Course Informations for", courseNum)
        print("Room Number:", courses[courseNum])
        print("Instructor:", instructor[courseNum])
        print("Meeting time:", meetingTime[courseNum])
    else:
        print("No record for course number:", courseNum)


#
#
#

#2. Capital Quiz
import random

MIN = 0
MAX = 49

def main():

    US = {

    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinois': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Moines',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'St. Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Nevada': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhode Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakota': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'
    }

    stateList = list(US)

    again = 'y'
    correct = 0
    incorrect = 0

    while again == 'y':

        randomNum = random.randint(MIN, MAX)
        state = stateList[randomNum]

        print("The random US state is",state)
        capital = input("Enter the capital of " + state + ": ")

        if capital == US[state]:
            correct += 1
            print("correct.")
            again = input("Enter y to play again, anything else to stop: ")

        else:
            incorrect += 1
            print("Incorrect.")
            again = input("Enter y to play again, anything else to stop: ")

    print("\nYou have", correct,"correct answers")
    print("\nYou have", incorrect, "incorrect answers")


#
#
#


#3. File Encryption and Decryption
# encryption_library = {'A':'!','B':'@','C':'#','D':'$','E':'%','F':'^','G':'&','H':'*','I':'(',
#                       'J':')','K':'-','L':'_','M':'+','N':'=','O':'`','P':'~','Q':'{','R':'[',
#                       'S':'}','T':']','U':':','V':';','W':'"','X':'<','Y':'>','Z':'0','a':'1',
#                       'b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8','i':'9','j':'a',
#                       'k':'b','l':'c','m':'d','n':'e','o':'f','p':'g','q':'h','r':'i','s':'j',
#                       't':'k','u':'l','v':'m','w':'n','x':'o','y':'p','z':'q'}

# decryption_library = {'!':'A','@':'B','#':'C','$':'D','%':'E','^':'F','&':'G','*':'H','(':'I',
#                       ')':'J','-':'K','_':'L','+':'M','=':'N','`':'O','~':'P','{':'Q','[':'R',
#                       '}':'S',']':'T',':':'U',';':'V','"':'W','<':'X','>':'Y','0':'Z','1':'a',
#                       '2':'b','3':'c','4':'d','5':'e','6':'f','7':'g','8':'h','9':'i','a':'j',
#                       'b':'k','c':'l','d':'m','e':'n','f':'o','g':'p','h':'q','i':'r','j':'s',
#                       'k':'t','l':'u','m':'v','n':'w','o':'x','p':'y','q':'z'}

# def main():
    
#     currentFile = "cities.txt"
#     newFile = "encrypCode.txt"
#     encryptionCode(currentFile, newFile)
#     decryptionCode(newFile)

# def encryptionCode(citiesFile, newFile):

#     oldFile = open(citiesFile, "r")
#     text = oldFile.read()
#     oldFile.close()

#     newFile = open(newFile, "w")

#     for char in text:
#         if char in encryption_library:
#             newFile.write(encryption_library[char])
#         else:
#             newFile.write(char)

#     newFile.close()

#     oldFile = open(citiesFile, "r")
#     text = oldFile.read()
#     oldFile.close()
#     codesItem = encryption_library.items()

#     for char in text:
#         if not char in encryption_library.values() or char == "," or char == "." or \
#         char == "!":
#             print(char)
#         else:
#             for k, v in codesItem:
#                 if char == v and char != ".":
#                     print(k, end="")

# def decryptionCode(newFile):

#     newsFile = open(newFile, "r")

#     text = newsFile.read()

#     newsFile.close()

#     decrypFile = open("decryptionFile.txt", "w")

#     for ch in text:
#         if ch in decryption_library:
#             decrypFile.write(decryption_library[ch])

#         else:
#             decrypFile.write(ch)

#     decrypFile.close()

#     newsFile = open(newFile, "r")

#     text = newsFile.read()

#     newsFile.close()

#     codesItem = decryption_library.items()

#     for ch in text:
#         if not ch in decryption_library or ch == "," or ch == "." or \
#         ch == "!":
#             print(ch)

#         else:
#             for k, v in codesItem:
#                 if ch == 'v' and ch != '.':
#                     print(k, end="")


# #
# #
# #
# encryption_library = {'A':'!','B':'@','C':'#','D':'$','E':'%','F':'^','G':'&','H':'*','I':'(',
#                       'J':')','K':'-','L':'_','M':'+','N':'=','O':'`','P':'~','Q':'{','R':'[',
#                       'S':'}','T':']','U':':','V':';','W':'"','X':'<','Y':'>','Z':'0','a':'1',
#                       'b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8','i':'9','j':'a',
#                       'k':'b','l':'c','m':'d','n':'e','o':'f','p':'g','q':'h','r':'i','s':'j',
#                       't':'k','u':'l','v':'m','w':'n','x':'o','y':'p','z':'q'}

# orig_file = open('Plain_Text_File.txt','r')
# file_read = orig_file.read()    
# orig_file.close()
# encrypt_file = open('ENCRYPTED_Plain_Text_File.txt','w')

# for ch in file_read:
#     if ch in encryption_library:
#         encrypt_file.write(encryption_library[ch])
#     else:
#         encrypt_file.write(ch)

# encrypt_file.close()
# encrypt_file = open('Plain_Text_File.txt','r')
# file_read = encrypt_file.read()
# encrypt_file.close()
# codes_items = encryption_library.items()

# for ch in file_read:
#     if not ch in encryption_library.values() or ch == '.' or ch == ',' or ch == '!':
#         print(ch)
#     else:
#         for k,v in codes_items:
#             if ch == v and ch != '.':
#                 print(k,end='')


#4. Unique Words
def main():
    textFile = open("cities.txt", "r")

    fileRead = textFile.read()

    #split the content into words using space as the delimiter
    wordList = fileRead.split()

    uniqueWords = set(wordList)

    for word in uniqueWords:
        print(word)



#5. Word Frequency
def read():
    file = input('Enter a file name with its extension: ')    
    object_file = open(file, 'r')
    return object_file

def count(object_file):
    word_frequency = {}
    for line in object_file:
        words = line.split()
        for word in words:
            word = word.lower()
            if word not in word_frequency:
                word_frequency[word] = 1
            else:
                word_frequency[word] += 1 

    print(word_frequency)

def main():
    object_file = read()
    count(object_file)


#6. File Analysis
def read():

    textFile1 = input("Enter a file name with its extension: ")
    textFile2 = input("Enter another file name with its extension: ")

    objectFile1 = open(textFile1, "r")
    objectFile2 = open(textFile2, "r")

    words1 = []
    words2 = []


    for line in objectFile1:
        words1 += line.split()
    for line in objectFile2:
        words2 += line.split()

    wordList = words1 + words2

    print("Combined list of words from both files:",wordList)

    wordsSet = set(wordList)

    print("Set of unique words from both files:",wordsSet)

    words1_set = set(words1)
    words2_set = set(words2)

    print("A list of the words that appear in both files:", words1_set & words2_set)
    print("A list of the words that appear in the first file but not the second:", words1_set - words2_set)
    print("A list of the words that appear in the second file but not the first:", words2_set - words1_set)
    print("A list of the words appear in either the first or second file but not both:", words1_set | words2_set)




#7. Name and Email Addresses
import pickle

def loadUserDict():
    try:
        with open('user_dict.pkl', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return {}

def saveUserDict(userDict):
    with open('user_dict.pkl', 'wb') as file:
        pickle.dump(userDict, file)

def userMenu():
    userDict = loadUserDict()
    again = False

    print("1. Add name and email address\n"\
          "2. Modify email address\n"\
          "3. Delete name and email address\n")

    while not again:
        choice = int(input("Enter a choice: "))

        if choice == 1:
            addInfo(userDict)

        elif choice == 2:
            modifyInfo(userDict)

        elif choice == 3:
            deleteInfo(userDict)

        else:
            print("Invalid input\n"\
                "Please enter again: ")
            again = input()
            return False

    saveUserDict(userDict)

def addInfo(userDict):
    name = input("Enter a name: ")
    email = input("Enter the email address: ")
    userDict[name] = email
    print(f"Information added for {name} with email {email}")

def modifyInfo(userDict):
    name = input("Enter the name to modify: ")
    if name in userDict:
        new_email = input("Enter the new email address: ")
        userDict[name] = new_email
        print(f"Email address modified for {name}")
    else:
        print(f"{name} not found in the user dictionary")

def deleteInfo(userDict):
    name = input("Enter the name to delete: ")
    if name in userDict:
        del userDict[name]
        print(f"{name}'s information deleted")
    else:
        print(f"{name} not found in the user dictionary")

# Example usage
# userMenu()


#8. BlackJack Simulation
import random

def deal_card():
    """Return a random card from the deck."""
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
    return random.choice(cards)

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards."""
    # Check for blackjack (an Ace and a 10-value card)
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack
    # Convert Ace from 11 to 1 if the score is over 21
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(player_score, opponent_score):
    """Compare the scores of the player and opponent."""
    if player_score > 21 and opponent_score > 21:
        return "You went over. You lose!"
    if player_score == opponent_score:
        return "It's a draw!"
    elif opponent_score == 0:
        return "Opponent has Blackjack. You lose!"
    elif player_score == 0:
        return "You have Blackjack. You win!"
    elif player_score > 21:
        return "You went over. You lose!"
    elif opponent_score > 21:
        return "Opponent went over. You win!"
    elif player_score > opponent_score:
        return "You win!"
    else:
        return "You lose!"

def play_game():
    player_cards = []
    opponent_cards = []
    game_over = False

    for _ in range(2):
        player_cards.append(deal_card())
        opponent_cards.append(deal_card())

    while not game_over:
        player_score = calculate_score(player_cards)
        opponent_score = calculate_score(opponent_cards)

        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Opponent's first card: {opponent_cards[0]}")

        if player_score == 0 or opponent_score == 0 or player_score > 21:
            game_over = True
        else:
            another_card = input("Type 'y' to get another card, 'n' to pass: ")
            if another_card == 'y':
                player_cards.append(deal_card())
            else:
                game_over = True

    while opponent_score != 0 and opponent_score < 17:
        opponent_cards.append(deal_card())
        opponent_score = calculate_score(opponent_cards)

    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Opponent's final hand: {opponent_cards}, final score: {opponent_score}")
    print(compare(player_score, opponent_score))

# Run the game
play_game()


