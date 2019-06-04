import tkinter as tk
import turtle
from random import randint
from tm import *
from meme import *
from tms import *
# *************************************************************************
#main tk (the menu starts below)
root = tk.Tk()
root.option_add("*Font", "courier")
root.wm_title("MENU - BACKROW PYTHON PRESENTATION")
root.minsize(400, 200)
a = tk.Button(root, text="trihston",font=('courier', '20') ,command=trihston)
b = tk.Button(root, text="jony  ",font=('courier', '20') ,command=jony)
c = tk.Button(root, text=" bryan  ",font=('courier', '20') ,command=bryan)

t1 = tk.Label(root, text="turtleg: TLM",font=('courier', '10'))
t2 = tk.Label(root, text="meme: jony",font=('courier', '10'))
t3 = tk.Label(root, text = "spyral: bryan",font=('courier', '10'))

a.pack()
b.pack()
c.pack()
t1.pack()
t2.pack()
t3.pack()
root.mainloop()

"""
This menu needs a lot of workself.
"""
