# Importing required modules
from DNA import DNA
from Selection import selectIndividuals
from Crossover import applyCrossover
from Mutation import applyMutation


# Class for defining properties of the population
class Population:
    def __init__(self, populationSize, mutationRate):
        self.populationSize = populationSize    # No of candidates in the population
        self.mutationRate = mutationRate    # Mutation rate for changing a candidate genes
        self.chromosomeSize = 2    # Initial candidate DNA size
        self.populationPool = self.generateInitialPopulation()  # Method to generate population pool
        self.bestInPopulation = None    # It keeps track of the best candidate in the population
        self.generation = 1 # It keeps track of current generation number

    # Method for initializing population
    def generateInitialPopulation(self):
        populationPool = list() # Initializing empty pool
        for i in range(self.populationSize):
            populationCandidate = DNA(self.chromosomeSize)  # Generating a candidate for the population
            # calculateFitness(populationCandidate, self.target)    # Calculating fitness of the candidate
            populationPool.append(populationCandidate)  # Adding candidate to the pool
        return populationPool   # Returning created pool

    # Method for generating new population
    def generateNewPopulation(self):
        newPopulationPool = list()  # Initializing new pool
        for i in range(self.populationSize):
            firstParent = selectIndividuals(self.populationPool)  # Selecting first parent from population
            secondParent = selectIndividuals(self.populationPool) # Selecting second parent from population
            child = applyCrossover(firstParent, secondParent, self.chromosomeSize) # Applying crossover between first and second parent and creating a child
            applyMutation(child, self.mutationRate)    # Applying mutation in child
            newPopulationPool.append(child)  # Adding child to the pool
        self.generation += 1    # Incrementing generation count
        self.populationPool = newPopulationPool # Changing population pool to the new pool