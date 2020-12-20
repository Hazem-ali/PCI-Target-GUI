import os
from time import sleep



# Make Time Delay
def Delay(number):
    return '#' + str(number) + '\n'

def txtgen1():
    # you'll make one like this as read & write operations

    txt1 = '''s
MOFTY
X
Y
Z
T
f'''
    return txt1




# function that takes template and write operations in a new file
def Make_Operations(Inputfile, Outputfile, Operations):
    # Opening Template file
    with open(Inputfile, "r") as source:
        lines = source.read().split('\n')  # lines is a list, each elemennt is a line
        print("lines: ", lines)
        
        # Creating a new file
        with open(Outputfile, "w") as target:
            
            # Looking for the flag that we'll mark and write after
            for line in lines:
                if line == "lol":  # Flag found
                    # Replace the flag with required operations
                    line = ''
                    for op in Operations:
                        line += op + '\n'
                # writing data (new or existing)
                target.writelines(line + '\n')





# Useful tools
# sleep(2)
# os.system("copy.txt") ## writing a terminal command
