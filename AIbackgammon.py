import random
import pickle
from board import Board

class AgenteRicercaLocale:
    def __init__(self):
        """ Inizializza la politica dell'agente. """
        self.politica = {}  # Dizionario {stato → {mossa → valore accumulato}}

    def scegli_mossa(self, board, side):


    def aggiorna_politica(self, board, mossa, reward):


def è_stato_finale(board):
    """ Controlla se la partita è finita. """
    return board.wFree == 15 or board.bFree == 15  # Se un giocatore ha liberato tutte le pedine, la partita è finita

def allenamento(agente, episodi=10000):


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


if __name__ == "__main__":
    agente = AgenteRicercaLocale()
    carica_politica(agente)

    print("Allenamento in corso...")
    allenamento(agente)
    salva_politica(agente)

    print("L'allenamento è completato! Ora l'IA giocherà una partita.")
    gioca_partita(agente)
