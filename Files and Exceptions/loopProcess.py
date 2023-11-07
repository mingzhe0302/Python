#Using loops to process files
#This program prompts the user for sales amounts and writes those amounts to the sales.txt file.
"""
def main():
    num_days = int(input("For how many days do you have sales? "))

    sales_file = open("sales.txt", "w")

    for count in range(1, num_days + 1):
        sales = float(input("Enter the sales for day #" + str(count) + ": "))

        sales_file.write(str(sales) + "\n")
    
    sales_file.close()
    print("Data written to sales.txt.")

main()
"""


#Read a file with a loop and detecting the end of the file
"""
def main():
    sales_file = open("sales.txt", "r")

    line = sales_file.readline()

    while line != "":
        amount = float(line)
        print(format(amount, ".2f"))
        line = sales_file.readline()
    
    sales_file.close()

main()
"""


#Use for loop to read line
"""
def main():
    sales_file = open("sales.txt", "r")
    for line in sales_file:
        amount = float(line)
        print(format(amount, ",.2f"))
    
    sales_file.close()

main()
"""



#Exercise: working with files
#save_running_times.py
"""
def main():
    numOfVideos = int(input("How many videos are in the project: "))

    videoFile = open("videoTimes.txt", "w")

    print("Enter the running times for each video (in seconds): ")
    for count in range(1, numOfVideos + 1):
        runTime = float(input("Video #" + str(count) + ": "))
        videoFile.write(str(runTime) + "\n")

    videoFile.close()
    print("The times have been saved to videoTimes.txt.")

main()

"""




#read_running_times.py
"""
def main():
    videoFile = open("videoTimes.txt", "r")

    total = 0.0
    count = 0

    print("Here are the running times for each video: ")

    for line in videoFile: 
        runTime = float(line)
        count += 1
        print("Video #", count, ": ", runTime, sep="")

        total += runTime
    
    videoFile.close()

    print("The total running time is", total, "seconds.")

main()

"""






