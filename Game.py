import HexaPawn as hp
import os
from time import sleep


def clear():
	if os.name == 'nt':
		os.system('cls')
	elif os.name == 'posix':
		os.system('clear')
	print(initMessage)
	print(game.boardGame.printBoard())
	print('Total of games played: %i' % game.gamesPlayed)
	print('%s total wins: %i' % (game.humanName, game.humanWins))
	print('%s total wins: %i' % (game.cpuName, game.machineWins))

initMessage = '''
#################################################################################
#################################################################################
##                                                                             ##
##               _   _                ____                                     ##
##              | | | | _____  ____ _|  _ \\ __ ___      ___ __                 ##
##              | |_| |/ _ \\ \\/ / _` | |_) / _` \\ \\ /\\ / / '_ \\                ##       
##              |  _  |  __/>  < (_| |  __/ (_| |\\ V  V /| | | |               ##
##              |_| |_|\\___/_/\\_\\__,_|_|   \\__,_| \\_/\\_/ |_| |_|               ##
##                                                                             ##
##                                                                             ##
#################################################################################
#################################################################################
'''

humanName = input('What\'s your name, human? ')
cpuName = input('What machine would you like to play? ')

game = hp.HexaPawn(humanName,cpuName)
game.startNewGame()

while True:
	clear()
	if game.playerToMove == 0:
		humanMove = input('Play your move, %s [format: row,col:row,col]: ' % game.humanName)
		convertedMove = game.boardGame.convertMove(humanMove)
		if not convertedMove:
			print('Invalid move format. Try again!')
			sleep(5)
			continue
		if game.makeMove(convertedMove[0], convertedMove[1]):
			if game.checkWin():
				game.humanWins += 1
				game.machine.learn(False)
				clear()
				print('\n%s, you have won this game! %s has learnd from its mistakes!' % (game.humanName. game.cpuName))
				print('%s has %i victories.' % (game.humanName, game.humanWins))
				print('%s has %i victories.' % (game.cpuName, game.machineWins))
				sleep(5)
				game.newGeneration()
			else:
				game.playerToMove = (game.playerToMove + 1) % 2
				game.round += 1
		else:
			print('Invalid move! Try again!')
			sleep(5)
			continue
	else:
		machineMove = game.machine.chooseMove(game.boardGame.getBoardState(), game.round)
		convertedMachineMove = game.boardGame.convertMove(machineMove)
		game.boardGame.updateBoard(convertedMachineMove[0], convertedMachineMove[1])
		print(convertedMachineMove)
		sleep(3)
		if game.checkWin():
			game.machineWins += 1
			game.machine.learn(True)
			clear()
			print('\n%s has won this game! It\'s learning!' % game.cpuName)
			print('%s has %i victories.' % (game.humanName, game.humanWins))
			print('%s has %i victories.' % (game.cpuName, game.machineWins))
			sleep(5)
			game.newGeneration()
		else:
			game.playerToMove = (game.playerToMove + 1) % 2
			game.round += 1
