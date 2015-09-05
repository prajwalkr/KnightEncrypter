from os.path import *
def get_sequences(x = 3,y = 10):
	global sequences,limit
	sequences = []
	for i in range(x):
		for j in range(y):
			board = [[-1 for l in range(y)] for m in range(x)]
			tour(board,i,j,1)
	f = open(join(dirname(__file__),'tours.txt'),'w')
	for s in sequences:
		a = " ".join(str(x) for x in s) + '\n'
		f.write(a)
	def tour(board,i,j,move):
		if i < 0 or j < 0 or i >= x or j >= y:
			return
		if board[i][j] != -1:
			return
		if move == x*y:
			board[i][j] = move
			process_board(board)
			board[i][j] = -1
			return
		board[i][j] = move
		move += 1
		temp = [board for _ in range(8)]
		tour(temp[0],i+1,j+2,move)
		tour(temp[1],i+1,j-2,move)
		tour(temp[2],i-1,j+2,move)
		tour(temp[3],i-1,j-2,move)
		tour(temp[4],i+2,j+1,move)
		tour(temp[5],i+2,j-1,move)
		tour(temp[6],i-2,j+1,move)
		tour(temp[7],i-2,j-1,move)
		board[i][j] = -1

	def process_board(board):
		seq = [-1 for _ in range(x*y)]
		for i in range(x):
			for j in range(y):
				seq[board[i][j] - 1] = i*y + j
		sequences.append(seq)

