import pyfiglet
import time
from termcolor import colored
import pyautogui as pt
import pyautogui

text = pyfiglet.print_figlet(text="Spammer", colors="YELLOW", font="speed")
print(colored('Developed By Ja3oli', 'red'))

limit = input(colored("Nechta Habar Bo'lsin: " ,'blue'))
xabar = input(colored("Xabaringizni Kiriting: ", 'blue'))

i = 0

time.sleep(2)

# Xabaringiz Tezligi
pyautogui.PAUSE = 0.0330

while i<int(limit):

    pt.typewrite(xabar)
    pt.press("enter")

    i+=1
