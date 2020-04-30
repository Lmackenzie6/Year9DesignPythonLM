import tkinter as tk
import tkinter.font as tkFont



def motion(event):
  print("Mouse position: (%s %s)" % (event.x, event.y))
  return

root = tk.Tk()

canvas = tk.Canvas(root, width=300, height=400)
canvas.pack()




canvas.create_rectangle(100,50,200,250, fill = "grey") #building frame

#row 1 squares
canvas.create_rectangle(110,80,130,100, fill = "blue") 
canvas.create_rectangle(140,80,160,100, fill = "blue") 
canvas.create_rectangle(170,80,190,100, fill = "blue") 
#row 2 squares
canvas.create_rectangle(110,120,130,140, fill = "blue") 
canvas.create_rectangle(140,120,160,140, fill = "blue") 
canvas.create_rectangle(170,120,190,140, fill = "blue") 
#row 3 squares
canvas.create_rectangle(110,160,130,180, fill = "blue") 
canvas.create_rectangle(140,160,160,180, fill = "blue") 
canvas.create_rectangle(170,160,190,180, fill = "blue") 
#door
canvas.create_rectangle(140,200,160,240, fill = "brown")
#doorknob
canvas.create_oval(155,230,160,234)



fontStyle = tkFont.Font(family="Lucida Grande", size=50)





for i in range(0,60,3):

	canvas.create_oval(0,0 + i,60,0 + i)
	canvas.create_oval(0 + i,0,0 + i,60)


canvas.bind('<Motion>',motion) 







root.mainloop();