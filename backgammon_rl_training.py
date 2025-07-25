from board import Board
from backgammon_rl import reinforcement_learning
import random
import time

exitTerms = "q"
def main():
	agent = reinforcement_learning()
	print("Loading previous experience")
	agent.upload_experiences_w("experience_w.json")
	agent.upload_experiences_b("experience_b.json")
	print("Training...")
	print("How many matches to play?")
	match = input()
	print("How many episodes per match?")
	episodes = input()
	for i in range(int(match)):
		if(agent.training(int(episodes))):
			print("Match no: ")
			print(i)
			#print("Saving white experience")
			#agent.save_experiences_w("experience_w.json")
		else:
			print("Match no: ")
			print(i)
			#print("Saving black experience")
			#agent.save_experiences_b("experience_b.json")
	print("Saving white experience")
	agent.save_experiences_w("experience_w.json")
	print("Saving black experience")
	agent.save_experiences_b("experience_b.json")
	print("Training completed! Now the AI is ready to play.")

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
	start_time = time.time()
	main()
	end_time = time.time()
	elapsed_time = end_time - start_time
	print(f"Il training ha richiesto {elapsed_time:.2f} secondi.")
