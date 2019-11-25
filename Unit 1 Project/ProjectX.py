import tkinter as tk
import os
from PIL import Image, ImageTk


#number associated with each variable defines which row it is in

root = tk.Tk()

root.title("ATL Tracker")

print("Start program")
root.configure(bg="#233C6A")

#variables
path = '1200px-Upper_Canada_College_Crest.svg.jpg'

img = ImageTk.PhotoImage(Image.open(path))

panelA = tk.Label(root, image = img, highlightthickness=0)
panelB = tk.Label(root, image = img, highlightthickness=0)
L = tk.Label(root, fg="#233C6A", text="Welcome to the ATL Tracker!", bg="#2fbc2f", font=("Helvetica", "55"))
canvas1 = tk.Canvas(root, width=25, height=50, bg = "#233C6A", highlightthickness=0)
studentlabel2 = tk.Label(root, text="Select a student", bg="#2fbc2f", font="Helvetica", fg="#233C6A")
canvas3 = tk.Canvas(root, width=150, height=25, bg = "#3b5482", highlightthickness=1)
canvas4 = tk.Canvas(root, width=25, height=25, bg = "#233C6A", highlightthickness=0)
studentlabel5 = tk.Label(root, text="Select an ATL",font="Helvetica", bg="#2fbc2f", fg="#233C6A")
canvas8 = tk.Canvas(root, width=25, height=25, bg = "#233C6A", highlightthickness=0)
canvas6 = tk.Canvas(root, width=150, height=25, bg = "#3b5482", highlightthickness=1)
label3 = tk.Label(root,text="Dropdown soon",fg="#233C6A", bg="#233C6A", font="Helvetica")
studentlabel8 = tk.Label(root, text="Choose grade",font="Helvetica", bg="#2fbc2f", fg="#233C6A")
canvas7 = tk.Canvas(root, width=25, height=25, bg = "#233C6A", highlightthickness=0)
canvas9 = tk.Canvas(root, width=25, height=25, bg = "#3b5482", highlightthickness=1)
canvas10 = tk.Canvas(root, width=25, height=25, bg = "#3b5482", highlightthickness=1)
canvas11 = tk.Canvas(root, width=25, height=25, bg = "#3b5482", highlightthickness=1)
canvas12 = tk.Canvas(root, width=25, height=25, bg = "#3b5482", highlightthickness=1)
canvas13 = tk.Canvas(root, width=25, height=25, bg = "#233C6A", highlightthickness=0)
canvas14 = tk.Canvas(root, width=25, height=25, bg = "#233C6A", highlightthickness=0)
canvas15 = tk.Canvas(root, width=25, height=25, bg = "#233C6A", highlightthickness=0)
variablestudents = tk.IntVar(root)
fontlistbox3 = tk.OptionMenu(root, variablestudents, "Student 1", "Student 2", "Student 3", "Student 4")
variableatl = tk.IntVar(root)
fontlistbox6 = tk.OptionMenu(root, variableatl, "ATL 1", "ATL 2", "ATL 3", "ATL 4")
button9 = tk.Button(text="1-2", highlightbackground="#233C6A")
button10 = tk.Button(text="3-4", highlightbackground="#233C6A")
button11 = tk.Button(text="5-6", highlightbackground="#233C6A")
button12 = tk.Button(text="7-8", highlightbackground="#233C6A")
button16 = tk.Button(text="Submit Grade", highlightbackground="#EE5E36", fg="#233C6A")
#end of variables



panelA.grid(row = 0, column = 0)
panelB.grid(row = 0, column = 5)

L.grid(row = 0, column = 1, columnspan = 4)

canvas1.grid(row=1, column=2)

studentlabel2.grid(row=2, column= 2)
canvas3.grid(row=3, column=2)
canvas4.grid(row=4, column=2)
studentlabel5.grid(row=5, column= 2)
canvas8.grid(row=8, column=2)
canvas6.grid(row=6, column=2)


label3.grid(row=3, column=1)


studentlabel8.grid(row=8, column= 2)
canvas7.grid(row=7, column=2)
canvas9.grid(row=9, column=2)
canvas10.grid(row=10, column=2)
canvas11.grid(row=11, column=2)
canvas12.grid(row=12, column=2)
canvas13.grid(row=13, column=2)
canvas14.grid(row=14, column=2)
canvas15.grid(row=15, column=2)

#dropdown code
variablestudents.set("Students") # default value

fontlistbox3.config(fg="#233C6A", highlightbackground="#233C6A",width=10, font =("Franklin Gothic", "15"))
fontlistbox3.grid(row=3, column=2)



variableatl.set("ATL's") # default value

fontlistbox6.config(fg="#233C6A", highlightbackground="#233C6A",width=10, font =("Franklin Gothic", "15"))
fontlistbox6.grid(row=6, column=2)

button9.grid(row=9, column=2)
button10.grid(row=10, column=2)
button11.grid(row=11, column=2)
button12.grid(row=12, column=2)


button16.grid(row=16, column=2)
root.mainloop()
print ("End program")




