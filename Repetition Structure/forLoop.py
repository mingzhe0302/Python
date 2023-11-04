#A count-controlled loop iterates a specific numbe of times.

#Program (simpleLoop.py)
print("I will display the number 1 through 5.")
for num in [1,2,3,4,5]:
    print(num, end=" ")




#Program (simpleLoop.py)
for x in range(5):
    print("Hello world")



#Using the target variable inside the loop
print("Number\tSquare")
print("--------------")
for number in range(1, 11):
    square = number**2
    print(number, "\t", square)



#Program (speed_converter.py)
startSpeed = 60
end_speed = 131
increment = 10
conversion_factor = 0.6214

print("KPH\tMPH")
print("------------")

#Print the speeds. 
for kph in range(startSpeed, end_speed, increment):
    mph = kph * conversion_factor
    print(kph, "\t", format(mph, ".1f"))


#Sum numbers.py
max = 5
total = 0.0
print("This program calculates the sum of max, numbers you will enter.")

for counter in range(max):
    number = int(input("Enter a number: "))
    total = total + number

print("The total is", total)







