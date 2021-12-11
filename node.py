from board import Board

class Node:
    def __init__(self, board, parent=None, action=None):
        self.board = board
        self.parent = parent
        self.action = action
        if (self.parent != None):
            self.g = parent.g + 1
        else:
            self.g = 0
        print(self)

    @property 
    def path(self):
        node, p = self, []
        while node:
            p.append(node)
            node = node.parent
        return reversed(p)

    @property
    def solved(self):
        return self.board.solved

    @property
    def actions(self):
        return self.board.possible_moves

    @property
    def h(self):
        return self.board.manhattan

    @property
    def f(self):
        return self.h + self.g

    @property
    def state(self):
        return self.board.state