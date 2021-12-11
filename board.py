from random import shuffle

class Board():
    def __init__(self, state, white, rows, cols):
        self.rows = rows
        self.cols = cols
        self.state = state
        self.white = white
        self.solved_state = [[1,8,7],
                        [2,'',6],
                        [3,4,5]]

    @property
    def possible_moves(self):
        moves=[]
        if self.white[0]!=0:
            moves.append('LEFT')
        if self.white[0]!=self.cols -1:
            moves.append('RIGHT')
        if self.white[1]!=0:
            moves.append('UP')
        if self.white[1]!=self.rows-1:
            moves.append('DOWN')
        return moves
    
    @property
    def manhattan(self):
            distance = 0
            for i in range(self.cols):
                for j in range(self.rows):
                    (x1, y1)= self.find(self.state[i][j], self.state)
                    (x2, y2)= self.find(self.state[i][j], self.solved_state)
                    distance += abs(x2 - x1) + abs(y2 - y1)
            return distance

    @property
    def solved(self):
        resolved = False
        if self.state == self.solved_state:
            resolved = True
        return resolved

    def move(self, direction):
        (i,j)= self.white
        if direction=='UP': 
            if j!=0:
                self.state[i][j]=self.state[i][j-1]
                self.state[i][j-1]=""
                self.white=(i, j-1)
        elif direction=='DOWN':
            if j!=len(self.state)-1:
                self.state[i][j]=self.state[i][j+1]
                self.state[i][j+1]=""
                self.white=(i, j+1)
        elif direction=='LEFT':
            if i!=0:
                self.state[i][j]=self.state[i-1][j]
                self.state[i-1][j]=""
                self.white=(i-1,j)
        elif direction=='RIGHT':
            if i!=len(self.state)-1:
                self.state[i][j]=self.state[i+1][j]
                self.state[i+1][j]=""
                self.white=(i+1,j)

    def find(self, element, state):
        for i in range(self.rows):
            for j in range(self.cols):
                if state[i][j] == element:
                    return (i, j)

    def copy(self):
        copy = [[0 for i in range(self.cols)] for j in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                copy[i][j]=self.state[i][j]
        return copy

    def shuffle_b(self):
        shuffle_list = [1, 2, 3, 4, 5, 6, 7, 8, '']
        k=0
        shuffle(shuffle_list)  
        for i in range(self.rows):
            for j in range(self.cols):
                self.state[i][j]=shuffle_list[k]
                k=k+1
        self.white = self.find('', self.state)

    def draw_b(self):
        for i in range(3):
            for j in range(3):
                stroke(255)
                if self.state[i][j]=='':
                    fill(221, 160, 221)
                    rect(i*100, j*100, 100, 100)
                else:
                    fill(0)
                    rect(i*100, j*100, 100, 100)
                textSize(30)
                textAlign(CENTER)
                fill(221, 160, 221)
                text(str(self.state[i][j]), (i*100)+50, (j*100)+50)
