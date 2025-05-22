import json
import random
from board import Board

class reinforcement_learning:
	def __init__(self):
		""" Inizializza la politica dell'agente. """
		self.politica_w = {}  # Dizionario {stato → {mossa → valore accumulato}}
		self.politica_b = {}  # Dizionario {stato → {mossa → valore accumulato}}

	def upload_experiences_w(self,file_path):
		try:
			with open(file_path, "r") as f:
				experiences = json.load(f)
		except (FileNotFoundError, json.JSONDecodeError):
			experiences = {}
		self.politica_w=experiences

	def upload_experiences_b(self,file_path):
		try:
			with open(file_path, "r") as f:
				experiences = json.load(f)
		except (FileNotFoundError, json.JSONDecodeError):
			experiences = {}
		self.politica_b=experiences

	def init_experiences_w(self, stringa, mosse):
		stringa_mosse= json.dumps(mosse)
		self.politica_w[stringa][stringa_mosse] = 0

	def init_experiences_b(self, stringa, mosse):
		stringa_mosse= json.dumps(mosse)
		self.politica_b[stringa][stringa_mosse] = 0

	def save_experiences_w(self,file_path):
		with open(file_path, "w") as f:
			json.dump(self.politica_w, f, indent=2)

	def save_experiences_b(self,file_path):
		with open(file_path, "w") as f:
			json.dump(self.politica_b, f, indent=2)

	def training(self,episodes):
		b = Board()
		print(b)
		side=True
		moves=2
		skip=False
		k=0
		while ((b.wFree < 15 or b.bFree < 15) and k<episodes):
			roll1 = random.randint(1,6)
			roll2 = random.randint(1,6)
			print("episodio n.")
			print(k)
			a=b.get_all_possible_moves(side, roll1, roll2)
			print("Possible move:")
			print(a)
			h=b.evaluate_heuristic(side)
			if (side==True):
				print("Heuristic value White:")
			else:
				print("Heuristic value Black:")
			print(h)
			stringa= json.dumps(b.my_board)
			print("tavolo")
			print(stringa)
			if(side):
				if stringa not in self.politica_w:
					self.politica_w[stringa] = {}
					for mosse in a:
						self.init_experiences_w(stringa,mosse)
			else:
				if stringa not in self.politica_b:
					self.politica_b[stringa] = {}
					for mosse in a:
						self.init_experiences_b(stringa,mosse)
			mosse_casuali=random.choice(a)
			print("mosse casuale")
			print(mosse_casuali)
			for mossa in mosse_casuali:
				if(skip==False):
					outcome=False
					while(outcome==False):
						column = mossa[0]
						steps = mossa[1]
						if(column==-1):
							if(steps==-1):
								column=101
						if(column==100):
							return
						if(column!=101):
							outcome, response = b.make_move(side, column, steps)
							print(response)
							print(b)
						else:
							print("skip")
							outcome=True
							skip=True
							print(b)
			skip=False
			if (side==True):
				side=False
			else:
				side=True
			k+=1
			print(k)
		print("episodi finiti")
		#faccio allenameto per un numero di episodio
		#gioco fichè ci sono episodi o finche non finisco la partita
		#comincio partita
		#vedo se tavola esiste dentro al dizionario
		#se esiste
		#vedo tutte le mosse possibili
		#ne prendo una a caso e la scelgo
		#se non esiste
		#aggiorno la politica e aggiungo tutte le mosse con reward = 0
		#continuo a giocare finche non finisce la partita
		#quando la partita finisce aggiorno tutte le posizioni in cui sono passato/ tutte le mosse scelte con +1 al reward
