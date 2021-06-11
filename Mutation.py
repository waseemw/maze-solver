# Importing required modules
import random

# Method for mutating genes of the population
def applyMutation(child, mutationRate):
    # Looping through the child genes
    for i in range(child.chromosomeSize):
        prob = random.random()  # Random float value between 0 and 1, it will be treated as probability
        # If mutation rate is higher, then there is a greater chance that "prob" value will lie between [0, mutation rate)
        # e.g. If mutation rate is 0.9, then there is a greater chance that "prob" value will lie between [0, 0.9)
        # Hence mutating the current gene
        # Normally a low mutation rate is taken, that is why the probability of mutating a gene is lower
        if(prob<mutationRate):
            child.chromosome[i] = child.generateGene()