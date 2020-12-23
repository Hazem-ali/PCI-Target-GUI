from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from datetime import *
from operations import *
import os
from PIL import ImageTk, Image

# .Pack Entries


def Create_TextBox_Pack(window, name):
    frame = Frame(window, bg=background_color)
    box = Entry(frame, width=10, font='bold')
    box_label = Label(frame, text=name, bg=background_color,
                      fg='white', font='bold 12')
    box_label.pack(side=RIGHT, padx=5, pady=5)
    box.pack(padx=10, pady=10)
    frame.pack(side=LEFT)
    return box


def Create_Button_Pack(window, name, cmd, padx, font):
    btn = Button(window, text=name, command=cmd, padx=padx, font=font)
    btn.pack()
    return btn


def Create_TextBox(window, name, x, y):
    frame = Frame(window, bg=background_color)
    box = Entry(frame, width=5, font='bold')
    box_label = Label(frame, text=name, bg=background_color,
                      fg='white', font='bold 12')
    box_label.pack(side=RIGHT, padx=5, pady=5)
    box.pack(padx=10, pady=10)
    frame.place(x=x, y=y)
    return box


def Create_Button(window, name, cmd, x, y, padx, font):
    btn = Button(window, text=name, command=cmd, padx=padx, font=font)
    btn.place(x=x, y=y)
    return btn

def Create_LabelFrame(window, text, x, y, color):
    Label(window, text=text, fg='white',
          font='bold 15', bg=color).place(x=x, y=y)
    return

def popup_warn(message):
    messagebox.showwarning("Warning", message)


def PassFunction_Button(window, name, cmd, fn_data, x, y, padx, font):
    btn = Button(window, text=name, command=lambda: cmd(
        fn_data), padx=padx, font=font)
    btn.place(x=x, y=y)
    return btn


def Switch_Buttons(disable, enable):
    disable.config(state='disabled')
    enable.config(state='normal')


def CloseButton(window, x, y):
    Close_Button = Button(window, text='Close', padx=20,
                          command=lambda: window.destroy())
    Close_Button.place(x=x, y=y)


def clear(textbox):
    textbox.delete(0, END)


def WriteData():
    global DataFrame
    global entry_widgets
    global entry_BE
    global Base
    # Checking Correct Data
    try:
        int(Words_Num.get())
    except:
        popup_warn("Please Write a number")
        return

    entry_widgets = []
    entry_BE = []

    # Creating a window
    DataFrame = Toplevel()
    DataFrame.title('Data Card')
    DataFrame.configure(bg=background_color)
    DataFrame.resizable(False, False)
    DataFrame.grab_set()  # Focusing The Window

    Bases = [
        ('HEX', "h"),
        ('DEC', "d"),
        ('BIN', "b")
    ]
    Base = StringVar()
    Base.set("h")

    Bases_Frame = Frame(DataFrame, bg=background_color)
    for text, name in Bases:
        Radiobutton(Bases_Frame, text=text, fg="white", bg=background_color, activeforeground='white',
                    activebackground=background_color, highlightbackground=background_color,
                    selectcolor='black', font="bold 14",
                    variable=Base, value=name, tristatevalue=0).pack(side=LEFT)
    Bases_Frame.pack()

    default_BE = StringVar()
    default_BE.set('1111')
    # Creating entries and confirm button
    for item in range(int(Words_Num.get())):
        Entries_Frame = Frame(DataFrame, bg=background_color)
        tmpbox = Create_TextBox_Pack(Entries_Frame, str(item + 1))
        BE = Create_TextBox_Pack(Entries_Frame, "BE Code")
        # BE.configure(textvariable=default_BE)
        Entries_Frame.pack()

        entry_widgets.append(tmpbox)
        entry_BE.append(BE)

    Confirm = Create_Button_Pack(
        DataFrame, 'Confirm', Confirm_Write_Data, 5, "bold 12")
    Confirm.config(bg="black", fg='white')


def Confirm_Write_Data():
    # adding confirm data into operations list
    global BE_values
    BE_values = []
    for item in range(int(Words_Num.get())):
        Operations.append(entry_widgets[item].get())
        BE_values.append(entry_BE[item].get())
    DataFrame.destroy()
    return


def TransactionStart():
    # Write Start Frame codes
    T_Start = '''
// Frame Start
tframe = 0;
'''
    TestBench.append(T_Start)
    return


def TransactionEnd():
    # Write End Frame codes

    # If Read --> Execute Read Function

    if user_cmd.get() == "Read":
        TestBench.append(Read_Gen())

    # If Write --> Execute Write Function (use Operations)
    if user_cmd.get() == "Write":
        # Initialize Data Write
        Write_init = """
operation=WRITE;
tCBE = 4'b0111;
tAD = 32'd1000;
#10
tIRDY=0;
#10                
"""

        TestBench.append(Write_init)
        # Operations (Data), entries_BE, Base
        for i in range(len(Operations)):
            TestBench.append(Write_Gen(Base.get(), Operations[i], BE_values[i]))
            

    T_End = """
// Frame End
tframe = 1;
#10 
tIRDY = 1;
#10 
    
"""
    TestBench.append(T_End)
    return


def Validate_Write_Entries():
    if Words_Num.get() == "":
        popup_warn("You Must Enter Words Number And BE Code")
        return 0

    return 1


def Run():
    # Adding data to testbench then running
    if user_cmd.get() == "Write":
        if not Validate_Write_Entries():
            return

    # Copy Data from operations into .v file then running it
    Make_Operations("t_buffer.v", "testcase1.v", TestBench)
    Exec_Simulation("testcase1")
    # Operations.clear()

    return


# Main window

global background_color
root = Tk()
root.title("PCI Target Simulator")

background_color = '#1c1c1c'
background_image = ImageTk.PhotoImage(Image.open('bg.jpg'))
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
w = background_image.width()
h = background_image.height()
root.geometry(str(w)+'x'+str(h))
root.resizable(False, False)

Operations = []
TestBench = []

# Creating radio buttons for read & write
choices = [
    ('Read', 'Read'),
    ('Write', 'Write')
]
user_cmd = StringVar()
user_cmd.set("Read")

Create_LabelFrame(root, "Start a Transaction and Choose Method & Details", 220,200,background_color)

tmpx = 220
for txt, val in choices:
    Radiobutton(root, text=txt, fg="white", bg=background_color, activeforeground='white',
                activebackground=background_color, highlightbackground=background_color,
                selectcolor=background_color, font="bold 14",
                variable=user_cmd, value=val).place(x=tmpx, y=250)
    tmpx = 575


######### Read Branch #########


###############################

######### Write Branch #########

Words_Num = Create_TextBox(root, "Words Number", 575, 300)

databutton = Create_Button(
    root, "Write Data Here", WriteData, 775, 305, 5, "bold 12")
databutton.config(fg="white", bg=background_color)

# BE = Create_TextBox(root, "BE Code", 575, 300)

################################
Start = Create_Button(root, "Start Transaction",
                            "", 225, 500, 20, "bold 14")
Start.config(command=lambda: [TransactionStart(), Switch_Buttons(Start, End)])
Start.config(bg="#006600",fg="white")
End = Create_Button(root, "End Transaction",
                          "", 575, 500, 20, "bold 14")
End.config(state='disable', command=lambda: [
           TransactionEnd(), Switch_Buttons(End, Start)])
End.config(bg="#800000",fg="white")


Simulate = Create_Button(root, "Simulate",
                               Run, 425, 600, 20, "bold 14")
Simulate.config(fg="white", bg='#0a0c69')

root.mainloop()
