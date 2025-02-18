class Board:
	def __init__(self):
		"""
		-1=black
		1=white
		"""
		self.myBoard = {}
		for i in range(24):
			self.myBoard[i] = 0
		self.myBoard[0] = 2
		self.myBoard[5] = -5
		self.myBoard[7] = -3
		self.myBoard[11] = 5
		self.myBoard[12] = -5
		self.myBoard[16] = 3
		self.myBoard[23] = -2
		self.myBoard[18] = 5
		self.wFree = 0
		self.bFree = 0
		self.wJail = 0
		self.bJail = 0
		self.wHome = 5
		self.bHome = 5
		self.wBoard = 15
		self.bBoard = 15

	def makeMove(self,side,column,steps):#manca controllo steps
		#controllo il lato, controllo se ci sono pedine in prigione, controllo se sulla colonna giusta posso muovermi, controllo la mossa
		if side:#white +1
			if (self.wJail > 0 and column!=0):
				return (False, "Free the jail!")
			elif(self.wJail > 0 and column ==0):
				#controllo casella arrivo, nel caso la fai
				if(column+steps<25):
					return(False,"Wrong steps number!")
				else:
					#fai la mossa
					if(self.myBoard[column+steps]<-1):
						return(False,"casella di arrivo non possibile da occupare")
					else:
						#fai la mossa
						self.wJail+=-1
						if(self.myBoard[column+steps]==-1):
							self.bJail+=1
							self.myBoard[column]+=-1
							self.myBoard[column+steps]=1
						else:
							self.myBoard[column]+=-1
							self.myBoard[column+steps]+=1
						return(True,"mossa fatta")
			if(column <0 and column >25):
				return (False, "Wrong number for the column!(too low or too big)")
			else:
				if(self.myBoard[column]<1):
					return (False, "Wrong number for the column!(there aren't a white piece)")
				else:
					#controllo casa arrivo
					if((column+steps)>25):
					    return(False,"mossa non possibile")
					elif((column+steps)==25):
						#controlla se tutti i pezzi sono a casa
						if(self.wBoard == self.wHome):
							self.myBoard[column]+=-1
							self.wFree +=1
							self.wBoard +=-1
					else:
						if(self.myBoard[column+steps]<-1):
							return(False,"casella di arrivo non possibile da occupare")
						else:
							#fai la mossa
							if(self.myBoard[column+steps]==-1):
								self.bJail+=1
								self.myBoard[column]+=-1
								self.myBoard[column+steps]=1
							else:
								self.myBoard[column]+=-1
								self.myBoard[column+steps]+=1
							if(column+steps>17):
								self.wHome+=1
							return(True,"mossa fatta")
		else:
			if (self.bJail > 0 and column!=23):
				return (False, "Free the jail!")
			elif(self.bJail > 0 and column ==23):
				#controllo casella arrivo, nel caso la fai
				if(column-steps<0):
					return(False,"Wrong steps number!")
				else:
					#fai la mossa
					if(self.myBoard[column-steps]>1):
						return(False,"casella di arrivo non possibile da occupare")
					else:
						#fai la mossa
						self.bJail+=-1
						if(self.myBoard[column-steps]==1):
							self.wJail+=1
							self.myBoard[column]+=1
							self.myBoard[column-steps]=-1
						else:
							self.myBoard[column]+=1
							self.myBoard[column-steps]+=-1
						return(True,"mossa fatta")
			if(column <0 and column >25):
				return (False, "Wrong number for the column!(too low or too big)")
			else:
				if(self.myBoard[column]>-1):
					return (False, "Wrong number for the column!(there aren't a black piece)")
				else:
					#controllo casa arrivo
					if((column-steps)<0):
					    return(False,"mossa non possibile")
					elif((column-steps)==0):
						#controlla se tutti i pezzi sono a casa
						if(self.bBoard == self.bHome):
							self.myBoard[column]+=1
							self.bFree +=1
							self.bBoard +=-1
					else:
						if(self.myBoard[column-steps]<-1):
							return(False,"casella di arrivo non possibile da occupare")
						else:
							#fai la mossa
							if(self.myBoard[column-steps]==1):
								self.wJail+=1
								self.myBoard[column]+=1
								self.myBoard[column-steps]=-1
							else:
								self.myBoard[column]+=1
								self.myBoard[column-steps]+=-1
							if(column+steps<7):
								self.wHome+=1
							return(True,"mossa fatta")

#	def posMoves2(self,side,roll1,roll2):
#		arrayResponse=[[-1,-1],[-1,-1]]
#		if(side):
#			if(roll1==roll2):
#				for i to range(4):
#					tempBoard=self.myBoard
#					tempwFree = self.wFree
#					tempwJail = self.wJail
#					tempwHome = self.wHome
#					tempwBoard = self.wBoard
#					if(tempwjal>1):
#						posMoves2Internal(tempBoard,side,roll1)
#			else:
#				#creo tabella temporanea
#				posMoves2Internal()#fai prima mossa
#						#inserisci nell'array di risposta 1+(-1)
#		else:
#			#side black
#
#	def posMoves2Internal(board, side, roll1):
#		if(side):
#			if(tempwjal>1):
#				if(self.posMove(side,0,roll1)):
#					#modifico tabella temp
#					#aggiungo mossa all array
#					return posMoves2Internal()
#			else:
#				for i in range(24):
#					if(self.posMove(side,i,roll1)):
#						#modifico tabella temp
#					return #mossa fatta

	def posMoves(self,side,roll1,roll2):
		arrayResponse=[[-1,-1],[-1,-1]]
		if side:
			if (self.wJail>1):#devo controllare caso doppio
				#fai qualcosa
				#posMove(side,0,roll1)
				#posMove(side,0,roll2)
				if(self.posMove(side,0,roll1)):
					if(self.posMove(side,0,roll2)):
						arrayResponse.append([[0,roll1],[0,roll2]])
					else:
						#o solo
						#posMove(side,0,roll1)
						arrayResponse.append([[0,roll1],[-1,-1]])
				#o solo
				#posMove(side,0,roll2)
				if(self.posMove(side,0,roll2)):
						arrayResponse.append([[0,roll1],[-1,-1]])
			elif (self.wJail==1):
				#posMove(side,0,roll1)
				if(self.posMove(side,0,roll1)):
					for i in range(24):
						if(self.myBoard[i]>0):
							#posMove(side,i,roll2)
							if(self.posMove(side,i,roll2)):
								arrayResponse.append([[0,roll1],[i,roll2]])
				else:
					#o solo
					#posMove(side,0,roll2)
					if(self.posMove(side,0,roll2)):
						arrayResponse.append([[0,roll2],[-1,-1]])
				#o
				#posMove(side,0,roll2)
				if(self.posMove(side,0,roll2)):
					for i in range(24):
						if(self.myBoard[i]>0):
							#posMove(side,i,roll1)
							if(self.posMove(side,i,roll1)):
								arrayResponse.append([[0,roll2],[i,roll1]])
				else:
					#o solo
					#posMove(side,0,roll1)
					if(self.posMove(side,0,roll1)):
						arrayResponse.append([[0,roll1],[-1,-1]])
			else:
					for i in range(24):
						if(self.myBoard[i]>0):
							#posMove(side,i,roll1)
							if(self.posMove(side,i,roll1)):
								temp = False
								#posMove(side,i,roll2)
								if(self.posMove(side,i,roll2)):
									arrayResponse.append([[i,roll1],[i,roll2]])
								for j in range(24):
									if(i!=j):
										if(self.myBoard[j]>0):
											#posMove(side,j,roll2)
											if(self.posMove(side,j,roll2)):
												temp=True
												arrayResponse.append([[i,roll1],[j,roll2]])
								if(self.posMove(side,i+roll1,roll2)):
									arrayResponse.append([[i,roll1],[i+roll1,roll2]])
								if(temp==False):
									arrayResponse.append([[i,roll1],[-1,-1]])
					for i in range(24):
						if(self.myBoard[i]>0):
							#posMove(side,i,roll1)
							if(self.posMove(side,i,roll2)):
								temp=False
								for j in range(24):
									if(i!=j):
										if(self.myBoard[j]>0):
											#posMove(side,j,roll2)
											if(self.posMove(side,j,roll1)):
												temp=True
								if(temp==False):
									arrayResponse.append([[i,roll2],[-1,-1]])
		return arrayResponse[2:]

	def posMove(self,side,column,steps):
		if(side):
			if(column+steps>0 and column+steps<25):
				if(column+steps==24):
					if(self.wBoard == self.wHome):
						return True
					else:
						return False
				else:
					if(self.myBoard[column+steps]<-1):
						return False
			return True
		else:
			if(column-steps>0 and column-steps<25):
				if(self.myBoard[column-steps]>1):
					return False
			return True

	def heuristic(self,side):
		if(side):
			v=[-18,-17,-16,-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6]
			w1=8
			w3= -2
			w4=-1
			K=-12
			M=3
			sumPos=0
			pallineMinacciate=[]
			for i in range(24):
				if(self.myBoard[i]>0):
					for j in range(self.myBoard[i]):
						sumPos+=v[i]
			for i in range(24):
				temp=False
				if(self.myBoard[i]==1):
					for j in range(23-i):
						if(self.myBoard[j+i]<0):
							temp=True
				if(temp==True):
					pallineMinacciate.append(1+(int)((i+1)/2))
			somMin=0
			for pallina in pallineMinacciate:
				somMin += pallina
			return sumPos+(w1*self.wFree)-somMin+self.wJail*(w3(num_caselle_occupate_perchè_ci sono_2_o_piu)+w4+K)+M

	def __repr__(self):
		boardstring = "Board\n"
		for i in range(24):
			boardstring += str(f"{self.myBoard[i]:^3}")
		boardstring += "\n"
		for i in range(24):
			boardstring += str(f"{(i):^3}")
		boardstring += "\n"
		return boardstring
