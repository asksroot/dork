import os
import time

os.system("clear")
os.system("pip install --upgrade pip")
os.system("pip install googlesearch")
os.system("pip install google")
os.system("pip install search")
os.system("pip install beautifilsoup4")
os.system("pip install termcolor")
os.system("pip install colored")
os.system("pip install time")
os.system("clear")

def progress_bar(done):
    print("\rIniciando Sua Dork... {0:50s}{1:.1f}%".format('#' * int(done * 100), done * 100),end='')
def test():
    for n in range(3):
        progress_bar(n/100)
        time.sleep(1)
test()
os.system("clear && python3 sqldork.py")