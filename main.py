from tkinter import *
from simulation import *
import webbrowser
from time import sleep

#Setup the GUI itsef
window = Tk()
window.title("Euler's Guessing Simulator")
window.geometry('1920x1080')
window.columnconfigure(0, weight = 1)
window.columnconfigure(1, weight = 4)

default_font = ("Arial", 12)

#Variables to control output labels' text
guessOutput = StringVar()
guessOutput.set("Guessed Maximum Value: N/A")
actualOutput = StringVar()
actualOutput.set("Actual Maximum Value: N/A")
validityOutput = StringVar()
validityOutput.set("")

#Functions
def callback(event):
    webbrowser.open_new(r"https://www.youtube.com/watch?v=OeJobV4jJG0")

def run():
    min = int(minimum.get())
    max = int(maximum.get())
    valSize = int(size.get())
    sim = Simulation(min, max, valSize)
    eGuess = sim.eulerGuess()
    guessOutput.set("Guessed Value: " + str(eGuess))
    actualOutput.set("Actual Value: " + str(sim.findMax()))
    if sim.validityChecker(eGuess):
        validityOutput.set("Correct!")
        return 1
    else:
        validityOutput.set("Incorrect.")
    return 0

def longRun():
    sum = 0
    length = int(numExecs.get())
    for x in range(0, length):
        sum += run() 
        sleep(.05)
        window.update()
    average = (float(sum)/float(length)) * 100.0
    validityOutput.set("Average Correct Guess: " + str(average) + "%")

#Label for description and video going more in depth by Vsauce
description = Label(window, text = "This is a program that simulates the Euler process for guessing the highest number in a series of hidden random numbers.", font = default_font)
link = Label(window,fg="blue", text = "Link to Vsauce video", cursor = "hand2", font = default_font)

description.grid(column=0, row=0)
link.grid(column=0, row =1)
link.bind("<Button-1>", callback)

#Text boxes to enter data with accomponying labels
minimum = Entry(window, width=50)
minimum.insert(0, "1")
minLbl = Label(window, text="Minimum: ", font = default_font)
maximum = Entry(window, width=50)
maximum.insert(0, "100")
maxLbl = Label(window, text="Maximum: ", font = default_font)
size = Entry(window, width=50)
size.insert(0, "10")
sizeLbl = Label(window, text="Size: ", font = default_font)
numExecs = Entry(window, width =50)
numExecs.insert(0, "100")
numExLbl = Label(window, text="Number of Executions: ", font = default_font)


minimum.grid(column=0, row = 6)
minLbl.grid(column=0, row = 5)
maximum.grid(column=0, row = 8)
maxLbl.grid(column=0, row = 7)
size.grid(column=0, row = 10)
sizeLbl.grid(column=0, row = 9)
numExecs.grid(column=0, row =18) 
numExLbl.grid(column=0, row = 17)

#Labels to show guess vs correct answer and button to initiate program
returnedVal=Label(window,  textvariable = guessOutput)
returnedVal.grid(column= 0, row = 2)
correctVal=Label( window,  textvariable = actualOutput)
correctVal.grid(column= 0, row = 3)
validityVal=Label( window,  textvariable = validityOutput)
validityVal.grid(column= 0, row = 4)

start = Button(window, text = "Start (Executes Once)", font = default_font, command = run)
start.grid(column=0, row = 15)

longTest = Button(window, text = "Long Test (1000 Executions)", font = default_font, command = longRun)
longTest.grid(column=0, row = 16)

window.mainloop()
