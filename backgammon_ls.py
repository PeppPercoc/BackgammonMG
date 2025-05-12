import random
from board import Board
from copy import deepcopy

class RicercaLocale:
	def scegli_mossa(self, board, side, roll1, roll2):
		print("You rolled a " + str(roll1) + " and a " + str(roll2))
		mosse_possibili = board.posMoves(side,roll1,roll2)
		if(len(mosse_possibili)!=0):
			print("mosse possibili:")
			print(mosse_possibili)
			print("numero mosse possibili")
			print(len(mosse_possibili))
			print("euristica:")
			h=board.heuristic(side)
			print(h)
			#calcolo temph
			tempb = deepcopy(board)
			for sublist in mosse_possibili[0]:
				tempb.makeMove(side,sublist[0],sublist[1])
			temph=tempb.heuristic(side)
			mossa_migliore=[[-1,-1],[-1,-1]]
			for mossa in mosse_possibili:
				b2 = deepcopy(board)
				outcome=False
				print(f"[DEBUG] Mossa analizzata: {mossa}")
				# `mossa` è una lista contenente due sottoliste, ad esempio: [[0, 2], [0, 4]]
				for sublist in mossa:
					# Ora `sublist` è una lista, ad esempio: [0, 2]
					# Fai qualcosa con gli elementi dentro la sottolista
					print(f"Elemento 1: {sublist[0]}, Elemento 2: {sublist[1]}")
					if(sublist[0]!=-1):
						if(sublist[1]!=-1):
							outcome,response=b2.makeMove(side,sublist[0],sublist[1])
				h2=b2.heuristic(side)
				print("euristica calcolata dopo mossa:")
				print(h2)
				if(h2>temph):
					temph=h2
					mossa_migliore=mossa
			return mossa_migliore
		else:
			return [[-1,-1],[-1,-1]]
		#if(len(mosse_possibili)!=0):
			#return mosse_possibili[0]
		#else:
		#	return [[-1,-1],[-1,-1]]
