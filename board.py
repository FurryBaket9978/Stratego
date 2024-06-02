from constants import *
from piece import *
import pygame

class Board:
	def __init__(self):
		self.board = []
		self.createBoard()

	def createBoard(self):
		for i in range(0,10):
			self.board.append([])
			for j in range(0,10):
				self.board[i].append(Piece(None, 0))



	def drawBoard(self, surface):
		for i in range(0,10):
			for j in range(0,10):
				if (j == 2 and (i == 4 or i == 5)) or (j == 3 and (i == 4 or i ==5)) or (j == 6 and (i == 4 or i == 5)) or (j == 7 and (i == 4 or i == 5)):
					pygame.draw.rect(surface, BLUE, pygame.Rect(j*60,i*60,60,60))
				else:
					pygame.draw.rect(surface, WHITE, pygame.Rect(j*60,i*60,60,60), 2)

	def draw(self, surface):
		font = pygame.font.Font('font.ttf', 32)
		for i in range(0,10):
			for j in range(0,10):
				piece = self.board[j][i]
				if piece.value == 0:
					continue
				char = str(piece.value)
				if piece.color == 'r':
					color = RED
					char = '*'
				elif piece.color == 'b':
					color = BLUE
				else:
					color = WHITE
				text = font.render(char, True, color)
				textRect = text.get_rect()
				textRect.center = ((i*60)+30, (j*60)+30)
				surface.blit(text, textRect)

	def reveal(self, surface, board, pos):
		font = pygame.font.Font('font.ttf', 32)
		surface.fill(BLACK)
		self.drawBoard(surface)
		for i in range(0,10):
			for j in range(0,10):				
				piece = self.board[j][i]
				if (i,j) == pos:
					#print(pos)
					color = RED
					char = str(piece.value)
				elif piece.value == 0:
					continue
				else:
					char = str(piece.value)
					if piece.color == 'r':
						color = RED
						char = '*'
					elif piece.color == 'b':
						color = BLUE
					else:
						color = WHITE
				text = font.render(char, True, color)
				textRect = text.get_rect()
				textRect.center = ((i*60)+30, (j*60)+30)
				surface.blit(text, textRect)

	def checkPieces(self):
		remainingPieces = {
		"Bomb": 6,
		"Marshal": 1,
		"General": 1,
		"Colonel": 2,
		"Major": 3,
		"Captain": 4,
		"Lieutenant": 4,
		"Sergeant": 4,
		"Miner": 5,
		"Scout": 8,
		"Spy": 1,
		"Flag": 1
		}
		for i in range(0,10):
			for j in range(0,10):
				if self.board[i][j].value != 0:
					remainingPieces[NOTATION[self.board[i][j].value]] -= 1

		return remainingPieces

	def checkFlag(self):
		redFlag = False
		blueFlag = False
		for i in range(0,10):
			for j in range(0,10):
				if self.board[i][j].value == 'f':
					if self.board[i][j].color == 'b':
						blueFlag = True
					elif self.board[i][j].color == 'r':
						redFlag = True
				if redFlag and blueFlag:
					break

		return (redFlag, blueFlag)