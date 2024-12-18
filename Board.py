import numpy as np

class Board(object):
    """Loads and updates the boardgame"""
    def __init__(self):
        super(Board, self).__init__()
        self.board = np.full((3,3), 0)
        self.board[0,0] = '2'
        self.board[0,1] = '2'
        self.board[0,2] = '2'
        self.board[2,0] = '1'
        self.board[2,1] = '1'
        self.board[2,2] = '1'

    def convertMove(self, move):
        try:
            frto = move.split(':')
            fr = list(map(int, frto[0].split(',')))
            to = list(map(int, frto[1].split(',')))
        except:
            return False
        return fr, to

    def updateBoard(self, fr, to):
        self.board[to[0],to[1]] = self.board[fr[0],fr[1]]
        self.board[fr[0],fr[1]] = 0

    def isMoveValid(self, fr, to, player):
        if to[1] == -1:
            return False
        if player == 0:
            if (fr[0] - to[0] == 1) and (fr[1] == to[1]):
                if self.board[to[0],to[1]] == 0:
                    return True
            if (fr[0] - to[0] == 1) and (abs(fr[1] - to[1]) == 1):
                if self.board[to[0],to[1]] != 0 and self.board[to[0],to[1]] != self.board[fr[0],fr[1]]:
                    return True
        elif player == 1:
            '''Test of forward move'''
            if (fr[0] - to[0] == -1) and (fr[1] == to[1]):
                if self.board[to[0],to[1]] == 0:
                    return True
            '''Test of capture movement'''
            if (fr[0] - to[0] == -1) and (abs(fr[1] - to[1]) == 1):
                if self.board[to[0],to[1]] != 0 and self.board[to[0],to[1]] != self.board[fr[0],fr[1]]:
                    return True
        return False

    def printBoard(self):
        print('    0   1   2  ')
        boardPieces = [' ', '#', '@']
        for i in range(3):
            print(f'{i} | {boardPieces[self.board[i,0]]} | {boardPieces[self.board[i,1]]} | {boardPieces[self.board[i,2]]}')

    def getBoardState(self):
        self.state = ''
        for i in range(3):
            for j in range(3):
                self.state += str(self.board[i,j])
        return self.state
