from Board import Board
import numpy as np
from Puzzle import Puzzle
#Implmentation by heap
#inherit everything from the puzzle class
class ASTAR(Puzzle):
    # initialization
    def __init__(self, start, goal, heuristic_name):
        super().__init__(start, goal)
        self.final = None     #we initialize it with none because we still didn't reach to the goal
        self.path = []        #the array will be filled when we reach to the goal
        self.actions = [self.up, self.down, self.right, self.left]     #array from functions to loop on each action
        self.heuristic_name = heuristic_name

    def puzzle(self):
        heuristic = self.heuristic(self.start, self.heuristic_name)
        board = Board(self.start, None, None, 0, heuristic)
        boards = [board]      #unexplored boards(still didn't generate from it)
        while True:
            curr_board = boards.pop(self.get_next(boards))  #to get from boards the index that has the board with least cost
            curr_state = curr_board.state                 #to get the 2D array inside the board
            if self.solved(curr_state, self.goal):         #if i reached the goal
                self.final = curr_board
                return
            x, y = self.emptycell(curr_state)              #to get the empty tile
            for action in self.actions:                    #will loop on the 4 actions
                result = action(np.copy(curr_state), x, y)    #(np.copy) will send a copy from the state
                if result is False:
                    continue                             #skip this action and do the next action
                new_state, move, valid = result
                if not self.explored(new_state):
                    if self.max_depth < curr_board.cost + 1:
                        self.max_depth = curr_board.cost + 1

                        #the last parameter gets the heuristic of the new state
                    new_board = Board(new_state, curr_board, move, curr_board.cost + 1, self.heuristic(new_state, self.heuristic_name))
                    boards.append(new_board)
                    self.explored_states.append(new_state)





