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
        self.values = random.sample(range(self.min, self.max), self.size)

    def eulerGuess(self):
        #The stopping point provided by theorem
        stopPoint = ceil(self.size/e)
        currMax = self.values[0] 
        #Find largest value in fist size/e values
        for x in range(1, stopPoint):
            if self.values[x] >= currMax:
                currMax = self.values[x]
        #Find and return first value larger than previous max
        for y in range(stopPoint, self.size):
            if self.values[y] >= currMax:
                return self.values[y]
        #Because we're not allowed to pick a value we revealed and passed on, even if the last value isn't the largest it's the only one we're allowed to pick
        return self.values[self.size-1]

    def findMax(self):
        return max(self.values)

    def validityChecker(self, guess):
        if self.findMax() == guess:
            return True
        else:
            return False

