
import random as rand
class Board(object):
	"""
	Internal representation of the board,
	grid is a list of board rows, where
	'True' represents a mine 
	"""
	def __init__(self,nrows,ncols,mines):
		# Initialize grid
		grid = [[False]*ncols]*nrows
		i = 0
		while (i<mines):
			rowPlacement = rand.randint(0,rows-1)
			colPlacement = rand.randint(0,cols-1)
			if (!grid[rowPlacement][colPlacement]):
				grid[rowPlacement][colPlacement] = True
				i+=1

	def getCell(self, x, y)
   		if grid[y] and grid[y][x]:
			return 9
		bombs = 0
		for x0 in range(-1, 2):
			for y0 in range (-1, 2):
				if grid[y + y0] and grid[y + y0][x + x0]:
					bombs+=1
		return bombs
