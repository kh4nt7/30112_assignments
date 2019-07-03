__author__ = "Khaing Myel Khant"

def printline():
	print('-' * 15)

def drawBoard(array):
	printline()
	for l in array:
		print("| ",end="")
		for e in l:
			if e == "1":
				print(" X |", end="")
			elif e == "0":
				print(" O |", end="")
			else:
				print("   |", end="")
		print()
		printline()

stage = [["1","0","1"], ["0", None, "1"], [None, None, None]]

winstage = [
	# Horizonal 1
	[stage[0][0], stage[0][1], stage[0][2]],
	# Horizonal 2
	[stage[1][0], stage[1][1], stage[1][2]],
	# Horizonal 3
	[stage[2][0], stage[2][1], stage[2][1]],

	# Vertical 1
	[stage[0][0], stage[1][0], stage[2][0]],
	# Vertical 2
	[stage[0][1], stage[1][1], stage[2][1]],
	# Vertical 3
	[stage[0][2], stage[1][2], stage[2][2]],

	# Cross 1
	[stage[0][0], stage[1][1], stage[2][2]],

	# Cross 2
	[stage[0][2], stage[1][1], stage[2][0]]
]

def checkSpace(l):
	flag = False
	for i in l:
		if None in l:
			flag = True
	return flag

def checkWin(l):
	flag = False
	for i in l:
		if i in winstage:
			flag = True
			return flag
	return flag

if __name__ == '__main__':
	print("Welcome to tictactoe game!")
	