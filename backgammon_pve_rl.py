from board import Board
from backgammon_rl import reinforcement_learning
from backgammon_ls import local_search
import random
import json
import ast

exitTerms = "q"
def main():
	agent = reinforcement_learning()
	print("Loading experience...")
	agent.upload_experiences_b("experience_b.json")
	b = Board()
	print("Press q if you want to quit, or press something else")
	line = input()
	SIDE = True #True if white, false if black
	print(b)
	moves = 2
	while (line not in exitTerms):
		if(b.wFree > 14 or b.bFree > 14):
				break
		roll1 = random.randint(1,6)
		roll2 = random.randint(1,6)
		skip = False
		if (SIDE):
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
			ls = local_search()
			string= json.dumps(b.my_board)
			a=b.get_all_possible_moves(SIDE, roll1, roll2)
			best_moves=[]
			string_best_moves=[]
			if string  in agent.politic_b:
				#controllare se esiste mossa
				temp=-1
				for move in a:
					moves_string=json.dumps(move)
					if moves_string in agent.politic_b[string]:
						if(agent.politic_b[string][moves_string] > temp):
							temp=agent.politic_b[string][moves_string]
							string_best_moves=moves_string
				if(temp==-1):
					print("Local search:")
					best_moves= ls.choose_best_moves(b, SIDE,roll1,roll2)
				else:
					print("Reinforcement learning best moves:")
					lista = ast.literal_eval(string_best_moves)
					best_moves = [tuple(x) for x in lista]
			else:
				best_moves= ls.choose_best_moves(b, SIDE,roll1,roll2)
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
