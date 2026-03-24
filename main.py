import time
import colorama

def chat(current_name_1):
	time.sleep(2)
	search_1 = input(colorama.Fore.CYAN + "Who do you talk to?: ")
	time.sleep(2)
	
	print(colorama.Fore.CYAN + f"Chat with {search_1}")
	
	while True:
		time.sleep(0.5)
		print(colorama.Fore.CYAN + f"You are {current_name_1}")
		time.sleep(0.5)
		msg_1 = input(colorama.Fore.CYAN + f"Message (Commands is /help): ")
		print(colorama.Fore.CYAN + msg_1)
		
		if msg_1.lower() == "/help":
			time.sleep(2)
			print(colorama.Fore.CYAN + "/q – Quit")
			time.sleep(0.5)
			print(colorama.Fore.CYAN + "/whoareu – Show a who do you talking to")
			time.sleep(0.5)
			print(colorama.Fore.CYAN + "/send – Send a your Telegram or messanger")
			time.sleep(0.5)
		
		elif msg_1.lower() == "/q":
			time.sleep(2)
			break
		
		elif msg_1.lower() == "/whoareu":
			time.sleep(2)
			print(colorama.Fore.CYAN + search_1)
		
		elif msg_1.lower() == "/send":
			time.sleep(2)
			send_1 = input(colorama.Fore.CYAN + "Please, enter a username of your social network: ")
			sn_1 = input(colorama.Fore.CYAN + "Please, enter a social network: ")
			time.sleep(2)
			print(colorama.Fore.CYAN + f"Hello, let's go to {sn_1}, it's cool there! My username is {send_1}!")
		
	

def main():
	time.sleep(0.5)
	ASCII = """
		╔════════════════════════════════════╗
		║  ████████╗███████╗██████╗ ███╗   ███╗
		║  ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║
		║     ██║   █████╗  ██████╔╝██╔████╔██║
		║     ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║
		║     ██║   ███████╗██║  ██║██║ ╚═╝ ██║
		║     ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝
		║  ████████╗ ██████╗                  ║
		║  ╚══██╔══╝██╔════╝                  ║
		║     ██║   ██║  ███╗                 ║
		║     ██║   ██║   ██║                 ║
		║     ██║   ╚██████╔╝                 ║
		║     ╚═╝    ╚═════╝                  ║
		╚═════════════════════════════════════╝
		 Terminal Telegram Client"""
	print(colorama.Fore.CYAN + ASCII)
	time.sleep(2)
	
	username_1 = input(colorama.Fore.CYAN + "Please, enter a your username: ")
	time.sleep(2)
	name_1 = input(colorama.Fore.CYAN + "Please. enter a your name: ")
	time.sleep(2)
	
	print(colorama.Fore.CYAN + "Good")
	time.sleep(2)
	print(colorama.Fore.CYAN + f"Your username is {username_1}, and your name is {name_1}")
	
	time.sleep(2)
	
	while True:
		print(colorama.Fore.CYAN + "1. Chat with somebody")
		time.sleep(0.5)
		print(colorama.Fore.CYAN + "2. Quit")
		time.sleep(0.5)
		
		main_1 = input(colorama.Fore.CYAN + "Choice: ")
		
		if main_1 == "1":
			time.sleep(2)
			chat(name_1)
			return
		
		elif main_1 == "2":
			time.sleep(2)
			break
		else:
			time.sleep(2)
			print(colorama.Fore.CYAN + "Please, enter a number 1 or 2")
			time.sleep(2)
	
if __name__ == "__main__":
	main()
