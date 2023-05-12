# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
from BFS import BFS
from DFS import DFS
from Astar import ASTAR
import time
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start = []
    goal = []
   #the program takes the initial state and goal state input by the user
    for i in range(3):
        a = list(map(int,input("Please enter row number " + str(i+1) + " for start state : ").strip().split()))[:3]
        start.append(a)
    for i in range(3):
        a = list(map(int,input("Please enter row number " + str(i+1) + " for goal state : ").strip().split()))[:3]
        goal.append(a)
    start = np.array(start)
    goal = np.array(goal)
    #the program asks the user which search algorithm he wants
    method = input("Please enter the name of the method, BFS, DFS or A*\n")
    if method == "A*":
        #the program asks the user whether he wants to continue wuth euclidean or manhattan
        heuristic = input("Please choose heuristic function, Euclidean or Manhattan\n")
        algorithm = ASTAR(start, goal, heuristic)
    if method == "BFS":
        algorithm = BFS(start, goal)
    if method == "DFS":
        algorithm = DFS(start, goal)
    #calculate the running time
    start_time = time.time()
    algorithm.puzzle()
    algorithm.print_path()
    print("--- %s seconds ---" % (time.time() - start_time))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
