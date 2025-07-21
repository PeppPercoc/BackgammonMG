from copy import deepcopy

class local_search:
	def choose_best_moves(self, board, side, roll1, roll2):
		possible_moves = board.get_all_possible_moves(side, roll1, roll2)
		if(len(possible_moves)!=0):
			print("Possible moves:")
			print(possible_moves)
			print("Possible moves number")
			print(len(possible_moves))
			print("Heuristic value:")
			h=board.evaluate_heuristic(side)
			print(h)
			#calcolo temph
			tempb = deepcopy(board)
			for sublist in possible_moves[0]:
				tempb.make_move(side, sublist[0], sublist[1])
			temph=tempb.evaluate_heuristic(side)
			best_moves=possible_moves[0]
			for moves in possible_moves:
				b2 = deepcopy(board)
				outcome=False
				# print(f"[DEBUG] Analyzed moves: {moves}")
				# `mossa` è una lista contenente due sottoliste, ad esempio: [[0, 2], [0, 4]]
				for sublist in moves:
					# Ora `sublist` è una lista, ad esempio: [0, 2]
					# Fai qualcosa con gli elementi dentro la sottolista
					print(f"First element: {sublist[0]}, Second element: {sublist[1]}")
					if(sublist[0]!=-1):
						if(sublist[1]!=-1):
							outcome,response=b2.make_move(side, sublist[0], sublist[1])
				h2=b2.evaluate_heuristic(side)
				print("Heuristic value after the move:")
				print(h2)
				if(h2>temph):
					temph=h2
					best_moves=moves
			return best_moves
		else:
			return [[-1,-1],[-1,-1]]
		#if(len(mosse_possibili)!=0):
			#return mosse_possibili[0]
		#else:
		#	return [[-1,-1],[-1,-1]]
