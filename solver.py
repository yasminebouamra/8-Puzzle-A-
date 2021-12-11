import itertools
import collections
from node import Node 
from board import Board
class Solver:

    def __init__(self, start):
        self.start = start

    def solve(self):
        seen = []
        children = [Node(self.start)]
        seen.append(children[0].state)
        racine = children[0]
        while(children):
            racine = children.pop(0)
            if(not racine.solved):
                for direction in racine.actions:
                    fils=[]
                    new_state = Board(racine.board.copy(), racine.board.white, racine.board.cols, racine.board.rows)
                    new_state.move(direction)
                    child = Node(new_state, racine, direction)
                    if child.state not in seen:
                        seen.append(child.state)
                        fils.append(child)
                sorted(fils, key=lambda node: node.f)
                for val in fils:
                    children.append(val)
            else:
                print(racine.path)
                return racine.path
