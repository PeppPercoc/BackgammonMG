from board import Board
import random
import sys

exitTerms = "q"
def main():
	b = Board()
	print("Press q if you want to quit, or press something else")
	line = input()
	SIDE = True #True if white, false if black
	while (line not in exitTerms and (b.wFree < 15 or b.bFree < 15)):
		print(b)
		roll1 = random.randint(1,6)
		roll2 = random.randint(1,6)
		turnComplete = False
		moves = 2
		if (roll1==roll2):
			moves = 4
		if (SIDE==True):
			print("W=1")
		else:
			print("B=-1")
		print("You rolled a " + str(roll1) + " and a " + str(roll2))
		for i in range(moves):
			outcome=False
			while(outcome==False):
				print("You have "+ str(moves-i)+" moves")
				print("What you wanna do? input:column steps")
				line = input()
				column,steps = parseInput(line)
				if(column==100):
					return
				outcome, response = b.makeMove(SIDE,column,steps)
				print(response)
				print(b)
		if (SIDE==True):
			SIDE=False
		else:
			SIDE=True

def parseInput(response):
	if (response =='s'):
		return (101,101)#skip perchè non ci sono mosse disponibili
	if response in exitTerms:
		return (100, 100)#controllo quit
	# if type(response) == type("Sample string"):
	# 	return(101,101)
	loc = findSeparation(response)
	return(int(response[:loc]), int(response[loc+1:]))

def findSeparation(value):
	for i in range(len(value)):
		if (value[i] == ' '):
			return i
	return 0

if __name__ == "__main__":
	main()
