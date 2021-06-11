# Importing required modules
from DNA import DNA
import random

# Method for applying crossover
def applyCrossover(firstParent, secondParent, chromosomeSize):
    child = DNA(chromosomeSize) # Generating a child for applying crossover
    crossoverSlice = random.randint(0, firstParent.chromosomeSize)  # Choosing random integer for applying slicing for crossover
    # Change child genes as follows
    # Child genes = genes from parent 1[0 to crossoverSlice-1] + genes from parent 2[crossoverSlice to end]
    # Giving both parents equal chance
    if(random.uniform(0, 1)<0.5):
        # Updating child genes
        for i in range(firstParent.chromosomeSize):
            if(i<crossoverSlice):
                child.chromosome[i] = firstParent.chromosome[i]
            else:
                child.chromosome[i] = secondParent.chromosome[i]
    else:
        # Updating child genes
        for i in range(firstParent.chromosomeSize):
            if(i<crossoverSlice):
                child.chromosome[i] = secondParent.chromosome[i]
            else:
                child.chromosome[i] = firstParent.chromosome[i]
    return child	# Return the child