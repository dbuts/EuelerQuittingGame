import random
from math import e, ceil

class Simulation:
    def __init__(self, minimum, maximum, valSize):
        self.min = minimum
        self.max = maximum
        self.size = valSize
        self.values = []
        self.generate()

    #Generates array of (size) items between given min/max
    def generate(self):
        self.values = []
        for i in range(0, self.size):
            self.values.append(random.randint(self.min, self.max))

    def eulerGuess(self):
        #Min value, max value, size of array to select from
        print(self.values)
        #The stopping point provided by theorem
        stopPoint = ceil(self.size/e)
        print("Stopping point: "+ str(stopPoint))
        currMax = self.values[0] 
        #Find largest value in fist size/e values
        for x in range(1, stopPoint):
            if x > currMax:
                currMax = x
        #Find and return first value larger than previous max
        for y in range(stopPoint, self.size):
            if y > currMax:
                return y
        #Because we're not allowed to pick a value we revealed and passed on, even if the last value isn't the largest it's the only one we're allowed to pick
        return self.values[self.size-1]

    def findMax(self):
        return max(self.values)

    def validityChecker(self, guess):
        if self.findMax() == guess:
            return True
        else:
            return False

