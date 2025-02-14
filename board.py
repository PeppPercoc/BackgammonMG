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
		column+=-1
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

	def posMoves(self,side,roll1,roll2):
		ArrayResponse=[[-1,-1],[-1,-1]]
		if side:
			if (self.wJail>1):
				#fai qualcosa
				#posMove(side,0,roll1)
				#posMove(side,0,roll2)
				if(self.posMove(side,0,roll1)):
					if(self.posMove(side,0,roll2)):
						ArrayResponse.append([[0,roll1],[0,roll2]])
				#o
				#posMove(side,0,roll1)
				#o
				#posMove(side,0,roll2)
			elif (self.wJail==1):
				#posMove(side,0,roll1)
				for i in range(24):
					if(self.myBoard[i]>0):
						#posMove(side,i,roll2)
						print("py di merda")
					#o
				#posMove(side,0,roll2)
				for i in range(24):
					if(self.myBoard[i]>0):
						#posMove(side,i,roll1)
						print("py di merda")
				#o
				#posMove(side,0,roll1)
				#o
				#posMove(side,0,roll2)
			else:
				for i in range(24):
					if(self.myBoard[i]>1):
						#posMove(side,i,roll1)
						#posMove(side,i,roll2)
						print("py di merda")
					elif(self.myBoard[i]==1):
						#posMove(side,i,roll1)
						for j in range(24):
							#posMove(side,j,roll2)
							print("py di merda")
				if(ArrayResponse=={}):
					for i in range(24):
						if(self.myBoard[i]>1):
							#posMove(side,i,roll1)
							print("py di merda")
					#o
					for i in range(24):
						if(self.myBoard[i]>1):
							#posMove(side,i,roll2)
							print("py di merda")
		return ArrayResponse

	def posMove(self,side,column,steps):
		if(side):
			if(column+steps>0 and column+steps<25):
				if(self.myBoard[column+steps]<-1):
					return False
			return True
		else:
			if(column-steps>0 and column-steps<25):
				if(self.myBoard[column-steps]>1):
					return False
			return True

	def __repr__(self):
		boardstring = "Board\n"
		for i in range(24):
			boardstring += str(f"{self.myBoard[i]:^3}")
		boardstring += "\n"
		for i in range(24):
			boardstring += str(f"{(i+1):^3}")
		boardstring += "\n"
		return boardstring
