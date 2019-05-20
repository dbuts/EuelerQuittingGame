from tkinter import *
from simulation import *
import webbrowser
from time import sleep
from math import sqrt, floor, ceil

#Setup the GUI for input
w = Tk()
w.title("Euler's Guessing Simulator")
w.geometry('1920x1080')
w.columnconfigure(0, weight = 1)
w.columnconfigure(1, weight = 4)

#Setup the GUI for canvas with animation
d = Tk()
d.title("Animation of Algorithm Running")
d.geometry('1000x1200')
d.resizable(width=False, height=False)

can = Canvas(d, width = 1000, height = 1200)
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
    if max-min < valSize:
        validityOutput.set("Maximum-Minimum must be > Size to have n unique values.")
        return -1
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
    min = int(minimum.get())
    max = int(maximum.get())
    valSize = int(size.get())
    if max-min < valSize:
        validityOutput.set("Maximum-Minimum must be > Size to have n unique values.")
        return -1
    sum = 0
    length = int(numExecs.get())
    for x in range(0, length):
        sum += run() 
        sleep(.05)
        w.update()
    average = (float(sum)/float(length)) * 100.0
    validityOutput.set("Average Correct Guess: " + str(average) + "%")

#Runs with the animation
def animatedRun():
    run()
    createGrid()
    d.mainloop()

#Creates grid of covered values
def createGrid():
    #Clear canvas and get values
    can.delete("all")
    min = int(minimum.get())
    max = int(maximum.get())
    sz = int(size.get())

    #Create simulation object
    sim = Simulation(min, max, sz)
    #Show details at bottom of canvas
    minText = can.create_text(250,1100, text="Minimum Possible Value: "+str(min),anchor="w")
    maxText = can.create_text(250,1125, text="Maximum Possible Value: "+str(max),anchor="w")
    sizeText = can.create_text(250,1150, text="Number of Values: "+str(sz),anchor="w")

    numColumns = ceil(sqrt(sz))
    if sz and sz <=100:
        #width is width of canvas/sqrt(size) because size = rows*columns
        width = 1000/numColumns
        #Generate the grid of lines
        for x in range(0, numColumns):   #1000/size is the width of each square
            can.create_line(int(x*width)-1, 0, int(x*width)-1, 1000)
        for y in range(0, numColumns+1):   #1000/size is the width of each square
            can.create_line(0,int(y*width)-1, 1000, int(y*width)-1)

        #TODO Populate the grid with text containing values
        numFullRows = floor(sz/numColumns)
        remainingVals = sz%(ceil(sqrt(sz)))
        if remainingVals == 0:
            numFullRows+=1

        for i in range(0, numFullRows):
            for j in range(0, numColumns):
                can.create_text(((j*width)+width/2), ((i*width)+width/2), text= str(sim.values[i*numColumns + j]), width = width-2)
        for x in range(int(remainingVals)):
            can.create_text(((x*width)+width/2), ((numFullRows*width) +width/2),text=str(sim.values[numFullRows*numColumns + x]), width = width-2)

        #Covers each unrevealed value with a rectangle object
        rects = [[None for _ in range(numColumns)] for _ in range(numColumns)]

        #Creates the arrays in the correct positions
        for i in range(0, numFullRows):
            for j in range(0, numColumns):
                rects[i][j] = can.create_rectangle((j*width)+1, (i*width)+1, (j*width)+(width-1), (i*width)+(width-1), fill = "brown")
        for n in range(0, int(remainingVals)):
                rects[numFullRows][n] = can.create_rectangle((n*width)+1, (numFullRows*width)+1, (n*width)+(width-1), (numFullRows*width)+(width-1), fill = "brown")

    else:
        errorTxt = can.create_text(500,500, text = "INVALID SIZE. SIZE MUST BE BETWEEN 0 AND 100")

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
start = Button(w, text = "Start (Executes Once)", font = default_font, command=animatedRun)
start.grid(column=0, row = 15)

longTest = Button(w, text = "Long Test (1000 Executions)", font = default_font, command = longRun)
longTest.grid(column=0, row = 16)

#Tell GUI to run
w.mainloop()
