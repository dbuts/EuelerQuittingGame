from tkinter import *
from simulation import *
import webbrowser

window = Tk()
window.title("Euler's Guessing Simulator")
window.geometry('1600x900')
default_font = ("Arial", 12)
output = StringVar()
output.set("Returned Value: N/A")

def callback(event):
    webbrowser.open_new(r"https://www.youtube.com/watch?v=OeJobV4jJG0")



description = Label(window, text = "This is a program that simulates the Euler process for guessing the highest number in a series of hidden random numbers.", font = default_font)
link = Label(window,fg="blue", text = "Link to Vsauce video", cursor = "hand2", font = default_font)
returnedVal=Label( window,  textvariable = output)

link.bind("<Button-1>", callback)
description.grid(column=0, row=0)
link.grid(column=0, row =1)
returnedVal.grid(column= 0, row = 2)

minimum = Entry(window, width=50)
maximum = Entry(window, width=50)
size = Entry(window, width=50)

minimum.grid(column=0, row = 3)
maximum.grid(column=0, row = 4)
size.grid(column=0, row = 5)

def run():
    min = int(minimum.get())
    max = int(maximum.get())
    valSize = int(size.get())
    output.set("Returned Value: " + str(eulerGuess(min, max, valSize)))

start = Button(window, text = "Start", font = default_font, command = run)
start.grid(column=0, row = 10)




window.mainloop()
