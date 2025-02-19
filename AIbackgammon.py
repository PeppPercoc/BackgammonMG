import random
import pickle
from board import Board

class AgenteRicercaLocale:
	def __init__(self):
		""" Inizializza la politica dell'agente. """
		self.politica = {}  # Dizionario {stato → {mossa → valore accumulato}}

	def scegli_mossa(self, board, side):
		roll1 = random.randint(1,6)
		roll2 = random.randint(1,6)
		mosse_possibili = board.posMoves(side, roll1, roll2)
		if not mosse_possibili:
			return None
		stato = repr(board)
		print("stato")
		print(stato)
		#se trova nel dizionario scegli quella
		#senno usa ricerca locale
		miglior_mossa = None
		miglior_punteggio = float('-inf')

		for mossa in mosse_possibili:
			print(f"[DEBUG] Mossa analizzata: {mossa}")
			# `pair` è una lista contenente due sottoliste, ad esempio: [[0, 2], [0, 2]]
			for sublist in mossa:
				# Ora `sublist` è una lista, ad esempio: [0, 2]
				# Fai qualcosa con gli elementi dentro la sottolista
				print(f"Elemento 1: {sublist[0]}, Elemento 2: {sublist[1]}")


	def aggiorna_politica(self, board, mossa, reward):
		print("py di merda")


def è_stato_finale(board):
	return board.wFree == 15 or board.bFree == 15

def allenamento(agente, episodi=10000):
	for _ in range(episodi):
		board = Board()
		side=True

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
	carica_politica(agente)

	print("Allenamento in corso...")
	allenamento(agente)
	salva_politica(agente)
	board = Board()
	agente.scegli_mossa(board,True)

	print("L'allenamento è completato! Ora l'IA giocherà una partita.")
	gioca_partita(agente)
