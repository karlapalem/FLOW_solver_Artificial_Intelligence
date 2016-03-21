# Import the FlowSolver (solution) file
from FlowSolver import *

# Test Cases:

problem2 = {"A":[(0, 1) , (1, 1)]}
# [   ] [   ]
# [ A ] [ A ]
print "problem2"
Grid(2, problem2).printGrid()
print "Solved problem2"
grid = solve(2, problem2)
grid.printGrid()
print


problem3 = {"A":[(0, 0) , (2, 2)]}
# [ A ] [   ] [   ]
# [   ] [   ] [   ]
# [   ] [   ] [ A ]
print "problem3"
Grid(3, problem3).printGrid()
print "Solved problem3"
grid = solve(3, problem3)
grid.printGrid()
print
 
problem3a = {"A":[(0, 0) , (2, 2)], "B":[(1, 1) , (1, 2)]}
# [ A ] [   ] [   ]
# [   ] [ B ] [   ]
# [   ] [ B ] [ A ]
print "problem3a"
Grid(3, problem3a).printGrid()
print "Solved problem3a"
grid = solve(3, problem3a)
grid.printGrid()
print
 
problem3b = {"A":[(0, 0) , (1, 2)], "B":[(1, 1) , (0, 2)]}
# [ A ] [   ] [   ]
# [   ] [ B ] [   ]
# [ B ] [ A ] [   ]
print "problem3b"
Grid(3, problem3b).printGrid()
print "Solved problem3b"
grid = solve(3, problem3b)
grid.printGrid()
print
 
nextcomplexProblem3a = {"A" : [(0, 0), (2, 2)], "B": [(0, 1), (0, 2)]}
# [ A ] [   ] [   ]
# [ B ] [   ] [   ]
# [ B ] [   ] [ A ]
print "nextcomplexProblem3a"
Grid(3, nextcomplexProblem3a).printGrid()
print "Solved nextcomplexProblem3a"
grid = solve(3, nextcomplexProblem3a)
grid.printGrid()
print
 
nextcomplexProblem3b = {"A" : [(0, 0), (0, 2)], "B": [(2, 0), (1, 2)]}
# [ A ] [   ] [ B ]
# [   ] [   ] [   ]
# [ A ] [ B ] [   ]
print "nextcomplexProblem3b"
Grid(3, nextcomplexProblem3b).printGrid()
print "Solved nextcomplexProblem3b"
grid = solve(3, nextcomplexProblem3b)
grid.printGrid()
print
 
 
prob4 = {"A":[(0, 0), (3, 0)]}
# [ A ] [   ] [   ] [ A ]
# [   ] [   ] [   ] [   ]
# [   ] [   ] [   ] [   ]
# [   ] [   ] [   ] [   ]
print "prob4"
Grid(4, prob4).printGrid()
print "Solved prob4"
grid = solve(4, prob4)
grid.printGrid()
print
 
problem4 = {"A":[(0, 0), (3, 3)], "B":[(2, 1), (1, 3)], "C":[(0, 3), (1, 2)]}
# [ A ] [   ] [   ] [   ]
# [   ] [   ] [ B ] [   ]
# [   ] [ C ] [   ] [   ]
# [ C ] [ B ] [   ] [ A ]
print "problem4"
Grid(4, problem4).printGrid()
print "Solved problem4"
grid = solve(4, problem4)
grid.printGrid()
print
 
problemtest4a = {"A":[(0, 0), (1, 2)], "B":[(1, 0), (0, 3)], "C":[(2, 0), (3, 3)]}
# [ A ] [ B ] [ C ] [   ]
# [   ] [   ] [   ] [   ]
# [   ] [ A ] [   ] [   ]
# [ B ] [   ] [   ] [ C ]
print "problemtest4a"
Grid(4, problemtest4a).printGrid()
print "Solved problemtest4a"
grid = solve(4, problemtest4a)
grid.printGrid()
print
 
problemtest4b = {"A":[(0, 0), (1, 2)], "B":[(1, 0), (2, 1)], "C":[(2, 0), (3, 3)], "D":[(2, 2), (0, 3)]}
# [ A ] [ B ] [ C ] [   ]
# [   ] [   ] [ B ] [   ]
# [   ] [ A ] [ D ] [   ]
# [ D ] [   ] [   ] [ C ]
print "problemtest4b"
Grid(4, problemtest4b).printGrid()
print "Solved problemtest4b"
grid = solve(4, problemtest4b)
grid.printGrid()
print
 
problemtest4c = {"A":[(0, 0) , (1, 2)], "B":[(0, 1) , (2, 3)], "C":[(2, 2) , (3, 0)], "D":[(3, 1) , (3, 3)]}
# [ A ] [   ] [   ] [ C ]
# [ B ] [   ] [   ] [ D ]
# [   ] [ A ] [ C ] [   ]
# [   ] [   ] [ B ] [ D ]
print "problemtest4c"
Grid(4, problemtest4c).printGrid()
print "Solved problemtest4c"
grid = solve(4, problemtest4c)
grid.printGrid()
print
 
concentricProblem4 = {"A" : [(0, 0), (1, 2)]}
# [ A ] [   ] [   ] [   ]
# [   ] [   ] [   ] [   ]
# [   ] [ A ] [   ] [   ]
# [   ] [   ] [   ] [   ]
print "concentricProblem4"
Grid(4, concentricProblem4).printGrid()
print "Solved concentricProblem4"
grid = solve(4, concentricProblem4)
grid.printGrid()
print
 

problem5 = {"A":[(0, 0) , (1, 4)], "B":[(2, 0) , (1, 3)], "C":[(2, 1) , (2, 4)], "D":[(4, 0) , (3, 3)], "E":[(3, 4) , (4, 1)]}
# [ A ] [   ] [ B ] [   ] [ D ]
# [   ] [   ] [ C ] [   ] [ E ]
# [   ] [   ] [   ] [   ] [   ]
# [   ] [ B ] [   ] [ D ] [   ]
# [   ] [ A ] [ C ] [ E ] [   ]
print "problem5"
Grid(5, problem5).printGrid()
print "Solved problem5"
grid = solve(5, problem5)
grid.printGrid()
print
 
problem5a = {"A":[(0, 0) , (1, 2)], "B":[(0, 1) , (2, 3)], "C":[(2, 2) , (4, 0)], "D":[(0, 4) , (3, 2)], "E":[(3, 1) , (4, 4)]}
# [ A ] [   ] [   ] [   ] [ C ]
# [ B ] [   ] [   ] [ E ] [   ]
# [   ] [ A ] [ C ] [ D ] [   ]
# [   ] [   ] [ B ] [   ] [   ]
# [ D ] [   ] [   ] [   ] [ E ]
print "problem5a"
Grid(5, problem5a).printGrid()
print "Solved problem5a"
grid = solve(5, problem5a)
grid.printGrid()
print
 
prob5 = {"A":[(0, 0), (4, 4)]}
# [ A ] [   ] [   ] [   ] [   ]
# [   ] [   ] [   ] [   ] [   ]
# [   ] [   ] [   ] [   ] [   ]
# [   ] [   ] [   ] [   ] [   ]
# [   ] [   ] [   ] [   ] [ A ]
print "prob5"
Grid(5, prob5).printGrid()
print "Solved prob5"
grid = solve(5, prob5)
grid.printGrid()
print
 
prob5a = {"A":[(0, 0), (4, 4)], "B":[(1, 0), (1, 3)], "C":[(2, 0), (2, 3)], "D":[(3, 0), (3, 3)], "E":[(4, 0), (4, 3)]}
# [ A ] [ B ] [ C ] [ D ] [ E ]
# [   ] [   ] [   ] [   ] [   ]
# [   ] [   ] [   ] [   ] [   ]
# [   ] [ B ] [ C ] [ D ] [ E ]
# [   ] [   ] [   ] [   ] [ A ]
print "prob5a"
Grid(5, prob5a).printGrid()
print "Solved prob5a"
grid = solve(5, prob5a)
grid.printGrid()
print
 
problem6 = {"A":[(0, 0), (5, 0)]}
# [ A ] [   ] [   ] [   ] [   ] [ A ]
# [   ] [   ] [   ] [   ] [   ] [   ]
# [   ] [   ] [   ] [   ] [   ] [   ]
# [   ] [   ] [   ] [   ] [   ] [   ]
# [   ] [   ] [   ] [   ] [   ] [   ]
# [   ] [   ] [   ] [   ] [   ] [   ]
print "problem6"
Grid(6, problem6).printGrid()
print "Solved problem6"
grid = solve(6, problem6)
grid.printGrid()
print
 
prob7 = {"A" : [(0, 0), (6, 6)]}
# [ A ] [   ] [   ] [   ] [   ] [   ] [   ]
# [   ] [   ] [   ] [   ] [   ] [   ] [   ]
# [   ] [   ] [   ] [   ] [   ] [   ] [   ]
# [   ] [   ] [   ] [   ] [   ] [   ] [   ]
# [   ] [   ] [   ] [   ] [   ] [   ] [   ]
# [   ] [   ] [   ] [   ] [   ] [   ] [   ]
# [   ] [   ] [   ] [   ] [   ] [   ] [ A ]
print "prob7"
Grid(7, prob7).printGrid()
print "Solved prob7"
grid = solve(7, prob7)
grid.printGrid()
print
