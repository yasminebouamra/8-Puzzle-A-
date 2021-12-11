from board import Board
from node import Node
from solver import Solver
import time

cols = 3
rows = 3
current_state = [[1,8,7],
              [2,'',6],
              [3,4,5]]
white = (1,1)
board = Board(current_state, white, cols, rows)
            
def setup():
    global cols
    global rows
    size(cols*100, rows*100+100)
    background(0)
    textSize(12)
    textAlign(CENTER)
    fill(0, 408, 612)
    text("Utilisez les fleches pour melanger manuellement", 150, 325)
    text("Utilisez entrer pour melanger automatiquement", 150, 350)

def draw():
    global board
    board.draw_b()
    
def keyPressed():
    global board
    (i,j)= board.white
    if key == CODED:
        if keyCode==UP: 
            board.move('UP')
        elif keyCode==DOWN:
            board.move('DOWN')
        elif keyCode==LEFT:
            board.move('LEFT')
        elif keyCode==RIGHT:
            board.move('RIGHT')
    if key==ENTER:
        board.shuffle_b()
    if key==TAB:
        s = Solver(board)
        tic = time.clock()
        p = s.solve()
        toc = time.clock()

        steps = 0
        print(p)
        for node in p:
            print(node.action)
            board=node.board
            steps += 1
        print(toc)
