# HexaPawnGame
A Python implementation of the game Hexapawn, described in the "Mathematical Games" section of the American Scientific magazine, March, 1962.

As described by Gardner, the goal of the game is to show how to build a machine that can learn from its mistakes, as well as with its victories, because it learns the good  if it loses or wins a round, respectively.

As you play the machine, you can see that at first, it makes really bad moves. But as the rounds go by, it starts to learn which moves are bad, discarting them, and which are good, keeping it as the only possible move for the current board configuration.

http://cs.williams.edu/~freund/cs136-073/GardnerHexapawn.pdf

# How to play the game
This game is a very simplified version of chess, containing only three pawns for each player and it's played on a 3x3 board, where the pawns initially ocupy the first and last rows of the board.

| * | * | * |  
|    |   |    |  
| * | * | * |  

A human plays against a machine and the machine initially does not know how to play the game. The human always plays first and they alternate their moves, which are identical to the pawn moves on a traditional chess game, except for the fact that thare is no pawn promotion, no en passant and there is no option for moving two squares forward on the first movement of each pawn.

The game objective is to win by placing one of your pawns on the opposite extreme row (the initial row of your opponent), taking all of your opponent pawns or by leaving him with no legal moves on his next move.

As you play, whether the machine wins or loses, it learns by knowing which moves led to its win/loss. If it wins, it keeps the winning move and discards all of the other moves from the winning position. This is ther "reward" it gets by winning the reound. If it loses, it discards the last move, which is the one that allowed the loss. This is the "punishment" it gets for its loss.

This way, after a few games played, it starts to play more and more moves that are not leading to a defeat, until it plays perfectly.
