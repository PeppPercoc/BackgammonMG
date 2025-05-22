from board import Board
from backgammon_rl import reinforcement_learning
import random

exitTerms = "q"
def main():
	agente = reinforcement_learning()
	print("Carico esperienza")
	agente.upload_experiences_w("esperienze_w.json")
	agente.upload_experiences_b("esperienze_b.json")
	print("allenamento...")
	agente.training(10)
	print("Salva esperienza white")
	print(agente.politica_w)
	print("Salva esperienza black")
	print(agente.politica_b)
	agente.save_experiences_w("esperienze_w.json")
	agente.save_experiences_b("esperienze_b.json")
	print("L'allenamento è completato! Ora l'IA è pronto per giocare una partita.")

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
