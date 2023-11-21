import os
import discord
from colorama import Fore, Back, init
import time
#init(autoreset=True)



class destruir(discord.Client):
	async def on_ready(self):
		#define
		canal = self.get_channel(1176321051270058004)
		#defineacabou
		print(f"{Fore.RED}iniciando o ataque")
		
		print("ataque iniciado")
		await canal.send("atacar")
				
		





if __name__ == "__main__":
	tempo = int(input(f"Tempo de ataque: {Fore.CYAN}"))
	token = str(input(f"{Fore.YELLOW}Token: "))
	for i in range(tempo):
		i + 1
		print(f"{Fore.WHITE}{Back.RED}{i}")
		time.sleep(1)
		if i >= tempo:
			break
	
	intents = discord.Intents.all()	
	rodar = destruir(intents=intents)
	rodar.run(token)		

