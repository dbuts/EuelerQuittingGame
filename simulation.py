import random
from math import e, ceil

class Simulation
    def _init__():
        
    #public so all functions have access
    values = []
    #Generates array of (size) items between given min/max
    def generate(min, max, size):
        values = []
        for i in range(0, size):
            values.append(random.randint(min, max))
        return values 
        
    def eulerGuess(min, max, size):
        #Min value, max value, size of array to select from
        values = generate(min, max, size)
        print(values)
        #The stopping point provided by theorem
        stopPoint = ceil(size/e)
        print("Stopping point: "+ str(stopPoint))
        currMax = values[0] 
        #Find largest value in fist size/e values
        for x in range(1, stopPoint):
            if x > currMax:
                currMax = x
        #Find and return first value larger than previous max
        for y in range(stopPoint, size):
            if y > currMax:
                return y
        #Because we're not allowed to pick a value we revealed and passed on, even if the last value isn't the largest it's the only one we're allowed to pick
        return values[size-1]

    def findMax():
        return max(values)

    def validityChecker(guess):
        if findMax() == guess:
            return True
        else:
            return False


