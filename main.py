from tkinter import *
from simulation import *
import webbrowser

#Setup the GUI itsef
window = Tk()
window.title("Euler's Guessing Simulator")
window.geometry('1920x1080')
window.columnconfigure(0, weight = 1)
window.columnconfigure(1, weight = 4)

default_font = ("Arial", 12)

#Variable to control output label's text
output = StringVar()
output.set("Returned Value: N/A")

#Functions
def callback(event):
    webbrowser.open_new(r"https://www.youtube.com/watch?v=OeJobV4jJG0")

def run():
    min = int(minimum.get())
    max = int(maximum.get())
    valSize = int(size.get())
    output.set("Returned Value: " + str(eulerGuess(min, max, valSize)))

#Label for description and video going more in depth by Vsauce
description = Label(window, text = "This is a program that simulates the Euler process for guessing the highest number in a series of hidden random numbers.", font = default_font)
link = Label(window,fg="blue", text = "Link to Vsauce video", cursor = "hand2", font = default_font)

description.grid(column=0, row=0)
link.grid(column=0, row =1)
link.bind("<Button-1>", callback)

#Text boxes to enter data with accomponying labels
minimum = Entry(window, width=50)
minLbl = Label(window, text="Minimum: ", font = default_font)
maximum = Entry(window, width=50)
maxLbl = Label(window, text="Maximum: ", font = default_font)
size = Entry(window, width=50)
sizeLbl = Label(window, text="Size: ", font = default_font)


minimum.grid(column=0, row = 4)
minLbl.grid(column=0, row = 3)
maximum.grid(column=0, row = 6)
maxLbl.grid(column=0, row = 5)
size.grid(column=0, row = 8)
sizeLbl.grid(column=0, row = 7)

#Label to show returned value and button to initiate program
returnedVal=Label( window,  textvariable = output)
returnedVal.grid(column= 0, row = 2)

start = Button(window, text = "Start", font = default_font, command = run)
start.grid(column=0, row = 10)




window.mainloop()
