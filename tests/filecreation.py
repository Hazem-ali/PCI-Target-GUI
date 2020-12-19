import os
from time import sleep

def copyfile(inputfile, outputfile):
    with open(inputfile, "r") as data:
        with open(outputfile, "w") as target:
            for line in data:
                target.write(line)

# String to add in (READ, WRITE ..etc operations)
txt = '''MOFTY
X
Y
Z
T'''

# function that takes template and write operations in a new file
def Make_Operations(inputfile, outputfile, operations):
    with open("copy.v", "r") as source:
        lines = source.read().split('\n')
        print("lines: ", lines)
        with open("copy.txt", "w") as target:
            for line in lines:
                if line == "lol": # flag to replace and write after
                    line = txt # replacement
                wr = target.writelines(line + '\n') # writing data (new or existing)
    
 
# Useful tools    
# sleep(2)
# os.system("copy.txt") ## writing a terminal command
