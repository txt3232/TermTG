import time
import colorama

def group(current_name_1):
	time.sleep(2)
	print(colorama.Fore.CYAN + " Who do you're wanna add to group?")
	time.sleep(0.5)
	member_1 = input(colorama.Fore.GREEN + "Who is first member?: ")
	time.sleep(0.5)
	member_2 = input(colorama.Fore.BLUE + "Who is second member?: ")
	time.sleep(0.5)
	member_3 = input(colorama.Fore.YELLOW + "Who is third member?: ")
	time.sleep(0.5)
	member_4 = input(colorama.Fore.MAGENTA + "Who is 4th member?: ")
	time.sleep(2)
	
	while True:
		print(colorama.Fore.CYAN + "Chat with group")
		time.sleep(0.5)
		print(colorama.Fore.CYAN + f"You are {current_name_1}")
		time.sleep(0.5)
		msg_1 = input(colorama.Fore.CYAN + f"Message (Commands is /help): ")
		print(colorama.Fore.CYAN + msg_1)
		time.sleep(0.5)
		
		print(colorama.Fore.GREEN + "Chat with group")
		time.sleep(0.5)
		print(colorama.Fore.GREEN + f"You are {member_1}")
		time.sleep(0.5)
		msg_2 = input(colorama.Fore.GREEN + f"Message (Commands is /help): ")
		print(colorama.Fore.GREEN + msg_2)
		time.sleep(0.5)
		
		print(colorama.Fore.BLUE + "Chat with group")
		time.sleep(0.5)
		print(colorama.Fore.BLUE + f"You are {member_2}")
		time.sleep(0.5)
		msg_3 = input(colorama.Fore.BLUE + f"Message (Commands is /help): ")
		print(colorama.Fore.BLUE + msg_3)
		time.sleep(0.5)
		
		print(colorama.Fore.YELLOW + "Chat with group")
		time.sleep(0.5)
		print(colorama.Fore.YELLOW + f"You are {member_3}")
		time.sleep(0.5)
		msg_4 = input(colorama.Fore.YELLOW + f"Message (Commands is /help): ")
		print(colorama.Fore.YELLOW + msg_4)
		time.sleep(0.5)
		
		print(colorama.Fore.MAGENTA + "Chat with group")
		time.sleep(0.5)
		print(colorama.Fore.MAGENTA + f"You are {member_4}")
		time.sleep(0.5)
		msg_5 = input(colorama.Fore.MAGENTA + f"Message (Commands is /help): ")
		print(colorama.Fore.MAGENTA + msg_5)
		time.sleep(0.5)
		
		if msg_1.lower() == "/help":
			time.sleep(2)
			print(colorama.Fore.CYAN + "/q – Quit")
			time.sleep(0.5)
			print(colorama.Fore.CYAN + "/send – Send a your Telegram or messanger")
			time.sleep(0.5)
		
		elif msg_1.lower() == "/q":
			time.sleep(2)
			break
		
		elif msg_1.lower() == "/send":
			time.sleep(2)
			send_1 = input(colorama.Fore.CYAN + "Please, enter a username of your social network: ")
			sn_1 = input(colorama.Fore.CYAN + "Please, enter a social network: ")
			time.sleep(2)
			print(colorama.Fore.CYAN + f"Hello, let's go to {sn_1}, it's cool there! My username is {send_1}!")
			
		if msg_2.lower() == "/help":
			time.sleep(2)
			print(colorama.Fore.GREEN + "/q – Quit")
			time.sleep(0.5)
			print(colorama.Fore.GREEN + "/send – Send a your Telegram or messanger")
			time.sleep(0.5)
		
		elif msg_2.lower() == "/q":
			time.sleep(2)
			break
		
		elif msg_2.lower() == "/send":
			time.sleep(2)
			send_2 = input(colorama.Fore.GREEN + "Please, enter a username of your social network: ")
			sn_2 = input(colorama.Fore.GRREN + "Please, enter a social network: ")
			time.sleep(2)
			print(colorama.Fore.GREEN + f"Hello, let's go to {sn_2}, it's cool there! My username is {send_2}!")
		
		if msg_3.lower() == "/help":
			time.sleep(2)
			print(colorama.Fore.BLUE + "/q – Quit")
			time.sleep(0.5)
			print(colorama.Fore.BLUE + "/send – Send a your Telegram or messanger")
			time.sleep(0.5)
		
		elif msg_3.lower() == "/q":
			time.sleep(2)
			break
		
		elif msg_3.lower() == "/send":
			time.sleep(2)
			send_3 = input(colorama.Fore.BLUE + "Please, enter a username of your social network: ")
			sn_3 = input(colorama.Fore.BLUE + "Please, enter a social network: ")
			time.sleep(2)
			print(colorama.Fore.BLUE + f"Hello, let's go to {sn_3}, it's cool there! My username is {send_3}!")
		
		if msg_4.lower() == "/help":
			time.sleep(2)
			print(colorama.Fore.YELLOW + "/q – Quit")
			time.sleep(0.5)
			print(colorama.Fore.YELLOW + "/send – Send a your Telegram or messanger")
			time.sleep(0.5)
		
		elif msg_4.lower() == "/q":
			time.sleep(2)
			break
		
		elif msg_4.lower() == "/send":
			time.sleep(2)
			send_4 = input(colorama.Fore.YELLOW + "Please, enter a username of your social network: ")
			sn_4 = input(colorama.Fore.YELLOW + "Please, enter a social network: ")
			time.sleep(2)
			print(colorama.Fore.YELLOW + f"Hello, let's go to {sn_4}, it's cool there! My username is {send_4}!")
		
		if msg_5.lower() == "/help":
			time.sleep(2)
			print(colorama.Fore.MAGENTA + "/q – Quit")
			time.sleep(0.5)
			print(colorama.Fore.MAGENTA + "/send – Send a your Telegram or messanger")
			time.sleep(0.5)
		
		elif msg_5.lower() == "/q":
			time.sleep(2)
			break
		
		elif msg_5.lower() == "/send":
			time.sleep(2)
			send_5 = input(colorama.Fore.MAGENTA + "Please, enter a username of your social network: ")
			sn_5 = input(colorama.Fore.MAGENTA + "Please, enter a social network: ")
			time.sleep(2)
			print(colorama.Fore.MAGENTA + f"Hello, let's go to {sn_5}, it's cool there! My username is {send_5}!")
		
	

def chat(current_name_1):
	time.sleep(2)
	search_1 = input(colorama.Fore.CYAN + "Who do you talk to?: ")
	time.sleep(2)
	
	while True:
		time.sleep(0.5)
		print(colorama.Fore.CYAN + f"Chat with {search_1}")
		time.sleep(0.5)
		print(colorama.Fore.CYAN + f"You are {current_name_1}")
		time.sleep(0.5)
		msg_1 = input(colorama.Fore.CYAN + f"Message (Commands is /help): ")
		print(colorama.Fore.CYAN + msg_1)
		
		time.sleep(0.5)
		print(colorama.Fore.GREEN + f"Chat with {current_name_1}")
		time.sleep(0.5)
		print(colorama.Fore.GREEN + f"You are {search_1}")
		time.sleep(0.5)
		msg_2 = input(colorama.Fore.GREEN + f"Message (Commands is /help): ")
		print(colorama.Fore.GREEN + msg_2)
		
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
		
		if msg_2.lower() == "/help":
			time.sleep(2)
			print(colorama.Fore.GREEN + "/q – Quit")
			time.sleep(0.5)
			print(colorama.Fore.GREEN + "/whoareu – Show a who do you talking to")
			time.sleep(0.5)
			print(colorama.Fore.GREEN + "/send – Send a your Telegram or messanger")
			time.sleep(0.5)
		
		elif msg_2.lower() == "/q":
			time.sleep(2)
			break
		
		elif msg_2.lower() == "/whoareu":
			time.sleep(2)
			print(colorama.Fore.CYAN + current_name_1)
		
		elif msg_2.lower() == "/send":
			time.sleep(2)
			send_2 = input(colorama.Fore.GREEN + "Please, enter a username of your social network: ")
			sn_2 = input(colorama.Fore.GREEN + "Please, enter a social network: ")
			time.sleep(2)
			print(colorama.Fore.GREEN + f"Hello, let's go to {sn_2}, it's cool there! My username is {send_2}!")
	

def main():
	time.sleep(0.5)
	ASCII = """
	┌─────────────────────────────────────┐
	│  ████████╗███████╗██████╗ ███╗   ███╗
	│  ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║
	│     ██║   █████╗  ██████╔╝██╔████╔██║
	│     ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║
	│     ██║   ███████╗██║  ██║██║ ╚═╝ ██║
	│     ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝
	│  ████████╗ █████╗ ██╗     ██╗  ██╗
	│  ╚══██╔══╝██╔══██╗██║     ██║ ██╔╝
	│     ██║   ███████║██║     █████╔╝ 
	│     ██║   ██╔══██║██║     ██╔═██╗ 
	│     ██║   ██║  ██║███████╗██║  ██╗
	│     ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
	└─────────────────────────────────────┘
     Terminal Messenger   V: 0.0.3"""
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
		print(colorama.Fore.CYAN + "2. Group")
		time.sleep(0.5)
		print(colorama.Fore.CYAN + "3. News")
		time.sleep(0.5)
		print(colorama.Fore.CYAN + "4. About")
		time.sleep(0.5)
		print(colorama.Fore.CYAN + "5. Quit")
		time.sleep(0.5)
		
		main_1 = input(colorama.Fore.CYAN + "Choice: ")
		
		if main_1 == "1":
			time.sleep(2)
			chat(name_1)
			return
		
		elif main_1 == "2":
			time.sleep(2)
			group(name_1)
			return
		elif main_1 == "3":
			time.sleep(2)
			print(colorama.Fore.CYAN + "1. Added page a news. 2. Added page a about. 3. Added group.")
		elif main_1 == "4":
			time.sleep(2)
			print(colorama.Fore.CYAN + "About")
			time.sleep(2)
			print(colorama.Fore.CYAN + "  TermTG is messenger for terminal on Python, full release will in V: 1.0.0")
			time.sleep(2)
			print(colorama.Fore.CYAN + "My GitHub: https://github.com/txt3232/")
			time.sleep(2)
		elif main_1 == "5":
			time.sleep(2)
			break
		else:
			time.sleep(2)
			print(colorama.Fore.CYAN + "Please, enter a number (1/4)")
			time.sleep(2)
	
if __name__ == "__main__":
	main()
