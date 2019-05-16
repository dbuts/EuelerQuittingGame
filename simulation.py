import random

def generate(min, max, size):
    values = []
    for i in range(0, size):
        values.append(random.randint(min, max))
    return values 
    
def eulerGuess(min, max, size):
    #min value, max value, size of array to select from
    values = generate(min, max, size)
    guess = values[0] 
    #TODO Implement actual algorithm lol
    return guess


