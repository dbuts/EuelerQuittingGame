import random

def generate(min, max, size):
    values = []
    for i in range(0, size+1):
        values.append(random.randint(min, max+1))
    return values 
    
def eulerGuess(min, max, size):
    #min value, max value, size of array to select from
    values = generate(min, max, size)
    guess = values[4] 
    return guess


