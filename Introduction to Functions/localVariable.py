#This program demonsratestwo functions that have local variables with the same name.

def main():
    texas()
    california()



def texas():
    birds = 5000
    print("texas has", birds, "birds.")



def california():
    birds = 8000
    print("california has", birds, "birds.")


main()