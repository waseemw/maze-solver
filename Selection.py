# Importing required modules
import random

# Method for selecting a random candidate from the population
def selectIndividuals(populationPool):
    n = len(populationPool) # Population Size
    k = 10  # Tournament size
    selectedIndex = 0  # Default index
    minFitness = float("inf")   # Minimum fitness tracker
    # Looping through population k times
    for i in range(k):
        temp = random.randint(0, n-1)   # Temporary variable for getting random index
        # If current selected index fitness is minimum
        if(populationPool[temp].fitnessValue<minFitness):
            minFitness = populationPool[temp].fitnessValue  # Update minimum fitness
            selectedIndex = temp    # Update Selected index
    return populationPool[selectedIndex]    # Return selected candidate