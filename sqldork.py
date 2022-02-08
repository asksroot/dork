from googlesearch import search
import os
import termcolor
from termcolor import colored

main = 0
root = 0
print(colored("""
_____             _    
|  __ \           | |   
| |  | | ___  _ __| | __
| |  | |/ _ \| '__| |/ /
| |__| | (_) | |  |   < 
|_____/ \___/|_|  |_|\_\
                   
                     """, "red"))
class Application():
	def __init__(self):
		self.root = root
		self.main = main
		self.home()

	def home(self):
		while True:
			if(main == main):
				dork = ""
				
				class RootApplication():
					def __init__(self):
						self.dork = dork
						self.input()
						
					def input(self):
						if(dork == dork):
							inurl = str(input(colored("#|D|o|r|k|-->> ", "blue")))
							for y in search(inurl, tld="co.in",
							 num=10,
							 stop=10,
							 pause=2):
							 	print(y)
							 	print(colored("------->>", "yellow"))
				RootApplication()
Application()