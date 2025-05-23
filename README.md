# Backgammon

BackgammonMG è un progetto universitario che implementa il celebre gioco del Backgammon* in Python, con l'aggiunta di un modulo di intelligenza artificiale per giocare contro il computer.

*La nostra implementazione non comprende la funzione del dado doppio. Nel gioco originale, quando si ottiene un dado doppio(Es. 6 e 6) si ha la possibilità di fare 4 mosse con il risultato dei dadi(Es. 6, 6, 6 e 6).

## 🔧 Funzionalità

- Interfaccia a riga di comando per giocare a Backgammon
- Regole base del Backgammon implementate
- IA semplice per il gioco contro il computer
- Possibilità di giocare in due sullo stesso dispositivo
- Gestione dei dadi, delle pedine e della logica di movimento
- Supporto per salvataggio e caricamento dello stato di gioco

## 🧠 Intelligenza Artificiale

Il modulo `backgammon_ls.py` contiene un agente artificiale basato su una logica euristica da noi scritta per prendere decisioni di gioco attraverso la ricerca locale. L'IA valuta le mosse disponibili in base a una funzione di valutazione, cercando di massimizzare la propria posizione e minimizzare le possibilità dell’avversario. Attualmente, la strategia si concentra su:

- Protezione delle pedine singole
- Occupazione delle posizioni strategiche
- Uscita efficiente delle pedine dalla tavola
- Penalizzazione delle posizioni vulnerabili

## 📁 Struttura del progetto

```
BackgammonMG/
├── backgammon_ls.py       # Modulo IA per il computer player
├── backgammon_pvp.py         # Entry point del gioco
├── board.py              # Gestione del board e delle regole
└── README.md             # Documentazione del progetto
```

## ▶️ Come eseguire il gioco

Assicurati di avere installato Python 3.10 o superiore.

1. Clona il repository:
   ```bash
   git clone https://github.com/PeppPercoc/BackgammonMG.git
   cd BackgammonMG
   ```

2. Esegui il file principale:
   ```bash
   python3 backgammon_pvp.py
   ```

## ✅ Requisiti

- Python >= 3.10

## 📌 Stato del progetto

✅ Gioco base funzionante  
🚧 IA in fase di sviluppo e miglioramento  
🛠 Possibili future estensioni:
- Interfaccia grafica (GUI)
- Algoritmi IA più avanzati (Apprendimento per rinforzo)

## 👤 Autore

Progetto sviluppato da Paolo Martino [175974] e Mario Oreste Gallozzi [175082] 
Corso di Intelligenza Artificiale, Università degli Studi del Molise
