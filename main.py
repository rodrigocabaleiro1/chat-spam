import pyautogui,webbrowser
a=0
from time import sleep

webbrowser.open('Insert a chat link')

sleep(30)
while a==0:
    with open('spam.txt','r') as file:
        for line in file:
            pyautogui.typewrite(line)
            pyautogui.press('enter')
