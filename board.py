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
		self.myBoard[18] = 5
		self.myBoard[23] = -2
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
				if(column+speps<25):
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
								self.wHome+=+1
							return(True,"mossa fatta")

	def __repr__(self):
		boardstring = "Board\n"
		for i in range(24):
			boardstring += str(f"{self.myBoard[i]:^3}")
		boardstring += "\n"
		for i in range(24):
			boardstring += str(f"{(i+1):^3}")
		boardstring += "\n"
		return boardstring
