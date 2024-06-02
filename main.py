import pygame
from board import *
from constants import *
from piece import *
import time
import random

pygame.init()

def main():
	SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
	running = True
	board = Board()
	gameBoard = board.board
	setupBlue = True
	setupRed = False
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
	selectedPiece = None
	selectedPos = None
	moves = []
	turn = 'b'
	while running:
		board.drawBoard(SCREEN)
		pos = pygame.mouse.get_pos()
		(col, row) = (pos[0]//60, pos[1]//60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			elif setupBlue:
				'''
				pos = [
					[Piece('b', 4),Piece('b', 8),Piece('b', 8),Piece('b', 8),Piece('b', 7),Piece('b', 'b'),Piece('b', 'f'),Piece('b', 'b'),Piece('b', 'b'),Piece('b', 8)],
					[Piece('b', 4),Piece('b', 9),Piece('b', 4),Piece('b', 's'),Piece('b', 5),Piece('b', 6),Piece('b', 'b'),Piece('b', 7),Piece('b', 6),Piece('b', 9)],
					[Piece('b', 7),Piece('b', 9),Piece('b', 3),Piece('b', 3),Piece('b', 2),Piece('b', 9),Piece('b', 7),Piece('b', 'b'),Piece('b', 'b'),Piece('b', 6)],
					[Piece('b', 1),Piece('b', 5),Piece('b', 6),Piece('b', 8),Piece('b', 9),Piece('b', 5),Piece('b', 9),Piece('b', 9),Piece('b', 9),Piece('b', 5)]]
				gameBoard[6:10] = reversed(pos)
				setupBlue = False
				setupRed = True
				'''
				if event.type == pygame.KEYDOWN:
					if row >= 6:
						if gameBoard[row][col].value != 0:
							remainingPieces[NOTATION[gameBoard[row][col].value]] += 1

						if event.key == pygame.K_b:
							value = 'b'
						elif event.key == pygame.K_f:
							value = 'f'
						elif event.key == pygame.K_1:
							value = 1
						elif event.key == pygame.K_2:
							value = 2
						elif event.key == pygame.K_3:
							value = 3
						elif event.key == pygame.K_4:
							value = 4
						elif event.key == pygame.K_5:
							value = 5
						elif event.key == pygame.K_6:
							value = 6
						elif event.key == pygame.K_7:
							value = 7
						elif event.key == pygame.K_8:
							value = 8
						elif event.key == pygame.K_9:
							value = 9
						elif event.key == pygame.K_s:
							value = 's'
						elif event.key == pygame.K_BACKSPACE:
							piece = gameBoard[row][col]
							remainingPieces[NOTATION[piece.value]] += 1
							gameBoard[row][col] = Piece(None, 0)
						elif event.key == pygame.K_RETURN:
							pieces = board.checkPieces()
							for i in pieces:
								if pieces[i] != 0:
									break
								else:
									setupBlue = False
									setupRed = True


						if event.key != pygame.K_RETURN and event.key != pygame.K_BACKSPACE:
							insertedPiece = Piece('b', value)
							if remainingPieces[NOTATION[insertedPiece.value]] > 0:
								gameBoard[row][col] = insertedPiece
								remainingPieces[NOTATION[insertedPiece.value]] -= 1

			elif event.type == pygame.MOUSEBUTTONDOWN and not setupRed and not setupBlue and turn == 'b':
				if selectedPiece != None and (row, col) in moves:
					if gameBoard[row][col].color == 'r':
						board.reveal(SCREEN, gameBoard, (col, row))
						pygame.display.update()
						time.sleep(1)
					selectedPiece.attack(gameBoard, selectedPos, (row, col))
					selectedPiece = None
					selectedPos = None
					moves = []
					turn = 'r'
				elif gameBoard[row][col].value != 0 and gameBoard[row][col].color == 'b':
					selectedPiece = gameBoard[row][col]
					selectedPos = (row, col)
					moves = selectedPiece.getMoves(row,col,gameBoard)
				
		if setupRed:
			pos = [
					[Piece('r', 4),Piece('r', 8),Piece('r', 8),Piece('r', 8),Piece('r', 7),Piece('r', 'b'),Piece('r', 'f'),Piece('r', 'b'),Piece('r', 'b'),Piece('r', 8)],
					[Piece('r', 4),Piece('r', 9),Piece('r', 4),Piece('r', 's'),Piece('r', 5),Piece('r', 6),Piece('r', 'b'),Piece('r', 7),Piece('r', 6),Piece('r', 9)],
					[Piece('r', 7),Piece('r', 9),Piece('r', 3),Piece('r', 3),Piece('r', 2),Piece('r', 9),Piece('r', 7),Piece('r', 'b'),Piece('r', 'b'),Piece('r', 6)],
					[Piece('r', 1),Piece('r', 5),Piece('r', 6),Piece('r', 8),Piece('r', 9),Piece('r', 5),Piece('r', 9),Piece('r', 9),Piece('r', 9),Piece('r', 5)]]
			gameBoard[0:4] = pos
			setupRed = False

		if turn == 'r':
			#make ai
			starting = True
			while starting:
				x = random.randint(0,9)
				y = random.randint(0,9)
				piece = gameBoard[y][x]
				if piece.color == 'r':
					aiMoves = piece.getMoves(y, x, gameBoard)
					if len(aiMoves) > 0:
						(row, col) = aiMoves[random.randint(0,len(aiMoves)-1)]
						if gameBoard[row][col].color == 'b':
							board.reveal(SCREEN, gameBoard, (x,y))
							pygame.display.update()
							time.sleep(1)
						piece.attack(gameBoard, (y,x), (row, col))
						starting = False
						turn = 'b'



		SCREEN.fill(BLACK)
		board.drawBoard(SCREEN)
		board.draw(SCREEN)
		if selectedPos:
			pygame.draw.circle(SCREEN, WHITE, ((selectedPos[1] *60)+30, (selectedPos[0] *60)+30), 30, 5)
		for i in moves:
			if gameBoard[i[0]][i[1]].color == None:
				pygame.draw.circle(SCREEN, WHITE, ((i[1] *60)+30, (i[0] *60)+30), 10)
			else:
				pygame.draw.circle(SCREEN, WHITE, ((i[1] *60)+30, (i[0] *60)+30), 30, 5)
		pygame.display.update()
		(blueFlag, redFlag) = board.checkFlag()
		if (not blueFlag or not redFlag) and (not setupRed and not setupBlue):
			time.sleep(3)
			running = False
	pygame.quit()

main()


