import math

import numpy as np


class Puzzle(object):
    #constructor
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal
        self.explored_states = [self.start]
        self.goal_empty = self.emptycell(goal)
        self.i, self.j = self.goal_empty
        self.cost_path = 0
        self.max_depth = 0

    #The 4 actions
    def up(self, state, i, j):
        if i - 1 < 0:
            return False
        temp = state[i][j]
        state[i][j] = state[i - 1][j]
        state[i - 1][j] = temp
        return state, "Up", True

    def down(self, state, i, j):
        if i + 1 > 2:
            return False
        temp = state[i][j]
        state[i][j] = state[i + 1][j]
        state[i + 1][j] = temp
        return state, "Down", True

    def left(self, state, i, j):
        if j - 1 < 0:
            return False
        temp = state[i][j]
        state[i][j] = state[i][j - 1]
        state[i][j - 1] = temp
        return state, "Left", True

    def right(self, state, i, j):
        if j + 1 > 2:
            return False
        temp = state[i][j]
        state[i][j] = state[i][j + 1]
        state[i][j + 1] = temp
        return state, "Right", True

    #find the index of the empty tile
    def emptycell(self, state):
        for i in range(len(state)):
            for j in range(len(state[0])):
                if state[i][j] == 0:
                    return i, j

    #check whether we reached to the goal or not
    def solved(self, state, goal):
        if (state == goal).all():
            return True
        return False

    #check whether we visited this state before or no
    def explored(self, state):
        for i in self.explored_states:
            if np.array_equiv(i, state):
                return True
        return False

    #for A* containing 2 methods(Euclidean,Manhattan)
    def heuristic(self, state, name):
        i, j = self.emptycell(state)
        if name == "Euclidean":
            return math.sqrt((i - self.i) ** 2 + (j - self.j) ** 2)
        return math.fabs(i - self.i) + math.fabs(j - self.j)

    #get the least cost of the boards
    def get_next(self, boards):
        min_board = 0
        for i in range(1, len(boards)):
            if boards[i].total < boards[min_board].total:
                min_board = i
        return min_board

    #take the final puzzle that we reached and go backward till the start puzzle
    # then will put all the boards in array.take the final puzzle that we reached and go backward till the start puzzle
    # then will put all the boards in array.
    def generate_path(self):
        board = self.final
        self.cost_path = board.cost
        while True:
            self.path.insert(0, board)
            board = board.previous_board
            if board.direction is None:
                break

    #takes array from generate path and print it
    def print_path(self):
        self.generate_path()
        print(self.start)
        for board in self.path:
            print(board.direction)
            print(board.state)
        print("Cost of path is ", self.cost_path)
        print("Maximum depth reached ", self.max_depth)
