import os


# Make Time Delay
def Delay(number):
    return '\n#' + str(number) + '\n'


def Read_Gen():

    Read_Text = """
// Operation Read
tCBE = 4'b0110;
tAD = 32'd1000;
#10
tIRDY = 0;
operation=READ;
#80
"""
    return Read_Text


def Write_Gen(Base, Data, BE):

    Write_Text = """
// Operation Write
tCBE = 4'b""" + str(BE) + """;
tAD = 32'""" + str(Base) + str(Data) + """;
#10

"""
    return Write_Text


# function that takes template and write operations in a new file
def Make_Operations(Inputfile, Outputfile, Data):
    # Opening Template file
    with open(Inputfile, "r") as source:
        lines = source.read().split('\n')  # lines is a list, each elemennt is a line
        # print("lines: ", lines)

        # Creating a new file
        with open(Outputfile, "w") as target:

            # Looking for the flag that we'll mark and write after
            for line in lines:
                if line == "module t_buffer1;":
                    line = "module t_buffertest;"
                if line == "$dumpvars(0, t_buffer1);":
                    line = "$dumpvars(0, t_buffertest);"
                
                if line == "//flag":  # Flag found
                    # Replace the flag with required operations
                    line = ''
                    for element in Data:
                        line += element + '\n'
                # writing data (new or existing)
                target.writelines(line + '\n')


def Exec_Simulation(name):
    os.system(
        'cmd /c "iverilog -o '+ name +'.vvp '+ name +'.v & vvp -n '+ name +'.vvp & gtkwave '+ name +'.vcd"')


# Useful tools
# sleep(2)
# os.system("copy.txt") ## writing a terminal command

# add included v files and timescale, then add $finish at end of tb file
