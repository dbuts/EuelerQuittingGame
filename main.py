from tkinter import *
from simulation import *
import webbrowser
from time import sleep

#Setup the GUI for input
w = Tk()
w.title("Euler's Guessing Simulator")
w.geometry('1920x1080')
w.columnconfigure(0, weight = 1)
w.columnconfigure(1, weight = 4)

#Setup the GUI for canvas with animation
d = Tk()
d.title("Animation of Algorithm Running")
d.geometry('1000x1000')

can = Canvas(d, width = 1000, height = 1000)
can.pack()

#Variables to control output labels' text
default_font = ("Arial", 12)

guessOutput = StringVar()
guessOutput.set("Guessed Maximum Value: N/A")
actualOutput = StringVar()
actualOutput.set("Actual Maximum Value: N/A")
validityOutput = StringVar()
validityOutput.set("")

#Functions
def callback(event):
    webbrowser.open_new(r"https://www.youtube.com/watch?v=OeJobV4jJG0")

#runs the eulerGuess algorithm once and outputs information to GUI
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

#Exectutes the run function multiple times and displays average correctness
def longRun():
    sum = 0
    length = int(numExecs.get())
    for x in range(0, length):
        sum += run() 
        sleep(.05)
        w.update()
    average = (float(sum)/float(length)) * 100.0
    validityOutput.set("Average Correct Guess: " + str(average) + "%")

def animatedRun():
    run()
    createGrid()
    d.mainloop()

def createGrid():
    sz = int(size.get())
    if sz and sz <=100:
        width = 1000/sz
        for x in range(0, sz):   #1000/size is the width of each square
            can.create_line(int(x*width)-1, 0, int(x*width)-1, 1000)
        for y in range(0, sz):   #1000/size is the width of each square
            can.create_line(0,int(y*width)-1, 1000, int(y*width)-1)
#Label for description and video going more in depth by Vsauce
description = Label(w, text = "This is a program that simulates the Euler process for guessing the highest number in a series of hidden random numbers.", font = default_font)
link = Label(w,fg="blue", text = "Link to Vsauce video", cursor = "hand2", font = default_font)

description.grid(column=0, row=0)
link.grid(column=0, row =1)
link.bind("<Button-1>", callback)

#Text boxes to enter data with accomponying labels
minimum = Entry(w, width=50)
minimum.insert(0, "1")
minLbl = Label(w, text="Minimum: ", font = default_font)
maximum = Entry(w, width=50)
maximum.insert(0, "100")
maxLbl = Label(w, text="Maximum: ", font = default_font)
size = Entry(w, width=50)
size.insert(0, "10")
sizeLbl = Label(w, text="Size: ", font = default_font)
numExecs = Entry(w, width =50)
numExecs.insert(0, "100")
numExLbl = Label(w, text="Number of Executions: ", font = default_font)


#Positioning Entries and Labels
minimum.grid(column=0, row = 6)
minLbl.grid(column=0, row = 5)
maximum.grid(column=0, row = 8)
maxLbl.grid(column=0, row = 7)
size.grid(column=0, row = 10)
sizeLbl.grid(column=0, row = 9)
numExecs.grid(column=0, row =18) 
numExLbl.grid(column=0, row = 17)

#Labels to show guess vs correct answer and button to initiate program
returnedVal=Label(w,  textvariable = guessOutput)
returnedVal.grid(column= 0, row = 2)
correctVal=Label( w,  textvariable = actualOutput)
correctVal.grid(column= 0, row = 3)
validityVal=Label( w,  textvariable = validityOutput)
validityVal.grid(column= 0, row = 4)

#Button placement and assignment
start = Button(w, text = "Start (Executes Once)", font = default_font, command = animatedRun)
start.grid(column=0, row = 15)

longTest = Button(w, text = "Long Test (1000 Executions)", font = default_font, command = longRun)
longTest.grid(column=0, row = 16)

#Tell GUI to run
w.mainloop()
