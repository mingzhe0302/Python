#While loop is a pre test loop

#Program > (commission.py)
keep_going = 'y'
while keep_going == 'y':
    sales = float(input("Enter the amount of sales: "))
    comm_rate = float(input("Enter the commission rate: "))

    commission = sales * comm_rate

    print("The commission is $",\
          format(commission, ".2f"), sep="")
    
    #See if the user wants to do another one.
    keep_going = input("Do you want to calculate another commission (Enter y for yes): ")


#Program > (temperature.py)
max_temp = 102.5

temperature = float(input("Enter the substance's Celsius temperature: "))

while temperature > max_temp:
    print("The temperature is too high.")
    print("Turn the thermostat down and wait 5 minutes.")
    print("Then take the temperature again and enter it.")

    temperature = float(input("Enter the new Celsius temperature: "))

print("The temperature is acceptable. Check it again in 15 minutes.")



