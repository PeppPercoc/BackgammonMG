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
			if (self.wJail > 0 and column!=-1):
				return (False, "Free the jail!")
			elif(self.wJail > 0 and column ==-1):
				#controllo casella arrivo, nel caso la fai
				if(column+steps>25):
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
							self.myBoard[column+steps]=1
							self.bHome+=-1
						else:
							self.myBoard[column+steps]+=1
						return(True,"mossa fatta")
			if(column <-1 and column >23):
				return (False, "Wrong number for the column!(too low or too big)")
			else:
				if(self.myBoard[column]<1):
					return (False, "Wrong number for the column!(there aren't a white piece)")
				else:
					if((column+steps)>24):
						for i in range(column):
							if (self.myBoard[i]>0):
								return (False, "C'è una pedina piu' indietro")
						if(self.wBoard == self.wHome):
							self.myBoard[column]+=-1
							self.wFree +=1
							self.wBoard +=-1
					elif((column+steps)==24):
						#controlla se tutti i pezzi sono a casa
						if(self.wBoard == self.wHome):
							self.myBoard[column]+=-1
							self.wFree +=1
							self.wBoard +=-1
						else:
							return (False,"non puoi liberare la pedina perche' le altre non sono a casa")
					else:
						if(self.myBoard[column+steps]<-1):
							return(False,"casella di arrivo non possibile da occupare")
						else:
							#fai la mossa
							if(self.myBoard[column+steps]==-1):
								self.bJail+=1
								self.myBoard[column]+=-1
								self.myBoard[column+steps]=1
								if((column+steps)<6):
									self.bHome+=-1
							else:
								self.myBoard[column]+=-1
								self.myBoard[column+steps]+=1
							if(column+steps>17):
								self.wHome+=1
					return(True,"mossa fatta")
		else:
			if (self.bJail > 0 and column!=24):
				return (False, "Free the jail!")
			elif(self.bJail > 0 and column ==24):
				#controllo casella arrivo, nel caso la fai
				if(column-steps<-1):
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
							self.myBoard[column-steps]=1
							self.wHome+=-1
						else:
							self.myBoard[column-steps]+=-1
						return(True,"mossa fatta")
			if(column <-1 and column >24):
				return (False, "Wrong number for the column!(too low or too big)")
			else:
				if(self.myBoard[column]>-1):
					return (False, "Wrong number for the column!(there aren't a white piece)")
				else:
					if((column-steps)<-1):#aaa
						for i in range(23-column):
							if (self.myBoard[(i+1)+column]<0):
								return (False, "C'è una pedina piu' indietro")
						if(self.bBoard == self.bHome):
							self.myBoard[column]+=1
							self.bFree +=1
							self.bBoard +=-1
					elif((column-steps)==-1):
						#controlla se tutti i pezzi sono a casa
						if(self.bBoard == self.bHome):
							self.myBoard[column]+=1
							self.bFree +=1
							self.bBoard +=-1
						else:
							return (False,"non puoi liberare la pedina perche' le altre non sono a casa")
					else:
						if(self.myBoard[column-steps]>1):
							return(False,"casella di arrivo non possibile da occupare")
						else:
							#fai la mossa
							if(self.myBoard[column-steps]==1):
								self.wJail+=1
								self.myBoard[column]+=1
								self.myBoard[column-steps]=-1
								if((column+steps)>17):
									self.wHome+=-1
							else:
								self.myBoard[column]+=1
								self.myBoard[column-steps]+=-1
							if(column+-steps<6):
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
			if (self.wJail>1):
				#posMove(side,0,roll1)
				#posMove(side,0,roll2)
				if(self.posMove(side,-1,roll1)):
					if(self.posMove(side,-1,roll2)):
						arrayResponse.append([[-1,roll1],[-1,roll2]])
					else:
						#o solo
						#posMove(side,0,roll1)
						arrayResponse.append([[-1,roll1],[-1,-1]])
				#o solo
				#posMove(side,0,roll2)
				elif(self.posMove(side,-1,roll2)):
						arrayResponse.append([[-1,roll2],[-1,-1]])
			elif (self.wJail==1):
				#posMove(side,0,roll1)
				if(self.posMove(side,-1,roll1)):
					for i in range(24):
						if(self.myBoard[i]>0):
							#posMove(side,i,roll2)
							if(self.posMove(side,i,roll2)):
								arrayResponse.append([[-1,roll1],[i,roll2]])
					if(self.posMove(side,roll1-1,roll2)):
						arrayResponse.append([[-1,roll1],[roll1-1,roll2]])
				else:
					if(self.posMove(side,-1,roll2)):
						for i in range(24):
							if(self.myBoard[i]>0):
								#posMove(side,i,roll1)
								if(self.posMove(side,i,roll1)):
									arrayResponse.append([[-1,roll2],[i,roll1]])
					else:
						#o solo
						#posMove(side,0,roll1)
						if(self.posMove(side,-1,roll1)):
							arrayResponse.append([[-1,roll1],[-1,-1]])
			else:
					for i in range(24):
						if(self.myBoard[i]>0):
							#posMove(side,i,roll1)
							if(self.posMove(side,i,roll1)):
								temp = False
								#posMove(side,i,roll2)
								if(self.myBoard[i]>1):
									if(self.posMove(side,i,roll2)):
										arrayResponse.append([[i,roll1],[i,roll2]])
								if(self.myBoard[i+roll1]==0):
									if(self.posMove(side,i+roll1,roll2)):
										arrayResponse.append([[i,roll1],[i+roll1,roll2]])
								for j in range(24):
									if(i!=j):
										if(self.myBoard[j]>0):
											#posMove(side,j,roll2)
											if(self.posMove(side,j,roll2)):
												temp=True
												arrayResponse.append([[i,roll1],[j,roll2]])
								if(temp==False):
									arrayResponse.append([[i,roll1],[-1,-1]])
					for i in range(24):
						if(self.myBoard[i]>0):
							#posMove(side,i,roll1)
							if(self.posMove(side,i,roll2)):
								if(self.posMove(side,i+roll2,roll1)):
									arrayResponse.append([[i,roll2],[i+roll2,roll1]])
								temp=False
								for j in range(24):
									if(i!=j):
										if(self.myBoard[j]>0):
											#posMove(side,j,roll2)
											if(self.posMove(side,j,roll1)):
												temp=True
								if(temp==False):
									arrayResponse.append([[i,roll2],[-1,-1]])
		else:
			if (self.bJail>1):
				#posMove(side,0,roll1)
				#posMove(side,0,roll2)
				if(self.posMove(side,24,roll1)):
					if(self.posMove(side,24,roll2)):
						arrayResponse.append([[24,roll1],[24,roll2]])
					else:
						#o solo
						#posMove(side,0,roll1)
						arrayResponse.append([[24,roll1],[-1,-1]])
				#o solo
				#posMove(side,0,roll2)
				elif(self.posMove(side,24,roll2)):
						arrayResponse.append([[24,roll2],[-1,-1]])
			elif (self.bJail==1):
				#posMove(side,0,roll1)
				if(self.posMove(side,24,roll1)):
					for i in range(24):
						if(self.myBoard[i]<0):
							#posMove(side,i,roll2)
							if(self.posMove(side,i,roll2)):
								arrayResponse.append([[24,roll1],[i,roll2]])
				else:
					#o solo
					#posMove(side,0,roll2)
					if(self.posMove(side,24,roll2)):
						arrayResponse.append([[24,roll2],[-1,-1]])
				#o
				#posMove(side,0,roll2)
				if(self.posMove(side,24,roll2)):
					for i in range(24):
						if(self.myBoard[i]<0):
							#posMove(side,i,roll1)
							if(self.posMove(side,i,roll1)):
								arrayResponse.append([[24,roll2],[i,roll1]])
				else:
					#o solo
					#posMove(side,0,roll1)
					if(self.posMove(side,24,roll1)):
						arrayResponse.append([[24,roll1],[-1,-1]])
			else:
					for i in range(24):
						if(self.myBoard[i]<0):
							#posMove(side,i,roll1)
							if(self.posMove(side,i,roll1)):
								temp = False
								#posMove(side,i,roll2)
								if(self.myBoard[i]<-1):
									if(self.posMove(side,i,roll2)):
										arrayResponse.append([[i,roll1],[i,roll2]])
								if(self.posMove(side,i-roll1,roll2)):#a
									arrayResponse.append([[i,roll1],[i-roll1,roll2]])
								for j in range(24):
									if(i!=j):
										if(self.myBoard[j]<0):
											#posMove(side,j,roll2)
											if(self.posMove(side,j,roll2)):
												temp=True
												arrayResponse.append([[i,roll1],[j,roll2]])
								if(temp==False):
									arrayResponse.append([[i,roll1],[-1,-1]])
					for i in range(24):
						if(self.myBoard[i]<0):
							#posMove(side,i,roll1)
							if(self.posMove(side,i,roll2)):
								if(self.posMove(side,i-roll2,roll1)):
									arrayResponse.append([[i,roll2],[i-roll2,roll1]])
								temp=False
								for j in range(24):
									if(i!=j):
										if(self.myBoard[j]<0):
											#posMove(side,j,roll2)
											if(self.posMove(side,j,roll1)):
												temp=True
								if(temp==False):
									arrayResponse.append([[i,roll2],[-1,-1]])
		return arrayResponse[2:]

	def posMove(self,side,column,steps):
		if(side):
			if(column+steps>23):
				if(self.wBoard == self.wHome):
					if(column+steps>24):
						temp=False
						for i in range(column-1):
							if(self.myBoard[i]>0):
								temp=True
						if(temp==True):
							return False
					return True
				else:
					return False
			else:
				if(self.myBoard[column+steps]<-1):
					return False
			return True
		else:
			if(column-steps<0):
				if(self.bBoard == self.bHome):
					if(column-steps<-1):
						temp=False
						for i in range(23-column):
							if(self.myBoard[(i+1)+column]<0):
								temp=True
						if(temp==True):
							return False
					return True
				else:
					return False
			else:
				if(self.myBoard[column-steps]>1):
					return False
			return True

	def heuristic(self,side):
		vw=[-18,-17,-16,-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6]
		vb=[6,5,4,3,2,1,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18]
		w1=8
		w3=-2
		w4=-1
		K=-12
		sumPosW=0
		pedineMinacciateW=[]
		for i in range(24):
			if(self.myBoard[i]>0):
				for j in range(self.myBoard[i]):
					sumPosW+=vw[i]
		for i in range(24):
			temp=False
			if(self.myBoard[i]==1):
				for j in range(23-i):
					if(self.myBoard[j+i]<0):
						temp=True
			if(temp==True):
				pedineMinacciateW.append(1+(int)((i+1)/2))
		somMinW=0
		for pedina in pedineMinacciateW:
			somMinW += pedina
		numCasOccW=0
		for i in range(6):
			if(self.myBoard[i]<-1):
				numCasOccW+=1
		#caso nero
		sumPosB=0
		pedineMinacciateB=[]
		for i in range(24):
			if(self.myBoard[i]<0):
				for j in range(-self.myBoard[i]):
					sumPosB+=vb[i]
		for i in range(24):
			temp=False
			if(self.myBoard[i]==-1):
				for j in range(i):
					if(self.myBoard[j]>0):
						temp=True
			if(temp==True):
				pedineMinacciateB.append(1+(int)((24-i)/2))
		somMinB=0
		for pedina in pedineMinacciateB:
			somMinB += pedina
		numCasOccB=0
		for i in range(6):
			if(self.myBoard[i]>1):
				numCasOccB+=1
		HW = sumPosW+(w1*self.wFree)-somMinW+self.wJail*(w3*numCasOccW+w4*(6-numCasOccW)+K)
		HB = sumPosB+(w1*self.bFree)-somMinB+self.bJail*(w3*numCasOccB+w4*(6-numCasOccB)+K)
		if(side):
			HW+=3
			return HW-HB
		else:
			HB+=3
			return HB-HW

	def __repr__(self):
		boardstring = ""
		for i in range(24):
			boardstring += str(f"{self.myBoard[i]:^3}")
		boardstring += "\n"
		for i in range(24):
			boardstring += str(f"{(i):^3}")
		boardstring += "\n"
		boardstring += "w in jail:" +str(f"{self.wJail}")
		boardstring += "\n"
		boardstring += "b in jail:" +str(f"{self.bJail}")
		boardstring += "\n"
		return boardstring
