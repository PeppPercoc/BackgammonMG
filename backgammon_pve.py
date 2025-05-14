from board import Board
from backgammon_ls import local_search
import random

exitTerms = "q"
def main():
	b = Board()
	print("Press q if you want to quit, or press something else")
	line = input()
	SIDE = True #True if white, false if black
	print(b)
	moves = 2
	agente = local_search()
	while (line not in exitTerms and (b.wFree < 15 or b.bFree < 15)):
		roll1 = random.randint(1,6)
		roll2 = random.randint(1,6)
		skip = False
		if(SIDE):
			print("W=1")
			print("You rolled a " + str(roll1) + " and a " + str(roll2))
			a=b.get_all_possible_moves(SIDE, roll1, roll2)
			print("possible move:")
			print(a)
			h=b.evaluate_heuristic(SIDE)
			print("Heuristic White:")
			print(h)
			for i in range(moves):
				if(skip==False):
					outcome=False
					while(outcome==False):
						print("You have "+ str(moves-i)+" moves")
						print("What you wanna do? input:column steps")
						line = input()
						column,steps = parse_input(line)
						if(column==100):
							return
						if(column!=101):
							outcome, response = b.make_move(SIDE, column, steps)
							print(response)
							print(b)
						else:
							outcome=True
							skip=True
							print(b)
		else:
			print("You rolled a " + str(roll1) + " and a " + str(roll2))
			best_moves = agente.choose_best_moves(b, SIDE, roll1, roll2)
			print("Best moves:")
			print(best_moves)
			for i in range(moves):
				if(skip==False):
					outcome=False
					while(outcome==False):
						column,steps = best_moves[i]
						if(column==-1):
							if(steps==-1):
								column=101
						if(column==100):
							return
						if(column!=101):
							outcome, response = b.make_move(SIDE, column, steps)
							print(response)
							print(b)
						else:
							print("Skip")
							outcome=True
							skip=True
							print(b)
			skip=False
		if (SIDE==True):
			SIDE=False
		else:
			SIDE=True

def parse_input(response):
	if (response =='s'):
		return (101,101)#skip perchè non ci sono mosse disponibili
	if response in exitTerms:
		return (100, 100)#controllo quit
	# if type(response) == type("Sample string"):
	# 	return(101,101)
	loc = find_separation(response)
	return(int(response[:loc]), int(response[loc+1:]))

def find_separation(value):
	for i in range(len(value)):
		if (value[i] == ' '):
			return i
	return 0

if __name__ == "__main__":
	main()
