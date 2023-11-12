#Two-Dimensional list
students = [["Yeoh", "Gan"], ["Soh", "Tan"], ["Lee", "Cha"]]

#           Column 0        Column 1
#  Row 0    "Yeoh"            "Gan"
#  Row 1    "Soh"             "Tan"
#  Row 2    "Lee"             "Cha"

#This program assings random numbers to a two-dimensional list
#random_numbers.py
import random

ROWS = 4
COLS = 4

def main():
    values = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]
    
    for r in range(ROWS):
        for c in range(COLS):
            values[r][c] = random.randint(1, 100)

    print(values)



