# Importing required modules
import random

# Class for defining the properties of a candidate in the population
class DNA:
    def __init__(self, chromosomeSize):
        self.chromosomeSize = chromosomeSize    # Size of the chromosome
        self.chromosome = self.generateChromosome() # Generating chromosome
        self.fitnessValue = 0    # Fitness value of a candidate

    # Method for generating chromosome
    def generateChromosome(self):
        chromosome = list() # Initializing empty chromosome
        # Loop through chromosome size
        for i in range(self.chromosomeSize):
            chromosome.append(self.generateGene())  # Add randomly generated gene to the chromosome
        return chromosome   # Return the chromosome

    # Method for generating a random gene
    def generateGene(self):
        # Choose a random integer between 0 and 3 both inclusive
        # 0 to 3 means,
        # 0 means go up
        # 1 means go left
        # 2 means go bottom
        # 3 means go right
        gene = random.randint(0, 3)
        return gene    # Return the randomly generated gene