import Board as b
import Machine as m


class HexaPawn(object):
	"""Creates a new learning game"""
	def __init__(self, humanName='Human', cpuName='Machine'):
		super(HexaPawn, self).__init__()
		self.humanName = humanName
		self.cpuName = cpuName
		self.machine = m.Machine()

	def startNewGame(self):
		self.gamesPlayed = 0
		self.playerToMove = 0
		self.humanWins = 0
		self.machineWins = 0
		self.round = 1
		self.boardGame = b.Board()
		self.machineTable = self.machine.loadNew()

	def newGeneration(self):
		self.gamesPlayed += 1
		self.playerToMove = 0
		self.boardGame = b.Board()
		self.round = 1

	def makeMove(self, fr, to):
		if self.boardGame.isMoveValid(fr, to, self.playerToMove):
			self.boardGame.updateBoard(fr, to)
			return True
		else:
			return False

	def checkWin(self):
		if ((1 in self.boardGame.board[0]) or (2 not in self.boardGame.board)) or ((2 in self.boardGame.board[2]) or (1 not in self.boardGame.board)):
			return True

		for i in range(3):
			for j in range(3):
				if self.boardGame.board[i,j] != 0:
					try:	
						if self.playerToMove == 0 and self.boardGame.board[i,j] == 2:
							for col in [-1,0,1]:
								if self.boardGame.isMoveValid([i,j],[i+1,j+col], self.playerToMove + 1):
									return False
						elif self.playerToMove == 1 and self.boardGame.board[i,j] == 1:
							for col in [-1,0,1]:
								if self.boardGame.isMoveValid([i,j],[i-1,j+col], self.playerToMove - 1):
									return False
					except IndexError:
						pass
		return True
