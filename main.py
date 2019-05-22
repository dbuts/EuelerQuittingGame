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
#TODO add slider for speed
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
def run(sim):
    min = int(minimum.get())
    max = int(maximum.get())
    valSize = int(size.get())
    if max-min < valSize:
        validityOutput.set("Maximum-Minimum must be > Size to have n unique values.")
        return -1
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
        sim = Simulation(min, max, valSize)
        sum += run(sim) 
        sleep(.05)
        w.update()
    average = (float(sum)/float(length)) * 100.0
    validityOutput.set("Average Correct Guess: " + str(average) + "%")

#Runs with the animation
def animatedRun():
    speed = .5
    #Get value and instantiate a simulation object
    min = int(minimum.get())
    max = int(maximum.get())
    sz = int(size.get())
    sim = Simulation(min, max, sz)

    run(sim)
    rects = createGrid(sim)

    #Steps text
    step1 = can.create_text(100,1025, text="Find Stopping Point (Size/e)",anchor="w")
    step2 = can.create_text(100,1050, text="Find Maximum Value before and including stopping point",anchor="w")
    step3 = can.create_text(100,1075, text="Find first value greater than previously found max",anchor="w")
    step4 = can.create_text(100,1100, text="Check if answer was correct",anchor="w")
    currProc = can.create_text(100, 1175, text= "Current Process: Calculating stopping point",anchor="w")
    
    #Start the actual animation loop
    d.update()

#Essentially doing eulerGuess() but with visual updates
    stopPoint = ceil(sz/e)
    sleep(speed)
    can.itemconfig(step1, fill = "red")
    can.itemconfig(currProc,text="Current Process: Stopping Point found to be: "+str(stopPoint))
    
    numColumns = ceil(sqrt(sz))

    #Color the stopping point blue
    stopRow = floor((stopPoint-1)/numColumns)
    stopCol = (stopPoint-1)%numColumns
    can.itemconfig(rects[stopRow][stopCol], fill="blue")
    d.update()
    sleep(speed)
    can.itemconfig(step1, fill = "green")
    can.itemconfig(step2, fill = "red")
    can.itemconfig(currProc, text = "Current Process: Find Maximum value within range of 0 to Stopping Point.")
    
#Start of Finding max in range 0 to Stopping Point
    #arbitrarily small number
    currMax = -999999999999999
    maxID = None
    for i in range(stopRow):
        for j in range(numColumns):
            can.itemconfig(rects[i][j],fill = "", outline="yellow", width = "5")
            d.update()
            sleep(speed)

            if sim.values[i*numColumns + j] > currMax:
                currMax = sim.values[i*numColumns + j] 
                can.delete(maxID)
                maxID = rects[i][j]
                can.itemconfig(rects[i][j],fill = "", outline="green", width = "5")
                can.itemconfig(currProc, text = "Current Process: Greater than previous max. New max is: "+str(currMax))
            else:
                can.delete(rects[i][j])
            d.update()
    
    for j in range(stopCol+1):
            can.itemconfig(rects[stopRow][j],fill = "", outline="yellow", width = "5")
            d.update()
            sleep(speed)

            if sim.values[stopRow*numColumns + j] > currMax:
                currMax = sim.values[stopRow*numColumns + j] 
                can.delete(maxID)
                maxID = rects[stopRow][j]
                can.itemconfig(currProc, text = "Current Process: Greater than previous max. New max is: "+str(currMax))
                sleep(speed)
                can.itemconfig(rects[stopRow][j],fill = "", outline="green", width = "5")

            else:
                can.delete(rects[stopRow][j])
            d.update()
#End of Finding max in range 0 to Stopping Point
    can.itemconfig(step2, fill = "green")
    can.itemconfig(currProc, text = "Current Process: Find first value greater than maximum just found.")
    can.itemconfig(step3, fill = "red")
    d.update()
#Start of Finding final Guess Value
    finalGuess = None
    #Finish the row that the stopping point is on
    for l in range(stopCol+1, numColumns):
        #Yellow for currently examined value
        can.itemconfig(rects[stopRow][l],fill = "", outline="yellow", width = "5")
        d.update()
        sleep(speed)
        #Check if this is our guess
        if sim.values[stopRow*numColumns + l] > currMax:
            #set value of guess to correct value and reflect it on canvas
            finalGuess = sim.values[stopRow*numColumns + l] 
            can.itemconfig(currProc, text = "Current Process: Value Greater than previous max found. ")
            sleep(speed)
            can.itemconfig(currProc, text = "Current Process: Final Guess is :"+str(finalGuess))
            can.itemconfig(rects[stopRow][l],fill = "", outline="blue", width = "5")
        else:
            #if not max value, no need to keep rectangle
            sleep(speed)
            can.delete(rects[stopRow][l])
        d.update()

    #loop through the rest of the complete full rows trying to find max
    numFullRows = floor(sz/numColumns)
    for m in range(stopRow+1, numFullRows):
        for n in range(0,numColumns):
            if not finalGuess:
                can.itemconfig(rects[m][n],fill = "", outline="yellow", width = "5")
                d.update()
                sleep(speed)

                if sim.values[m*numColumns + n] > currMax:
                    finalGuess = sim.values[m*numColumns + n] 
                    can.itemconfig(currProc, text = "Current Process: Value Greater than previous max found. ")
                    sleep(speed)
                    can.itemconfig(currProc, text = "Current Process: Final Guess is :"+str(finalGuess))
                    can.itemconfig(rects[m][n],fill = "", outline="blue", width = "5")
                    can.itemconfig(step3, fill = "green")
                    d.update()
                    break
                else:
                    sleep(speed)
                    can.delete(rects[m][n])
                d.update()

#Search non full row if finalGuess hasn't been made yet

    for t in range(sz%(ceil(sqrt(sz)))-1):
        if not finalGuess:
            can.itemconfig(rects[numFullRows][t],fill = "", outline="yellow", width = "5")
            d.update()
            sleep(speed)

            if sim.values[(numFullRows)*numColumns + t] > currMax:
                finalGuess = sim.values[(numFullRows)*numColumns + t] 
                can.itemconfig(currProc, text = "Current Process: Value Greater than previous max found. ")
                sleep(speed)
                can.itemconfig(currProc, text = "Current Process: Final Guess is "+str(finalGuess))
                can.itemconfig(rects[numFullRows][t],fill = "", outline="blue")
                can.itemconfig(step3, fill = "green")
                d.update()
                sleep(speed)
                break

            else:
                sleep(speed)
                can.delete(rects[numFullRows][t-1])
        d.update()
#if all values have been checked and none greater, forced to pick final value
    if not finalGuess:
        finalGuess = sim.values[(numFullRows)*numColumns + sz%ceil(sqrt(sz))-1]
        row = ceil(sz/numColumns)
        column = sz%numColumns
        #Deals with perfect squares having sqrt 0
        if column == 0:
            column = numColumns

        can.itemconfig(rects[row-1][column-1], fill = "", outline="blue", width = "5")
        d.update()
        sleep(speed)
        can.itemconfig(currProc, text = "Current Process: Out of Options, Final Guess is "+str(finalGuess))
        can.itemconfig(step3, fill = "green")
        d.update()

#Now check if answer was correct
    can.itemconfig(step4, fill = "red")
    actualMax = sim.values[0]
    location = 0
    #Find actual maximum value and highlight it in red if not what we guessed
    for x in range(1, len(sim.values)):
        if sim.values[x] > actualMax:
            actualMax = sim.values[x]
            location = x
    #If correct
    if actualMax == finalGuess:
        testCount = 1
        print(str(rects))
        for r in rects:
            print("iteration: "+str(testCount))
            testCount+=1
            for rect in r:
                if rect and str(can.itemcget(rect, "outline")) != "blue":
                    can.itemconfig(rect, fill="", outline = "")
        can.itemconfig(currProc, text = "The guess of "+str(finalGuess)+" was correct!", fill = "green")
        can.itemconfig(step4, fill="green")
        d.update
        return 1
    #If incorrect
    else:
        actualRow = ceil(location/numColumns)
        actualCol = location%numColumns
        #Check final column edge case
        if actualCol == 0:
            actualCol = numColumns-1
        for r in rects:
            for rect in r:
                can.itemconfig(rect, fill="", outline = "")
        can.itemconfig(rects[actualRow-1][actualCol], outline="red", width = "5")
        can.itemconfig(currProc, text ="The guess was wrong, the actual maximum value is: " + str(actualMax), fill = "red")
        can.itemconfig(step4, fill="green")
        d.update()
        return 0


#Creates grid of covered values
def createGrid(sim):
    #Clear canvas and get values
    can.delete("all")
    min = int(minimum.get())
    max = int(maximum.get())
    sz = int(size.get())

    numColumns = ceil(sqrt(sz))
    if sz and sz <=100:
        #width is width of canvas/sqrt(size) because size = rows*columns
        width = 1000/numColumns
        #Generate the grid of lines
        for x in range(0, numColumns):   #1000/size is the width of each square
            can.create_line(int(x*width)-1, 0, int(x*width)-1, 1000)
        for y in range(0, numColumns+1):   #1000/size is the width of each square
            can.create_line(0,int(y*width)-1, 1000, int(y*width)-1)

        #Populate the grid with text containing values
        numFullRows = floor(sz/numColumns)
        remainingVals = sz%(ceil(sqrt(sz)))

        for i in range(0, numFullRows):
            for j in range(0, numColumns):
                can.create_text(((j*width)+width/2), ((i*width)+width/2), text= str(sim.values[i*numColumns + j]), width = width-2)
        for x in range(int(remainingVals)):
            can.create_text(((x*width)+width/2), ((numFullRows*width) +width/2),text=str(sim.values[numFullRows*numColumns + x]), width = width-2)

        #Covers each unrevealed value with a rectangle object
        rects = [[None for _ in range(numColumns)] for _ in range(numColumns)]

        #Populates the array of rectangles in the correct positions
        for i in range(0, numFullRows):
            for j in range(0, numColumns):
                rects[i][j] = can.create_rectangle((j*width)+1, (i*width)+1, (j*width)+(width-1), (i*width)+(width-1), fill = "brown")
        for n in range(0, int(remainingVals)):
                rects[numFullRows][n] = can.create_rectangle((n*width)+1, (numFullRows*width)+1, (n*width)+(width-1), (numFullRows*width)+(width-1), fill = "brown")
        return rects
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
