#If statement

#Get the first, second, and third score
#Calculate the average 
#Display the average
#If the average is greater than 95, congratulate the user

score1 = float(input("Enter the score for test 1: "))
score2 = float(input("Enter the score for test 2: "))
score3 = float(input("Enter the score for test 3: "))

average = (score1 + score2 + score3) / 3

print("The average score is " + format(average, ".2f"))

if average > 95:
    print("Congratulation!")


#If-else statement

#Get the number of hours worked
#Get the hourly pay rate
#If the employee worked more than 40 hours, calculate and display the gross pay with overtime
#else calculate and display the gross pay as usual

#auto_repair_payroll.py
baseHours = 40
OtRate = 1.5

hoursWorked = float(input("Enter the number of hours worked: "))
payRate = float(input("Enter thr hourly pay rate: "))

if hoursWorked > baseHours:
    overtimeHours = hoursWorked - baseHours
    overtimePay = overtimeHours * payRate * OtRate
    grossPay = baseHours * payRate + overtimePay

else:
    grossPay = baseHours * payRate

print("The gross pay is $", format(grossPay, ",.2f"), sep="")

#Comparing strings
#password.py
password = input("Enter the password: ")

if password == "ABC":
    print("Password accepted.")
else:
    print("Sorry, this is a wrong password.")

#sort_names.py
name1 = input("Enter a name (last name first): ")
name2 = input("Enter another name (last name first): ")

if name1 < name2:
    print(name1)
    print(name2)

else:
    print(name2)
    print(name1)

#if_elseif_else
#grader.py
testScore = float(input("Enter your test score: "))

if testScore >= 90:
    print("Your grade is A")
elif testScore >= 80:
    print("Your grade is B")
elif testScore >= 70:
    print("Your grade is C")
elif testScore >= 60:
    print("Your grade is D")
else:
    print("Your grade is F")



