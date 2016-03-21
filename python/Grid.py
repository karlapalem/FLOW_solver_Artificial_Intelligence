class Grid:
    def __init__(self, size, problem):
        self.size = size
        self.problem = problem
        self.gridDict = dict()
        self.initializeGrid()
    
    def generateGridKeys(self):
        gridKeys = list()
        for row in range(self.size):
            for column in range(self.size):
                gridKeys.append((row, column))
        return gridKeys
    
    def initializeGrid(self):
        for key in self.generateGridKeys():
            self.gridDict[key] = None
        for color in self.problem.keys():
            for position in self.problem[color]:
                self.gridDict[position] = color
    
    def markGridPosition(self, position, color):
        allInitialAndFinalPositions = list()
        for c in self.problem.keys():
            for pos in self.problem[c]:
                allInitialAndFinalPositions.append(pos)
        if position not in allInitialAndFinalPositions:
            self.gridDict[position] = color
        return self.gridDict

    def unmarkGridPosition(self, position):
        allInitialAndFinalPositions = list()
        for c in self.problem.keys():
            for pos in self.problem[c]:
                allInitialAndFinalPositions.append(pos)
        if position not in allInitialAndFinalPositions:
            self.gridDict[position] = None
        return self.gridDict

    def printGrid(self):
        for row in range(self.size):
            for column in range(self.size):
                if self.gridDict[(column, row)] == None:
                    print "[   ]",
                else:
                    print "[", self.gridDict[(column, row)], "]",
            print

    def getGridSize(self):
        return self.size
    
    def getGridDict(self):
        return self.gridDict
    
    def getGridDictCopy(self):
       return self.gridDict.copy()
    
    @staticmethod
    # Given a grid and a color returns the obstacle dictionary.
    def ObstructionDict(problem, grid, color):
        finalColorPosition = problem[color][1]
        obst = grid.getGridDictCopy()
        if finalColorPosition in obst.keys():
            obst.pop(finalColorPosition)
        return obst
