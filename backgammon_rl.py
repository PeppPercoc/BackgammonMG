import json
import random
from board import Board
from backgammon_ls import local_search

epsilon = 0.5

class reinforcement_learning:
	def __init__(self):
		''' Initializing agent's politic.'''
		self.politic_w = {}  # Dizionario {stato → {mossa → valore accumulato}}
		self.politic_b = {}  # Dizionario {stato → {mossa → valore accumulato}}

	def upload_experiences_w(self,file_path):
		try:
			with open(file_path, "r") as f:
				experiences = json.load(f)
		except (FileNotFoundError, json.JSONDecodeError):
			experiences = {}
		self.politic_w=experiences

	def upload_experiences_b(self,file_path):
		try:
			with open(file_path, "r") as f:
				experiences = json.load(f)
		except (FileNotFoundError, json.JSONDecodeError):
			experiences = {}
		self.politic_b=experiences

	def init_experience(self, politic, string, chosen_move_string):
		if string not in politic:
			politic[string] = {}
		if chosen_move_string not in politic[string]:
			politic[string][chosen_move_string] = 0

	def save_experiences_w(self,file_path):
		with open(file_path, "w") as f:
			json.dump(self.politic_w, f, indent=2)

	def save_experiences_b(self,file_path):
		with open(file_path, "w") as f:
			json.dump(self.politic_b, f, indent=2)

	def training(self,episodes):
		b = Board()
		ls = local_search()
		print(b)
		side=True
		skip=False
		k=0
		chosen_moves_w={}
		chosen_moves_b={}
		while (k<episodes):
			if(b.wFree > 14 or b.bFree > 14):
				break
			roll1 = random.randint(1,6)
			roll2 = random.randint(1,6)
			# print("Episode no.")
			# print(k)
			all_moves=b.get_all_possible_moves(side, roll1, roll2)
			# print("Possible moves:")
			# print(a)
			#h=b.evaluate_heuristic(side)
			#if (side==True):
			#	print("Heuristic value White:")
			#else:
			#	print("Heuristic value Black:")
			#print(h)
			string= json.dumps(b.my_board)
			#print(string)

			if random.random() < epsilon:
				#print("Random chosen moves: ")
				if(len(all_moves)!=0):
					moves=random.choice(all_moves)
				else:
					moves=[[-1,-1],[-1,-1]]
			else:
				#print("Moves chosen with local search: ")
				moves= ls.choose_best_moves(b, side,roll1,roll2)
			#print(moves)
			moves_string= json.dumps(moves)

			if (side):
				#self.init_experience(self.politic_w, string, moves_string)
				chosen_moves_w[string] = moves_string
			else:
				#self.init_experience(self.politic_b, string, moves_string)
				chosen_moves_b[string] = moves_string

			for move in moves:
				if(skip==False):
					outcome=False
					while(outcome==False):
						column = move[0]
						steps = move[1]
						if(column==-1):
							if(steps==-1):
								column=101
						if(column==100):
							return
						if(column!=101):
							outcome, response = b.make_move(side, column, steps)
							#print(response)
							#print(b)
						else:
							#print("skip")
							outcome=True
							skip=True
							#print(b)
			skip=False
			if (side==True):
				side=False
			else:
				side=True
			k+=1

		print(k)
		print("Episodes ended")

		if(b.wFree > 14):
			#print("White won")
			for status in chosen_moves_w:
				if status not in self.politic_w:
					self.politic_w[status] = {}
				if chosen_moves_w[status] not in self.politic_w[status]:
					self.politic_w[status][chosen_moves_w[status]] = 1
				else:
					if(chosen_moves_w[status]!="[[-1, -1], [-1, -1]]"):
						self.politic_w[status][chosen_moves_w[status]]+=1
			return 1

		if(b.bFree > 14):
			#print("Black won")
			for status in chosen_moves_b:
				if status not in self.politic_b:
					self.politic_b[status] = {}
				if chosen_moves_b[status] not in self.politic_b[status]:
					self.politic_b[status][chosen_moves_b[status]] = 1
				else:
					if(chosen_moves_b[status]!="[[-1, -1], [-1, -1]]"):
						self.politic_b[status][chosen_moves_b[status]]+=1
			return 0

		#faccio allenameto per un numero di episodio
		#gioco finchè ci sono episodi o finchè non finisco la partita
		#comincio partita
		#vedo se tavola esiste dentro al dizionario
		#se esiste
		#vedo tutte le mosse possibili
		#ne prendo una a caso e la scelgo
		#se non esiste
		#aggiorno la politica e aggiungo tutte le mosse con reward = 0
		#continuo a giocare finche non finisce la partita
		#quando la partita finisce aggiorno tutte le posizioni in cui sono passato/ tutte le mosse scelte con +1 al reward
