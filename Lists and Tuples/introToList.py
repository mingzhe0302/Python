#Concept: A List is an object that contains multiple data items. 
#         List are mutable (can change during a program's execution)

even_numbers = [2,4,6,8,10]
names = ["Yeoh", "Soh", "Tan"]

#first argument: starting value
#second argument: ending limit
#third argument: step value
numbers = list(range(1, 10, 2))  #the result is [1, 3, 5, 7, 9]

#The repetition operator
#format: list * n
repeatNum = [2] * 5
print(repeatNum) #result is [2, 2, 2, 2, 2]
repeatNum2 = [1, 2, 3] * 3
print(repeatNum2)  #result is [1, 2, 3, 1, 2, 3, 1, 2, 3]

#Indexing
myList = [10, 20, 30, 40]
print(myList[0], myList[1], myList[2], myList[3])

#or
index = 0
while index < 4:
    print(myList[index])
    index += 1

#also can use negative indexes to identify element positions relative to the end of the list
print(myList[-1], myList[-2], myList[-3], myList[-4])



#The len function
#This is built-in function that return the length of a sequence.
size = len(myList) 
print(size)   #return 4

while index < len(myList):
    print(myList[index])
    index += 1

#Concatenating list
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

list3 = list1 + list2

print(list3)    #result is [1, 2, 3, 4, 5, 6, 7, 8]

#OR

list1 += list2

print(list1)    #result is [1, 2, 3, 4, 5, 6, 7, 8]


boyName = ["Yeoh Ming Zhe"]
girlName = ["Felicia Gan"]

allName = boyName + girlName

print(allName)   #["Yeoh Ming Zhe", "Felicia Gan"]

#OR
boyName += girlName

print(boyName)   #["Yeoh Ming Zhe", "Felicia Gan"]
