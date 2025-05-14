from telnetlib import KERMIT


class Board:
	def __init__(self):
		"""
		-1=black
		1=white
		"""
		self.init_board()

	def make_move(self, side, column, steps):
		#controllo il lato, controllo se ci sono pedine in prigione, controllo se sulla colonna giusta posso muovermi, controllo la mossa
		if side:#white +1

			if (not self.is_white_jail_empty() and column!=-1):
				return (False, "Free the jail!")
			elif(not self.is_white_jail_empty() and column ==-1):
				#controllo casella arrivo, nel caso la fai

				if(column+steps>25):
					return(False,"Wrong steps number!")
				else:
					#fai la mossa

					if(self.my_board[column + steps]<-1):
						return(False,"Arrival column not possible to occupy")
					else:
						#fai la mossa

						self.white_jail+=-1
						if(self.my_board[column + steps]==-1):
							self.black_jail+=1
							self.my_board[column + steps]=1
							self.black_home+=-1
						else:
							self.my_board[column + steps]+=1
						return(True,"Move done")

			if(column <-1 and column >23):
				return (False, "Wrong number for the column!(too low or too big)")
			else:

				if(self.my_board[column]<1):
					return (False, "Wrong number for the column!(there aren't white pieces)")
				else:

					if((column+steps)>24):
						for i in range(column):
							if (self.my_board[i]>0):
								return (False, "There is a piece in a previous column")

						if(self.white_board == self.white_home):
							self.my_board[column]+=-1
							self.free_white_pieces()

					elif((column+steps)==24):
						#controlla se tutti i pezzi sono a casa
						if(self.white_board == self.white_home):
							self.my_board[column]+=-1
							self.free_white_pieces()
						else:
							return (False,"Impossible to free the piece! The other pieces are not in the home")
					else:
						if(self.my_board[column + steps]<-1):
							return(False,"Impossible to occupy the arrival column")
						else:
							#fai la mossa
							if(self.my_board[column + steps]==-1):
								self.black_jail+=1
								self.my_board[column]+=-1
								self.my_board[column + steps]=1
								if((column+steps)<6):
									self.black_home+=-1
							else:
								self.my_board[column]+=-1
								self.my_board[column + steps]+=1
							if(column+steps>17):
								self.white_home+=1
					return(True,"Move done")
		else:
			if (not self.is_black_jail_empty() and column!=24):
				return (False, "Free the jail!")
			elif(not self.is_black_jail_empty() and column ==24):
				#controllo casella arrivo, nel caso la fai
				if(column-steps<-1):
					return(False,"Wrong steps number!")
				else:
					#fai la mossa
					if(self.my_board[column - steps]>1):
						return(False,"Impossible to occupy the arrival column")
					else:
						#fai la mossa
						self.black_jail+=-1
						if(self.my_board[column - steps]==1):
							self.white_jail+=1
							self.my_board[column - steps]=1
							self.white_home+=-1
						else:
							self.my_board[column - steps]+=-1
						return(True,"Move done")
			if(column <-1 and column >24):
				return (False, "Wrong number for the column!(too low or too big)")
			else:
				if(self.my_board[column]>-1):
					return (False, "Wrong number for the column!(there aren't a white piece)")
				else:
					if((column-steps)<-1):
						for i in range(23-column):
							if (self.my_board[(i + 1) + column]<0):
								return (False, "There is a piece in a previous column")
						if(self.black_board == self.black_home):
							self.my_board[column]+=1
							self.free_black_pieces()
					elif((column-steps)==-1):
						#controlla se tutti i pezzi sono a casa
						if(self.black_board == self.black_home):
							self.my_board[column]+=1
							self.free_black_pieces()
						else:
							return (False,"Impossible to free the piece! The other pieces are not in the home")
					else:
						if(self.my_board[column - steps]>1):
							return(False,"Impossible to occupy the arrival column")
						else:
							#fai la mossa
							if(self.my_board[column - steps]==1):
								self.white_jail+=1
								self.my_board[column]+=1
								self.my_board[column - steps]=-1
								if((column+steps)>17):
									self.white_home+=-1
							else:
								self.my_board[column]+=1
								self.my_board[column - steps]+=-1
							if(column+-steps<6):
								self.white_home+=1
					return(True,"Move done")

	def get_all_possible_moves(self, side, roll1, roll2):
		array_response=[[-1,-1],[-1,-1]]
		if side:
			if (self.white_jail>1):
				#posMove(side,0,roll1)
				#posMove(side,0,roll2)
				if(self.get_possible_move(side, -1, roll1)):
					if(self.get_possible_move(side, -1, roll2)):
						array_response.append([[-1,roll1],[-1,roll2]])
					else:
						#o solo
						#posMove(side,0,roll1)
						array_response.append([[-1,roll1],[-1,-1]])
				#o solo
				#posMove(side,0,roll2)
				elif(self.get_possible_move(side, -1, roll2)):
						array_response.append([[-1,roll2],[-1,-1]])
				else:
					array_response.append([[-1,-1],[-1,-1]])
			elif (self.white_jail == 1):
				temp1=False
				#posMove(side,0,roll1)
				if(self.get_possible_move(side, -1, roll1)):
					temp=False
					for i in range(24):
						if(self.my_board[i]>0):
							#posMove(side,i,roll2)
							if(self.get_possible_move(side, i, roll2)):
								temp=True
								temp1=True
								array_response.append([[-1,roll1],[i,roll2]])
					if(self.get_possible_move(side, roll1 - 1, roll2)):
						temp=True
						temp1=True
						array_response.append([[-1,roll1],[roll1-1,roll2]])
					if(temp==False):
						temp1=True
						array_response.append([[-1,roll1],[-1,-1]])
				if(self.get_possible_move(side, -1, roll2)):
					temp=False
					for i in range(24):
						if(self.my_board[i]>0):
							#posMove(side,i,roll1)
							if(self.get_possible_move(side, i, roll1)):
								temp=True
								temp1=True
								array_response.append([[-1,roll2],[i,roll1]])
					if(self.get_possible_move(side, roll2 - 1, roll1)):
						temp=True
						temp1=True
						array_response.append([[-1,roll2],[roll2-1,roll1]])
					if(temp==False):
						temp1=True
						array_response.append([[-1,roll2],[-1,-1]])
				if(temp1==False):
					array_response.append([[-1,-1],[-1,-1]])
			else:
					for i in range(24):
						if(self.my_board[i]>0):
							#posMove(side,i,roll1)
							if(self.get_possible_move(side, i, roll1)):
								temp = False
								#posMove(side,i,roll2)
								if(self.my_board[i]>1):
									if(self.get_possible_move(side, i, roll2)):
										array_response.append([[i,roll1],[i,roll2]])
								if(self.my_board[i + roll1]==0):
									if(self.get_possible_move(side, i + roll1, roll2)):
										array_response.append([[i,roll1],[i+roll1,roll2]])
								for j in range(24):
									if(i!=j):
										if(self.my_board[j]>0):
											#posMove(side,j,roll2)
											if(self.get_possible_move(side, j, roll2)):
												temp=True
												array_response.append([[i,roll1],[j,roll2]])
								if(temp==False):
									array_response.append([[i,roll1],[-1,-1]])
					for i in range(24):
						if(self.my_board[i]>0):
							#posMove(side,i,roll1)
							if(self.get_possible_move(side, i, roll2)):
								if(self.get_possible_move(side, i + roll2, roll1)):
									array_response.append([[i,roll2],[i+roll2,roll1]])
								temp=False
								for j in range(24):
									if(i!=j):
										if(self.my_board[j]>0):
											#posMove(side,j,roll2)
											if(self.get_possible_move(side, j, roll1)):
												temp=True
								if(temp==False):
									array_response.append([[i,roll2],[-1,-1]])
		else:
			if (self.black_jail>1):
				#posMove(side,0,roll1)
				#posMove(side,0,roll2)
				if(self.get_possible_move(side, 24, roll1)):
					if(self.get_possible_move(side, 24, roll2)):
						array_response.append([[24,roll1],[24,roll2]])
					else:
						#o solo
						#posMove(side,0,roll1)
						array_response.append([[24,roll1],[-1,-1]])
				#o solo
				#posMove(side,0,roll2)
				elif(self.get_possible_move(side, 24, roll2)):
						array_response.append([[24,roll2],[-1,-1]])
				else:
					array_response.append([[-1,-1],[-1,-1]])
			elif (self.black_jail == 1):
				temp1=False
				#posMove(side,0,roll1)
				if(self.get_possible_move(side, 24, roll1)):
					temp=False
					for i in range(24):
						if(self.my_board[i]<0):
							#posMove(side,i,roll2)
							if(self.get_possible_move(side, i, roll2)):
								temp=True
								temp1=True
								array_response.append([[24,roll1],[i,roll2]])
					if(self.get_possible_move(side, 24-roll1, roll2)):
						temp=True
						temp1=True
						array_response.append([[24,roll1],[24-roll1,roll2]])
					if(temp==False):
						temp1=True
						array_response.append([[-1,roll1],[-1,-1]])
				if(self.get_possible_move(side, 24, roll2)):
					temp=False
					for i in range(24):
						if(self.my_board[i]<0):
							#posMove(side,i,roll1)
							if(self.get_possible_move(side, i, roll1)):
								temp1=True
								temp=True
								array_response.append([[24,roll2],[i,roll1]])
					if(self.get_possible_move(side, 24-roll2, roll1)):
						temp=True
						temp1=True
						array_response.append([[-1,roll2],[24-roll2,roll1]])
					if(temp==False):
						temp1=True
						array_response.append([[-1,roll2],[-1,-1]])
				if(temp1==False):
					array_response.append([[-1,-1],[-1,-1]])
			else:
					for i in range(24):
						if(self.my_board[i]<0):
							#posMove(side,i,roll1)
							if(self.get_possible_move(side, i, roll1)):
								temp = False
								#posMove(side,i,roll2)
								if(self.my_board[i]<-1):
									if(self.get_possible_move(side, i, roll2)):
										array_response.append([[i,roll1],[i,roll2]])
								if(self.get_possible_move(side, i - roll1, roll2)):#a
									array_response.append([[i,roll1],[i-roll1,roll2]])
								for j in range(24):
									if(i!=j):
										if(self.my_board[j]<0):
											#posMove(side,j,roll2)
											if(self.get_possible_move(side, j, roll2)):
												temp=True
												array_response.append([[i,roll1],[j,roll2]])
								if(temp==False):
									array_response.append([[i,roll1],[-1,-1]])
					for i in range(24):
						if(self.my_board[i]<0):
							#posMove(side,i,roll1)
							if(self.get_possible_move(side, i, roll2)):
								if(self.get_possible_move(side, i - roll2, roll1)):
									array_response.append([[i,roll2],[i-roll2,roll1]])
								temp=False
								for j in range(24):
									if(i!=j):
										if(self.my_board[j]<0):
											#posMove(side,j,roll2)
											if(self.get_possible_move(side, j, roll1)):
												temp=True
								if(temp==False):
									array_response.append([[i,roll2],[-1,-1]])
		return array_response[2:]

	def get_possible_move(self, side, column, steps):
		if(side):
			if(column+steps>23):
				if(self.white_board == self.white_home):
					if(column+steps>24):
						temp=False
						for i in range(column-1):
							if(self.my_board[i]>0):
								temp=True
						if(temp==True):
							return False
					return True
				else:
					return False
			else:
				if(self.my_board[column + steps]<-1):
					return False
			return True
		else:
			if(column-steps<0):
				if(self.black_board == self.black_home):
					if(column-steps<-1):
						temp=False
						for i in range(23-column):
							if(self.my_board[(i + 1) + column]<0):
								temp=True
						if(temp==True):
							return False
					return True
				else:
					return False
			else:
				if(self.my_board[column - steps]>1):
					return False
			return True

	def evaluate_heuristic(self, side):
		points_vector_white=[-18,-17,-16,-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6]
		points_vector_black=[6,5,4,3,2,1,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18]
		K1=8
		K2=-2
		K3=-1
		K4=-12
		sum_pos_white=0
		threatened_pieces_white=[]
		for i in range(24):
			if(self.my_board[i]>0):
				for j in range(self.my_board[i]):
					sum_pos_white+=points_vector_white[i]
		for i in range(24):
			temp=False
			if(self.my_board[i]==1):
				for j in range(23-i):
					if(self.my_board[j + i]<0):
						temp=True
			if(temp==True):
				threatened_pieces_white.append(1+(int)((i+1)/2))
		threatened_white_sum=0
		for piece in threatened_pieces_white:
			threatened_white_sum += piece
		occupied_columns_number_white=0
		for i in range(6):
			if(self.my_board[i]<-1):
				occupied_columns_number_white+=1
		#caso nero
		sum_pos_black=0
		threatened_pieces_black=[]
		for i in range(24):
			if(self.my_board[i]<0):
				for j in range(-self.my_board[i]):
					sum_pos_black+=points_vector_black[i]
		for i in range(24):
			temp=False
			if(self.my_board[i]==-1):
				for j in range(i):
					if(self.my_board[j]>0):
						temp=True
			if(temp==True):
				threatened_pieces_black.append(1+(int)((24-i)/2))
		threatened_black_sum=0
		for piece in threatened_pieces_black:
			threatened_black_sum += piece
		occupied_columns_number_black=0
		for i in range(6):
			if(self.my_board[i]>1):
				occupied_columns_number_black+=1
		heuristic_white = sum_pos_white + (K1*self.wFree) - threatened_white_sum + self.white_jail * (K2 * occupied_columns_number_white + K3 * (6 - occupied_columns_number_white) + K4)
		heuristic_black = sum_pos_black + (K1*self.bFree) - threatened_black_sum + self.black_jail * (K2 * occupied_columns_number_black + K3 * (6 - occupied_columns_number_black) + K4)
		if(side):
			heuristic_white+=3
			return heuristic_white-heuristic_black
		else:
			heuristic_black+=3
			return heuristic_black-heuristic_white

	def init_board(self):
		self.my_board = {}
		for i in range(24):
			self.my_board[i] = 0
		self.my_board[0] = 2
		self.my_board[5] = -5
		self.my_board[7] = -3
		self.my_board[11] = 5
		self.my_board[12] = -5
		self.my_board[16] = 3
		self.my_board[23] = -2
		self.my_board[18] = 5
		self.wFree = 0
		self.bFree = 0
		self.white_jail = 0
		self.black_jail = 0
		self.white_home = 5
		self.black_home = 5
		self.white_board = 15
		self.black_board = 15

	def is_white_jail_empty(self):
		return self.white_jail==0

	def is_black_jail_empty(self):
		return self.black_jail==0

	def free_white_pieces(self):
		self.wFree += 1
		self.white_board += -1

	def free_black_pieces(self):
		self.bFree += 1
		self.black_board += -1

	def __repr__(self):
		boardstring = ""
		for i in range(24):
			boardstring += str(f"{self.my_board[i]:^3}")
		boardstring += "\n"
		for i in range(24):
			boardstring += str(f"{(i):^3}")
		boardstring += "\n"
		boardstring += "w in jail:" +str(f"{self.white_jail}")
		boardstring += "\n"
		boardstring += "b in jail:" +str(f"{self.black_jail}")
		boardstring += "\n"
		return boardstring
