#contains some variables
class Board(object):
    def __init__(self, state, previous_board, direction, cost, heuristic):
        self.state = state
        self.previous_board = previous_board
        self.direction = direction
        self.cost = cost
        self.heuristic = heuristic
        self.total = self.cost + self.heuristic
