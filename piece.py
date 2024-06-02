import pygame

class Piece():

	def __init__(self, color, value):
		self.value = value
		self.color = color
		self.forbiddenCoords = [(4,2), (5,2), (4,3), (5,3), (4,6), (5,6), (4,7), (5,7)]

	def getMoves(self, row, col, board):
		moves = []
		if self.value == 'b' or self.value == 'f':
			#bomb and flag movement
			pass
		elif self.value == 9:
			running = True
			x = 1
			while running:
				if col+x > 9 or (row, col+x) in self.forbiddenCoords:
					running = False
				elif board[row][col+x].color != self.color:
					if board[row][col+x].color != None:
						moves.append((row, col+x))
						running = False
					else:
						moves.append((row, col+x))
						x += 1
				else:
					running = False

			running = True
			x = 1
			while running:
				if col-x < 0 or (row, col-x) in self.forbiddenCoords:
					running = False
				elif board[row][col-x].color != self.color:
					if board[row][col-x].color != None:
						moves.append((row, col-x))
						running = False
					else:
						moves.append((row, col-x))
						x += 1
				else:
					running = False

			running = True
			y = 1
			while running:
				if row+y > 9 or (row+y, col) in self.forbiddenCoords:
					running = False
				elif board[row+y][col].color != self.color:
					if board[row+y][col].color != None:
						moves.append((row+y, col))
						running = False
					else:
						moves.append((row+y, col))
						y += 1
				else:
					running = False

			running = True
			y = 1
			while running:
				if row-y < 0 or (row-y, col) in self.forbiddenCoords:
					running = False
				elif board[row-y][col].color != self.color:
					if board[row-y][col].color != None:
						moves.append((row-y, col))
						running = False
					else:
						moves.append((row-y, col))
						y += 1
				else:
					running = False

		else:
			#everyone else
			for i in range(4):
				if i == 0 and row+1 <= 9 and row+1 >= 0:
					if board[row+1][col].color != self.color:
						moves.append((row+1, col))
				elif i == 1 and col+1 <= 9 and col+1 >= 0:
					if board[row][col+1].color != self.color:
						moves.append((row, col+1))
				elif i == 2 and row-1 <= 9 and row-1 >= 0:
					if board[row-1][col].color != self.color:
						moves.append((row-1, col))
				elif i == 3 and col-1 <= 9 and col-1 >= 0:
					if board[row][col-1].color != self.color:
						moves.append((row, col-1))
			pass

		for i in moves:
			if i in self.forbiddenCoords:
				moves.remove(i)


		return moves

	def move(self, board, initialCoords=tuple, finalCoords=tuple):
		board[initialCoords[0]][initialCoords[1]] = Piece(None, 0)
		board[finalCoords[0]][finalCoords[1]] = Piece(self.color, self.value)

	def attack(self, board, pos, attackingPos):
		attackedPiece = board[attackingPos[0]][attackingPos[1]]
		if attackedPiece.value == 0:
			self.move(board, pos, attackingPos)
		elif type(attackedPiece.value) == int and type(self.value) == int: 
			if attackedPiece.value > self.value:
				self.move(board, pos, attackingPos)
			elif attackedPiece.value < self.value:
				board[pos[0]][pos[1]] = Piece(None, 0)
			elif attackedPiece.value == self.value:
				board[pos[0]][pos[1]] = Piece(None, 0)
				board[attackingPos[0]][attackingPos[1]] = Piece(None, 0)
		elif attackedPiece.value == 's':
			self.move(board, pos, attackingPos)
		elif attackedPiece.value == 'b' and self.value != 8:
			board[pos[0]][pos[1]] = Piece(None, 0)
		elif attackedPiece.value == 'b' and self.value == 8:
			self.move(board, pos, attackingPos)
		elif self.value == 's' and attackedPiece.value == 1:
			self.move(board, pos, attackingPos)
		elif self.value == 's' and attackedPiece.value != 1:
			board[pos[0]][pos[1]] = Piece(None, 0)
		elif attackedPiece.value == 'f':
			self.move(board, pos, attackingPos)

		

	def __repr__(self):
		return f'Piece({self.color}, {self.value})'


gameBoard = [
[Piece('r', 4),Piece('r', 8),Piece('r', 8),Piece('r', 8),Piece('r', 7),Piece('r', 'b'),Piece('r', 'f'),Piece('r', 'b'),Piece('r', 'b'),Piece('r', 8)],
[Piece('r', 4),Piece('r', 9),Piece('r', 4),Piece('r', 's'),Piece('r', 5),Piece('r', 6),Piece('r', 'b'),Piece('r', 7),Piece('r', 6),Piece('r', 9)],
[Piece('r', 7),Piece('r', 9),Piece('r', 3),Piece('r', 3),Piece('r', 2),Piece('r', 9),Piece('r', 7),Piece('r', 'b'),Piece('r', 'b'),Piece('r', 6)],
[Piece('r', 1),Piece('r', 5),Piece('r', 6),Piece('r', 8),Piece('r', 9),Piece('r', 5),Piece('r', 9),Piece('r', 9),Piece('r', 9),Piece('r', 5)],
[Piece(None, 0), Piece(None, 0), Piece(None, 0), Piece(None, 0), Piece(None, 0), Piece(None, 0), Piece(None, 0), Piece(None, 0), Piece(None, 0), Piece(None, 0)], 
[Piece(None, 0), Piece(None, 0), Piece(None, 0), Piece(None, 0), Piece(None, 0), Piece(None, 0), Piece(None, 0), Piece(None, 0), Piece(None, 0), Piece(None, 0)], 
[Piece('b', 4),Piece('b', 8),Piece('b', 8),Piece('b', 8),Piece('b', 7),Piece('b', 'b'),Piece('b', 'f'),Piece('b', 'b'),Piece('b', 'b'),Piece('b', 8)],
[Piece('b', 4),Piece('b', 9),Piece('b', 4),Piece('b', 's'),Piece('b', 5),Piece('b', 6),Piece('b', 'b'),Piece('b', 7),Piece('b', 6),Piece('b', 9)],
[Piece('b', 7),Piece('b', 9),Piece('b', 3),Piece('b', 3),Piece('b', 2),Piece('b', 9),Piece('b', 7),Piece('b', 'b'),Piece('b', 'b'),Piece('b', 6)],
[Piece('b', 1),Piece('b', 5),Piece('b', 6),Piece('b', 8),Piece('b', 9),Piece('b', 5),Piece('b', 9),Piece('b', 9),Piece('b', 9),Piece('b', 5)]]


if __name__ == '__main__':
	gameBoard[6][0].move(gameBoard, (6,0), (5,0))
	print(gameBoard)