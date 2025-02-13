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
		move = 2
		if (roll1==roll2):
			move += 4
		if (SIDE==True):
			print("W=1")
		else:
			print("B=-1")
		print("You rolled a " + str(roll1) + " and a " + str(roll2)+", you have "+ str(move)+" moves")
		line = input()

if __name__ == "__main__":
	main()
