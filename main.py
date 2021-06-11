# Importing required modules
import pygame
from Population import Population
from FitnessEvaluation import RunAgent, calcFitness
import random

pygame.init()	# Initializing pygame instance

f = open("maze.txt", "r")	# Reading maze


maze = []	# Empty list for keeping track of maze
for line in f.readlines():
	maze.append([i for i in line.strip()])	# Adding lines to maze

COL_SIZE = 20	# Cell size

WIDTH = len(maze[0])*COL_SIZE	# Width of the maze
HEIGHT = len(maze)*COL_SIZE	# Height of the maze

display = pygame.display.set_mode((WIDTH, HEIGHT))	# Creating display object
pygame.display.set_caption("Maze Solver")	# Setting display caption
pygame.time.set_timer(pygame.USEREVENT+1, 750)
dont_burn_my_cpu = pygame.time.Clock()	# Adding a clock


# Colors to be used in maze
COLORS = {
	"#": (128, 128, 128),
	".": (255, 255, 255),
	"S": (255, 0, 0),
	"E": (0, 255, 0),
	"path": (0, 0, 255)
}

# Loop to get start position from the maze
StartPos = None
for i, block in enumerate(maze[0]):
	if(block=="S"):
		StartPos = [0, i]
		break


# Loop to get end position from the maze
EndPos = None
for i, block  in enumerate(maze[len(maze)-1]):
	if(block=="E"):
		EndPos = [len(maze)-1, i]
		break


# Method for drawing maze
def DrawMaze():
	global COLORS, COL_SIZE, display, maze
	for i, line in enumerate(maze):
		for j, block in enumerate(line):
			pygame.draw.rect(display, COLORS[block], 
				pygame.Rect(j*COL_SIZE, i*COL_SIZE, COL_SIZE, COL_SIZE), 0)

# Method for drawing path
def DrawPath(path):
	global maze, COL_SIZE, display, COLORS
	for pos in path:
		pygame.draw.rect(display, COLORS["path"],
			pygame.Rect(pos[1]*COL_SIZE, pos[0]*COL_SIZE, COL_SIZE, COL_SIZE), 0)		


PopulationSize = 100	# Population size
MutationRate = 0.01	# MutationRate
population = Population(PopulationSize, MutationRate)	# Creating population object
popPool = population.populationPool	# Getting population pool
index = 0	# Variable for keeping track of pool index
# Loop to draw everything on screen
print("Generation:", population.generation)	# Printing first generation
minFitness = float("inf")	# Variable for keeping track of minimum fitness
runGenetic = True	# Variable for deciding whether to run genetic algorithm or not
while True:
	display.fill((255, 255, 255))	# Filling screen with white color
	# If index reached population pool length
	if(index>=len(popPool)):
		index = 0	# Resetting index
		population.generateNewPopulation()	# Generating new population
		# If population chromosome size is less than 200 then increment chromosome size
		if(population.chromosomeSize<200):
			population.chromosomeSize += 4	# This is just to limit the search space at first and broaden it as the generation increases
		popPool = population.populationPool	# Getting the new population pool
		print("Best In Generation:", population.bestInPopulation, end="\n\n")	# Printing best solution in population
		print("Generation:", population.generation)	# Printing generation number
	DrawMaze()	# Drawing maze
	# If run genetic is false
	if(not runGenetic):
		DrawPath(population.bestInPopulation)	# Then draw best path
	else:
		path = RunAgent(popPool[index], StartPos, EndPos, maze)	# Otherwise calculate path
		DrawPath(path)	# Draw the calculated path
		# If fitness is less than minimum fitness
		if(popPool[index].fitnessValue<minFitness):
			population.bestInPopulation = path.copy()	# Then update best path
			minFitness = popPool[index].fitnessValue	# Update minimum fitness
		# If fitness value is 0 means it's best
		if(popPool[index].fitnessValue==0):
			runGenetic = False	# Then stop genetic algorithm
			print("Best Path:", population.bestInPopulation)	# Printing best path for the maze
	# Loop to get events
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			pygame.quit()	# Quitting the game
			exit(0)
	pygame.display.update()	# Updating the display
	dont_burn_my_cpu.tick(60)	# Setting a clock with value, 60 means 60FPS
	# If run genetic is true
	if(runGenetic):
		index += 1	# Update index