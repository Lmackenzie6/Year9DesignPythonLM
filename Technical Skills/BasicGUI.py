import tkinter as tk



def runMe():
	output1.insert(1.0,"HI");
	output2.config(bg = "blue")

print("Start Program")
root = tk.Tk()#builds your main window

#Widget/element is an element in a GUI
#Button, Textbox, Input box, drop down, image
#Step 1: Construct the widget
btn1 = tk.Button(root, width = 100, height = 3)
#Step 2: Configure the widget
btn1.config(text = "I am a button")
#Step 3: Place the widget - pack(), grid(), 
btn1.pack()


output1 = tk.Text(root, width = 100, height = 20, borderwidth = 2, relief = tk.GROOVE)
output1.config(bg = "pink")
output1.pack();

btn2 = tk.Button(root, width = 100, height = 3, command = runMe)

btn2.config(text = "I am another button")

btn2.pack()


output2 = tk.Text(root, width = 100, height = 20, borderwidth = 2, relief = tk.GROOVE)
output2.config(bg="pink")
output2.pack();


root.mainloop()
print("END PROGRAM")