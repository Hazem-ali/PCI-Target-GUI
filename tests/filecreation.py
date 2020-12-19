import os
from time import sleep


def copyfile(inputfile, outputfile):
    with open(inputfile, "r") as data:
        with open(outputfile, "w") as target:
            for line in data:
                target.write(line)


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


def Make_Operations(inputfile, outputfile, operations):
    # Opening Template file
    with open(inputfile, "r") as source:
        lines = source.read().split('\n') # lines is a list, each is a line
        print("lines: ", lines)
        # Creating a new file 
        with open(outputfile, "w") as target:
            for line in lines:
                # Looking for the flag that we'll mark and write after
                if line == "lol":  # flag to replace and write after 
                    # Replace the flag with required operations 
                    line = ''
                    for op in operations:
                        line += op + '\n'
                # writing data (new or existing)
                target.writelines(line + '\n')



# String to add in (READ, WRITE ..etc operations)
txt1 = '''MOFTY
X
Y
Z
T'''
txt2 = '''Hazem
X
Y
Z
LOL'''
txt3 = '''yabaaa
X
Y
Z
enddddd'''

operations = [txtgen1(), txt2, txt3]

# function that takes template and write operations in a new file



# Useful tools
# sleep(2)
# os.system("copy.txt") ## writing a terminal command


Make_Operations('copy.v', 'copy.txt', operations)
