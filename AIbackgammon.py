import random
import pickle
from board import Board

class AgenteRicercaLocale:
	def __init__(self):
		""" Inizializza la politica dell'agente. """
		self.politica = {}  # Dizionario {stato → {mossa → valore accumulato}}

	def scegli_mossa2(self, board, side):
		roll1 = random.randint(1,6)
		roll2 = random.randint(1,6)
		mosse_possibili = board.posMoves(side,roll1,roll2)
		print("mosse possibili:")
		print(mosse_possibili)
		print("numero mosse possibili")
		print(len(mosse_possibili))
		if(len(mosse_possibili)!=0):
			return mosse_possibili[0]
		else:
			return [[-1,-1],[-1,-1]]

	def scegli_mossa(self, board, side):
		roll1 = random.randint(1,6)
		roll2 = random.randint(1,6)
		mosse_possibili = board.posMoves(side, roll1, roll2)
		if not mosse_possibili:
			return None
		b = Board()
		print("stato")
		print(b)
		#se trova nel dizionario scegli quella
		#senno usa ricerca locale
		miglior_mossa = None
		miglior_punteggio = float('-inf')

		for mossa in mosse_possibili:
			print(f"[DEBUG] Mossa analizzata: {mossa}")
			# `mossa` è una lista contenente due sottoliste, ad esempio: [[0, 2], [0, 4]]
			for sublist in mossa:
				# Ora `sublist` è una lista, ad esempio: [0, 2]
				# Fai qualcosa con gli elementi dentro la sottolista
				print(f"Elemento 1: {sublist[0]}, Elemento 2: {sublist[1]}")


	def aggiorna_politica(self, board, mossa, reward):
		print("py di merda(aggiorna_politica)")


def è_stato_finale(board):
	return board.wFree == 15 or board.bFree == 15

def ricerca_locale(agente, episodi=40):
	b = Board()
	print(b)
	side=True
	moves=2
	skip=False
	for k in range(episodi):
		print("episodio n.")
		print(k)
		mosse_migliori = agente.scegli_mossa2(b,side)#restituisce 2 mosse
		print("mosse migliori")
		print(mosse_migliori)
		for i in range(moves):
			if(skip==False):
				outcome=False
				while(outcome==False):
					column,steps = mosse_migliori[i]
					if(column==-1):
						if(steps==-1):
							column=101
					if(column==100):
						return
					if(column!=101):
						outcome, response = b.makeMove(side,column,steps)
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
	print("episodi finiti")


def salva_politica(agente, filename="politica_ia.pkl"):
	with open(filename, "wb") as file:
		pickle.dump(agente.politica, file)

def carica_politica(agente, filename="politica_ia.pkl"):
	try:
		with open(filename, "rb") as file:
			agente.politica = pickle.load(file)
	except FileNotFoundError:
		print("Nessuna politica salvata trovata, l'agente inizierà da zero.")

def gioca_partita(agente):
	print("py di merda")

if __name__ == "__main__":
	agente = AgenteRicercaLocale()
	#carica_politica(agente)

	print("Ricerca Locale...")
	ricerca_locale(agente)

	#print("Allenamento in corso...")
	#allenamento(agente)
	#salva_politica(agente)

	print("L'allenamento è completato! Ora l'IA giocherà una partita.")
	gioca_partita(agente)
