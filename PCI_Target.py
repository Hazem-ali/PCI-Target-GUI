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
    box = Entry(frame, width=5, font='bold')
    box_label = Label(frame, text=name, bg=background_color,
                      fg='white', font='bold 12')
    box_label.pack(side=RIGHT, padx=5, pady=5)
    box.pack(padx=10, pady=10)
    frame.pack()
    return box


def Create_Button_Pack(window, name, cmd, padx, font):
    btn = Button(window, text=name, command=cmd, padx=padx, font=font)
    btn.pack()
    return btn


def Create_TextBox(window, name, x, y):
    frame = Frame(window, bg='black')
    box = Entry(frame, width=5, font='bold')
    box_label = Label(frame, text=name, bg='black',
                      fg='white', font='bold 12')
    box_label.pack(side=RIGHT, padx=5, pady=5)
    box.pack(padx=10, pady=10)
    frame.place(x=x, y=y)
    return box


def Create_Button(window, name, cmd, x, y, padx, font):
    btn = Button(window, text=name, command=cmd, padx=padx, font=font)
    btn.place(x=x, y=y)
    return btn


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
    
    
    try:
        int(Words_Num.get())
    except:
        popup_warn("Please Write a number")
        return
    
    DataFrame = Toplevel()
    DataFrame.title('Data Card')
    DataFrame.configure(bg=background_color)
    DataFrame.resizable(False, False)
    entry_widgets = []
    DataFrame.grab_set()  # Focusing The Window
    for item in range(int(Words_Num.get())):
        tmpbox = Create_TextBox_Pack(DataFrame, str(item+1))
        entry_widgets.append(tmpbox)

    Confirm = Create_Button_Pack(
        DataFrame, 'Confirm', Confirm_Write_Data, 5, "bold 12")
    Confirm.config(bg="black", fg='white')


def Confirm_Write_Data():
    for item in range(int(Words_Num.get())):
        Operations.append(entry_widgets[item].get())
    DataFrame.destroy()


def TransactionStart():
    # Write Start Frame codes

    return


def TransactionEnd():
    # Write End Frame codes

    # If Read --> Execute Read Function

    # If Write --> Execute Write Function (use Operations)

    return

def Validate_Write_Entries():
    if BE.get() == "" or Words_Num.get() == "":
        popup_warn("You Must Enter Words Number And BE Code")
        return 0
    try:
        int(BE.get())
    except:
        popup_warn("Please Write a number in BE")
        return 0
    return 1

def Run():
    if user_cmd.get() == "Write":
        if not Validate_Write_Entries():
            return
        
        

    # Copy Data from operations into .v file then running it
    
    # Exec_Simulation()
    # Operations.clear()

    return


global background_color
root = Tk()
root.title("PCI Simulator")

background_color = '#1c1c1c'
background_image = ImageTk.PhotoImage(Image.open('bg.jpg'))
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
w = background_image.width()
h = background_image.height()
root.geometry(str(w)+'x'+str(h))
root.resizable(False, False)

Operations = []

# Creating radio buttons for read & write
choices = [
    ('Read', 'Read'),
    ('Write', 'Write')
]
user_cmd = StringVar()
user_cmd.set("Read")

tmpx = 220
for txt, val in choices:
    Radiobutton(root, text=txt, fg="white", bg="black", activeforeground='white', activebackground='black', highlightbackground='black', selectcolor='black', font="bold 14",
                variable=user_cmd, value=val).place(x=tmpx, y=200)
    tmpx = 575
###############################

######### Read Branch #########


###############################

######### Write Branch #########

Words_Num = Create_TextBox(root, "Words Number", 575, 250)

databutton = Create_Button(
    root, "Write Data Here", WriteData, 775, 255, 5, "bold 12")
databutton.config(fg="white", bg="black")

BE = Create_TextBox(root, "BE Code", 575, 300)

################################
Start = Create_Button(root, "Start Transaction",
                            "", 225, 500, 20, "bold 14")
Start.config(command=lambda: [TransactionStart(), Switch_Buttons(Start, End)])
End = Create_Button(root, "End Transaction",
                          "", 575, 500, 20, "bold 14")
End.config(state='disable', command=lambda: [
           TransactionStart(), Switch_Buttons(End, Start)])


Simulate = Create_Button(root, "Simulate",
                               Run, 425, 600, 20, "bold 14")
Simulate.config(fg="white", bg='#0a0c69')

root.mainloop()
