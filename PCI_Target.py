from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from datetime import *
import sqlite3
import cv2
import os
from PIL import ImageTk, Image

root = Tk()
root.title("PCI Simulator")


background_color = '#1c1c1c'
background_image = ImageTk.PhotoImage(Image.open('bg.png'))
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
w = background_image.width()
h = background_image.height()
root.geometry(str(w)+'x'+str(h))
root.resizable(False, False)

# os.system("dir")

root.mainloop()
