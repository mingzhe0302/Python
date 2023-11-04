#A loop that is inside another loop is called a nested loop.

#Program (test_score_averages.py)
numStudents = int(input("How many students do you have? "))

numTestScores = int(input("How many test scores per student? "))

for student in range(numStudents):
    total = 0.0
    print("Student number", student + 1)
    print("----------------")
    for testNum in range(numTestScores):
        print("Test number", testNum + 1, end="")
        score = float(input(": "))
        #Add the score to the accumulator.
        total += score

    
    #Calculate the average test score for this student.
    average = total / numTestScores


    #Display the average 
    print("The average for student number", student + 1,\
          "is: ", average)
    
    print()


#Using nested loops for print patterns
for row in range(8):
    for col in range(6):
        print("*", end="")
    print()


#Program (triangle_pattern.py)
base_size = 8

for r in range(base_size):
    for c in range(r + 1):
        print("*", end="")
    print()


