from board import Board
import random

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
		for i in range(moves)
		print(", you have "+ str(moves-(i-1))+" moves")
		print("what you wanna do? input:column steps")
		line = input()
		column,steps = parseInput(line)
		outcome, response = b.makeMove(SIDE,column,steps)

if __name__ == "__main__":
	main()
