# Import the grid file
from Grid import *

class Stack:
    "A container with a last-in-first-out (LIFO) queuing policy."
    def __init__(self):
        self.list = []

    def push(self, item):
        "Push 'item' onto the stack"
        self.list.append(item)

    def pop(self):
        "Pop the most recently pushed item from the stack"
        return self.list.pop()

    def isEmpty(self):
        "Returns true if the stack is empty"
        return len(self.list) == 0

class Directions:
    NORTH, SOUTH, EAST, WEST = "n", "s", "e", "w"
    DEFAULT = SOUTH
    @staticmethod
    def rotateDirectionClockwise(direction):
        if Directions.NORTH == direction:
            return Directions.EAST
        if Directions.SOUTH == direction:
            return Directions.WEST
        if Directions.EAST == direction:
            return Directions.SOUTH
        if Directions.WEST == direction:
            return Directions.NORTH
    @staticmethod
    def rotateDirectionCounterClockwise(direction):
        if Directions.NORTH == direction:
            return Directions.WEST
        if Directions.SOUTH == direction:
            return Directions.EAST
        if Directions.EAST == direction:
            return Directions.NORTH
        if Directions.WEST == direction:
            return Directions.SOUTH
    @staticmethod
    def oppositeDirection(direction):
        if Directions.NORTH == direction:
            return Directions.SOUTH
        if Directions.SOUTH == direction:
            return Directions.NORTH
        if Directions.EAST == direction:
            return Directions.WEST
        if Directions.WEST == direction:
            return Directions.EAST

class SubProblem:
    def __init__(self, grid, color, initialPos, finalPos, obstacleDict):
        self.grid = grid
        self.color = color
        self.initialPos = initialPos
        self.finalPos = finalPos
        self.obstacleDict = obstacleDict
    
    def getStartState(self):
        return self.initialPos
    
    def isGoalState(self, pos):
        return (self.finalPos == pos)

    def getSuccessors(self, position):
        return generateValidSuccessorDirections(self.grid, position, self.obstacleDict)


 ### SOME UTILITY FUNCTIONS ###
    
def generateValidSuccessorDirections(grid, position, obstacleDict):
    possibleSuccessorsAndDirections = dict()
    possibleSuccessorsAndDirections[(position[0] + 1, position[1])] = Directions.EAST
    possibleSuccessorsAndDirections[(position[0] - 1, position[1])] = Directions.WEST
    possibleSuccessorsAndDirections[(position[0], position[1] + 1)] = Directions.SOUTH
    possibleSuccessorsAndDirections[(position[0], position[1] - 1)] = Directions.NORTH
    successors = []
    obstaclePositions = []  # [key for key in obstacleDict.keys() if obstacleDict[key] is not None]
    for key in obstacleDict.keys():
        if obstacleDict[key] is not None:
            obstaclePositions.append(key)
    for successor in possibleSuccessorsAndDirections.keys():
        if successor in grid.generateGridKeys() and successor not in obstaclePositions:
            successors.append((successor, possibleSuccessorsAndDirections[successor]))
    return successors

def generateSuccessor(grid, position, direction, obstacleDict):
    def successorInAParticularDirection(p, d):
        s = None
        if d == Directions.NORTH:
            s = (p[0], p[1] - 1)
        elif d == Directions.EAST:
            s = (p[0] + 1, p[1])
        elif d == Directions.SOUTH:
            s = (p[0], p[1] + 1)
        elif d == Directions.WEST:
            s = (p[0] - 1, p[1])
        return s
    def isSuccessorSatisfactory(p, o):
        obstaclePositions = []
        for key in o.keys():
            if o[key] is not None:
                obstaclePositions.append(key)
        if p in grid.generateGridKeys():
            if p not in obstaclePositions:
                return True
            else:
                return False
        else:
            return False
    sameDirectionSuccessor = successorInAParticularDirection(position, direction)
    clockwiseSuccessor = successorInAParticularDirection(position, Directions.rotateDirectionClockwise(direction))
    counterClockwiseSuccessor = successorInAParticularDirection(position, Directions.rotateDirectionCounterClockwise(direction))
    if isSuccessorSatisfactory(sameDirectionSuccessor, obstacleDict):
        return (sameDirectionSuccessor, direction)
    elif isSuccessorSatisfactory(clockwiseSuccessor, obstacleDict):
        return (clockwiseSuccessor, Directions.rotateDirectionClockwise(direction))
    elif isSuccessorSatisfactory(counterClockwiseSuccessor, obstacleDict):
        return (counterClockwiseSuccessor, Directions.rotateDirectionCounterClockwise(direction))
    else:
        return None
