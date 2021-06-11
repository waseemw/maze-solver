# Method for calculating agent paths
def RunAgent(agent, StartPos, EndPos, maze):
    temp = StartPos.copy()  # Making copy of startpos for not changing startpos
    path = []   # Empty list for agent path
    premove = agent.chromosome[0]   # Variable for keeping track of previous move
    # Loop to iterate through all the moves
    for i, move in enumerate(agent.chromosome):
        # If previous move is opposite of current move then skip this move
        if((premove==0 and move==2) or (premove==2 and move==0)):
            continue
        # If previous move is opposite of current move then skip this move
        if((premove==1 and move==3) or (premove==3 and move==1)):
            continue
        # If move is 0 then go up
        if(move==0):
            temp[0] -= 1
        # If move is 1 then go left
        elif(move==1):
            temp[1] -= 1
        # If move is 2 then go down
        elif(move==2):
            temp[0] += 1
        # If move is 3 then go right
        elif(move==3):
            temp[1] += 1
        # If current position is equal to target position then break the loop
        if(temp[0]==EndPos[0] and temp[1]==EndPos[1]):
            break
        # If position is out of bounds
        if(temp[0]<0 or temp[0]>=len(maze)):
            # Reverse the move
            if(move==0):
                temp[0] += 1
            elif(move==2):
                temp[0] -= 1
            continue    # Skip the move
        # If position is out of bounds
        if(temp[1]<0 or temp[1]>=len(maze[0])):
            # Reverse the move
            if(move==1):
                temp[1] += 1
            elif(move==3):
                temp[1] -= 1
            continue    # Skip the move
        # If position is a wall
        if(maze[temp[0]][temp[1]]=="#"):
            # Reverse the move
            if(move==0):
                temp[0] += 1
            elif(move==1):
                temp[1] += 1
            elif(move==2):
                temp[0] -= 1
            elif(move==3):
                temp[1] -= 1
            wallCount = 0  # Variable for keeping track of adjacent walls
            # If position's top position is a wall
            if((temp[0]-1)>=0 and maze[temp[0]-1][temp[1]]=="#"):
                wallCount += 1
            # If position's down position is a wall
            if((temp[0]+1)<len(maze) and maze[temp[0]+1][temp[1]]=="#"):
                wallCount += 1
            # If position's left position is a wall
            if((temp[1]-1)>=0 and maze[temp[0]][temp[1]-1]=="#"):
                wallCount += 1
            # If position's right position is a wall
            if((temp[1]+1)<len(maze[0]) and maze[temp[0]][temp[1]+1]=="#"):
                wallCount += 1
            # If there are 3 adjacent walls means it is a dead-end
            if(wallCount==3):
                agent.fitnessValue = 99999  # Assigning this agent fitness a higher value
                break   # Breaking the loop
            continue    # Otherwise skip this move
        path.append(temp.copy())    # Adding move to the path list
        premove = move # Updating previous move
    # If Agent already has fitness greater than 0
    if(agent.fitnessValue>0):
        agent.fitnessValue += calcFitness(temp, EndPos)*100 # Add more as a penalty, if path is distant from target penalty will be high otherwise low
    else:
        agent.fitnessValue = calcFitness(temp, EndPos)  # Otherwise updating agent fitness
    return path # Returning path

# Method for calculating fitness
def calcFitness(temp, end_pos):
    return (temp[0]-end_pos[0])**2 + (temp[1]-end_pos[1])**2    # Fitness is the squared sum distance between target and current position