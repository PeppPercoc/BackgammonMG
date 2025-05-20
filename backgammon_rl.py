import json

class reinforcement_learning:
    def __init__(self):
		""" Inizializza la politica dell'agente. """
		self.politica = {}  # Dizionario {stato → {mossa → valore accumulato}}

	def upload_experiences(self,file_path):
		try:
			with open(file_path, "r") as f:
			experiences = json.load(f)
		except (FileNotFoundError, json.JSONDecodeError):
			experiences = {}
		self.politica=experiences

	def save_experiences(self,file_path):
		with open(file_path, "w") as f:
			json.dump(self.politica, f, indent=2)

    def training(self,episodes):
        b = Board()
        print(b)
        side=True
        moves=2
        skip=False
        for k in range(episodes):
            print("episodio n.")
            print(k)

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

