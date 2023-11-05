#Design a program to use functions
#Program (acme_dryer.py)
def main():
    startup_message()
    input("Press enter to see step 1.")
    step1()
    input("Press enter to see step 2.")
    step2()
    input("Press enter to see step 3.")
    step3()
    input("Press enter to see step 4.")
    step4()



def startup_message():
    print("This programs tell you how to disassemble an ACME laundry dryer."\
          "There are 4 steps in the process.")
    print()



def step1():
    print("Step 1: Unplug the dryer and move it away from the wall.")
    print()


def step2():
    print("Step 2: Remove the six screws from the back of the dryer.")
    print()

def step3():
    print("Step 3: Remove the back panel from the dryer.")
    print()

def step4():
    print("Step 4: Pull the top of the dryer straight up.")


main()