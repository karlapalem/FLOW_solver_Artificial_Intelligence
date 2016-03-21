# Import the Classes file and the Grid file
from Classes import *
from Grid import *

# DFS To find if any path exists for a SubProblem
def findIfAPathExists(subProblem):
    fringe = Stack()  # Fringe to manage which states to expand
    fringe.push(subProblem.getStartState())
    visited = []  # List to check whether state has already been visited
    tempPath = []  # Temp variable to get intermediate paths
    path = []  # List to store final sequence of directions 
    pathToCurrent = Stack()  # Queue to store direction to children (currState and pathToCurrent go hand in hand)
    currState = fringe.pop()
    while not subProblem.isGoalState(currState):
        if currState not in visited:
            visited.append(currState)    
            successors = subProblem.getSuccessors(currState)
            for next, direction in successors:
                fringe.push(next)
                tempPath = path + [direction]
                pathToCurrent.push(tempPath)
        if fringe.isEmpty():
            return False
        currState = fringe.pop()
        path = pathToCurrent.pop()
    return True

def solve(size, problem):
    # Initializing the color
    colors = problem.keys()
    colors = sorted(problem.keys())
    colorIndex = 0

    # Initialize the initial state of the grid
    grid = Grid(size, problem)

    # Initialize Problem specific variables
    currentPosition = None
    currentDirection = Directions.DEFAULT
    markedPositions = list()  # Stack
    visited = dict()
    for color in colors:
        visited[color] = list()
    
    # Initialize the start color and position
    activeColor = colors[colorIndex] 
    currentPosition = problem[activeColor][0]  

    # Local function to check whether all "to be" marked colors 
    # have a path from thier initial to final positions. 
    def checkIfAllColorsAreClear(inputGrid):
        tempColorIndex = colorIndex  # - 1
        allColorsAreClear = True  # True only when there is an obstruction
        # There is an obstruction even if one color does not have a path
        for ci in range(tempColorIndex, len(colors)):
            cc = colors[ci]
            ipcc = problem[cc][0]
            fpcc = problem[cc][1]
            od = inputGrid.getGridDictCopy()
            od.pop(fpcc)
            subProblem = SubProblem(inputGrid, cc, ipcc, fpcc, od)
            allColorsAreClear = allColorsAreClear and findIfAPathExists(subProblem)
        return allColorsAreClear

    # Loop until we find a solution to the problem
    while None in grid.getGridDict().values():
        # Initialize the start and final state of the current color
        initialActiveColorPosition = problem[activeColor][0]
        finalActiveColorPosition = problem[activeColor][1]
        # Define The Obstacle dictionary.
        currentObstacles = Grid.ObstructionDict(problem, grid, activeColor)
        currentPosDir = generateSuccessor(grid, currentPosition, currentDirection, currentObstacles)
        ######### Check the successor ############
        # if successor exists
        if currentPosDir is not None:
            currentPosition, currentDirection = currentPosDir
            # Check that the successor is neither Initial or Final Position of the current color
            if (not (currentPosition == finalActiveColorPosition)) and \
                    (not (currentPosition == initialActiveColorPosition)):
                grid.markGridPosition(currentPosition, activeColor)
                markedPositions.append((currentPosition, currentDirection))
                (visited[activeColor]).append(currentPosition)
        # If no successor found 
        else:
            # Backtrack
            # dead end condition         
            # If current color has no marked positions reverse the direction for the current position.
            # and continue with the search
            if 0 == len(visited[activeColor]):
                currentPosition = problem[activeColor][0]
                currentDirection = Directions.oppositeDirection(currentDirection)
            # Backtrack until a path to final position is found
            else:
                while True:
                    # Break Condition 1 : Backtracking led to unmarking all previously marked positions for all colors.
                    if (1 > len(markedPositions)):
                        currentPosition = problem[colors[0]][0]  # initial color's initial position
                        break
                    else:
                        # Break Condition 2 : Current Color has backtracked to its initial state.
                        if 0 == len(visited[activeColor]):
                            currentPosition = problem[activeColor][0]
                            break
                        tempCurrPosDir = markedPositions[len(markedPositions) - 1]
                        subProblemT = SubProblem(grid,
                                                 activeColor,
                                                 tempCurrPosDir[0], finalActiveColorPosition,
                                                 currentObstacles)
                        # Break Condition 3 : If Path to current colors final position is found
                        if findIfAPathExists(subProblemT):
                            currentPosition, currentDirection = tempCurrPosDir
                            break
                        # If All break conditions fail then pop from marked positions. 
                        currentPosition, currentDirection = markedPositions.pop()
                        visited[activeColor].remove(currentPosition)
                        currentObstacles.pop(currentPosition)
                        grid.unmarkGridPosition(currentPosition)
                
                currentDirection = Directions.oppositeDirection(currentDirection)
            continue

        # Check if the current position is the final position 
        # if yes increase the color index.
        if (currentPosition == finalActiveColorPosition):
            colorIndex += 1
            # If the color is the final color
            # Check if all positions are marked.
            # If not try to find a path for this color such that the grid is filled.
            # This part of the algortihm can be improved by selecting the longest available path. 
            if len(colors) == colorIndex and None in grid.getGridDict().values():
                currentDirection = Directions.oppositeDirection(currentDirection) 
                continue
            # If color is not the final color.
            else:
                # If any of remaining colors has no path
                # Backtrack until the paths open up
                if not checkIfAllColorsAreClear(grid):
                    tempColorIndex = colorIndex - 1
                    while (not checkIfAllColorsAreClear(grid)):
                        currentPosition, currentDirection = markedPositions.pop()
                        grid.unmarkGridPosition(currentPosition)
                        visited[activeColor].remove(currentPosition)

                    if (0 == len(visited[colors[tempColorIndex]])):
                        grid.unmarkGridPosition(currentPosition)
                        currentPosition = problem[colors[tempColorIndex]][0]
                        currentDirection = Directions.oppositeDirection(currentDirection)
                    else:
                        currentPosition, currentDirection = markedPositions[len(markedPositions) - 1]
                        currentDirection = Directions.oppositeDirection(currentDirection)
                    colorIndex -= 1
                    continue  
            activeColor = colors[colorIndex]
            currentPosition = problem[activeColor][0]
    # print visited
    return grid
