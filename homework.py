import math
import sys

# variable for student number
stuNum = None
# get student number input from user and validate
# loop until input is an int, 8 digits in length
while True:
    stuNum = input("Give me a valid student number (X to exit): ")
    # exit the application
    if stuNum.upper() == "X":
        print("Goodbye")
        sys.exit()
    # meets the conditions - break out of loop
    elif stuNum.isdigit() == True and len(stuNum) == 8:
        break
    # enform user of invalid input before looping# meets the conditions
    else:
        print("Invalid input")

# variable for percentage (can be represented as decimal)
percent = 0.1
# change percentage value added to subnet
# loop until user inputs Y or N
while True:
    changePercent = input("10% will be added to the subnet, would you like to change this value? (Y/N): ")
    # if user enters Y, prompt to change percentage value before breaking out of loop
    if changePercent.upper() == 'Y':
        # loop until unser gives a valid percentage value
        while True:
            newPercent = input("Enter the new percentage value (between 0 and 100): ")
            # if value is an int and between 0 and 100, change value of percent and breakout of loop
            if newPercent.isdigit() and 0 <= int(newPercent) <= 100:
                percent = int(newPercent) / 100
                break
            else:
                print("Invalid input. Please enter a valid number.")
        # having entered a valid percentage, break out of first loop
        break
    # if user enters N, break out of the loop
    elif changePercent.upper() == 'N':
        print("10% will be used")
        break
    # anything other than N or Y will loop again
    else:
        print("Invalid response, please enter 'Y' for yes or 'N' for no.")

# lists with default range values
hrRange = [0, 2]
salesRange = [0, 3]
markeRange = [1, 3]
managRange = [2, 5]
adminRange = [4, 6]
rdRange = [5, 8]
# tuple that will be looped through - links to department range values above
departments = (
    ("HR", hrRange),
    ("Sales", salesRange),
    ("Marketing", markeRange),
    ("Management", managRange),
    ("Administration", adminRange),
    ("R&D", rdRange)
)
# loop to get valid Y/N response from user regarding setting ranges
while True:
    changeRanges = input("Would you like to define the ranges for each department? (Y/N): ")
    # if user enters Y, prompt to change percentage range values before breaking out of loop
    if changeRanges.upper() == 'Y':
        # loop for each department in the departments tuple
        for department, departmentRange in departments:
            # loop until unser gives a valid starting range value
            while True:
                startRange = input(f"Enter the starting range for {department} [0-7]: ")
                if startRange.isdigit() and 0 <= int(startRange) <= 7:
                    departmentRange[0] = int(startRange)
                    break
                else:
                    print("Invalid input. Please enter a number between 0 and 7.")
            # loop until unser gives a valid ending range value
            while True:
                endRange = input(f"Enter the ending range for {department} [{int(startRange) + 1}-8]: ")
                if endRange.isdigit() and int(startRange) + 1 <= int(endRange) <= 8:
                    departmentRange[1] = int(endRange)
                    break
                else:
                    print(f"Invalid input. Please enter a number between {int(startRange) + 1} and 8.")    
        # having entered a valid ranges, break out of first loop
        break
    # if user enters N, break out of the loop
    elif changeRanges.upper() == 'N':
        print("Default ranges will be used")
        break 
    # anything other than N or Y will loop again
    else:
        print("Invalid response, please enter 'Y' for yes or 'N' for no.")

# 01234567
# xyzrstuv 
# split student number into departments for subnetting - convert to int
hr = int(stuNum[hrRange[0]:hrRange[1]])
# hr = int(stuNum[0:2])
sales = int(stuNum[salesRange[0]:salesRange[1]])
marke = int(stuNum[markeRange[0]:markeRange[1]])
manag = int(stuNum[managRange[0]:managRange[1]])
admin = int(stuNum[adminRange[0]:adminRange[1]])
rd = int(stuNum[rdRange[0]:rdRange[1]])

# add 10% to the values, round up, make whole number, and output
print(f"HR department         | {hr} + {int(percent * 100)}% = {int(math.ceil(hr + (hr * percent)))}")
# print("HR department         | ", hr, "+", int(percent * 100), "% =", int(math.ceil(hr + (hr * percent))))
print(f"Sales department      | {sales} + {int(percent * 100)}% = {int(math.ceil(sales + (sales * percent)))}")
print(f"Marketing department  | {marke} + {int(percent * 100)}% = {int(math.ceil(marke + (marke * percent)))}")
print(f"Management department | {manag} + {int(percent * 100)}% = {int(math.ceil(manag + (manag * percent)))}")
print(f"Admin department      | {admin} + {int(percent * 100)}% = {int(math.ceil(admin + (admin * percent)))}")
print(f"R&D department        | {rd} + {int(percent * 100)}% = {int(math.ceil(rd + (rd * percent)))}")
