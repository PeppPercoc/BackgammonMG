# Backgammon

BackgammonMG è un progetto universitario che implementa il celebre gioco del Backgammon in Python, con l'aggiunta di un modulo di intelligenza artificiale per giocare contro il computer.

## 🔧 Funzionalità

- Interfaccia a riga di comando per giocare a Backgammon
- Regole base del Backgammon implementate
- IA semplice per il gioco contro il computer attraverso la ricerca locale
- IA più complicata per il gioco contro il computer attraverso l'esperienza accumulata dall' apprendimento per rinforzo
- Possibilità di giocare in due sullo stesso dispositivo
- Gestione dei dadi, delle pedine e della logica di movimento
- Supporto per salvataggio e caricamento dello stato di gioco

## 🧠 Intelligenza Artificiale

Il modulo `backgammon_ls.py` contiene un agente artificiale basato su una logica euristica da noi scritta per prendere decisioni di gioco attraverso la ricerca locale. L'IA valuta le mosse disponibili in base a una funzione di valutazione, cercando di massimizzare la propria posizione e minimizzare le possibilità dell’avversario. Attualmente, la strategia si concentra su:

- Protezione delle pedine singole
- Occupazione delle posizioni strategiche
- Uscita efficiente delle pedine dalla tavola
- Penalizzazione delle posizioni vulnerabili

Nel file `backgammon_rl_training.py`, l’agente apprende a giocare tramite un approccio basato sul reinforcement learning. L'addestramento è stato effettuato su 100.000 partite simulate, con salvataggio della politica in formato JSON. L’agente aggiorna la propria strategia in base alle ricompense ricevute, riducendo la probabilità di rimanere intrappolato in situazioni apparentemente vantaggiose ma svantaggiose a lungo termine.

Per ragioni di performance, sono state salvate solo le mosse effettivamente eseguite e che hanno portato ad una vittoria, evitando di memorizzare tutte quelle possibili per ogni stato.


## 📁 Struttura del progetto

```
BackgammonMG/
├── backgammon_ls.py            # Modulo IA con ricerca locale per il computer player
├── backgammon_pvp.py           # Entry point del gioco in pvp
├── backgammon_pve_ls.py        # Entry point del gioco contro l'IA per ricerca locale
├── backgammon_pve_rl.py        # Entry point del gioco contro l'IA con apprendimento per rinforzo
├── backgammon_rl.py            # Modulo IA con l'apprendimento per rinforzo
├── backgammon_rl_training.py   # Allenamento dell'IA e memorizzazzione dell'esperienza nel JSON
├── board.py                    # Gestione del board e delle regole
└── README.md                   # Documentazione del progetto
```

## ▶️ Come eseguire il gioco

Assicurati di avere installato Python 3.10 o superiore.

1. Clona il repository:
   ```bash
   git clone https://github.com/PeppPercoc/BackgammonMG.git
   cd BackgammonMG
   ```

2. Esegui il file con la modalità di gioco desiderata:
   ```bash
   python3 backgammon_[pvp; pve_ls; pve_rl].py
   ```

## ✅ Requisiti

- Python >= 3.10  
Non sono necessarie librerie esterne.

## 📌 Stato del progetto

✅ Gioco base funzionante  
✅ IA per ricerca locale completata
✅ IA con apprendimento per rinforzo addestrata (100.000 partite)  
🛠 Possibili future estensioni:
- Interfaccia grafica (GUI)
- Maggiore ottimizzazione delle prestazioni
- Salvataggio esperienze in formato più efficiente (es. solo mosse scelte)

## 👤 Autore

Progetto sviluppato da Paolo Martino [175974] e Mario Oreste Gallozzi [175082] 
Corso di Intelligenza Artificiale, Università degli Studi del Molise
