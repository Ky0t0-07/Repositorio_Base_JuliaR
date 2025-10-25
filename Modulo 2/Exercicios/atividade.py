'''
Vamos fazer o pyautogui entrar no youtube
------------------------
instalei e ativei o venv
Istalei o pyautogui no terminal: pip install pyautogui
importar o time e pyautogui
'''
import time
import pyautogui

pyautogui.click (x=1190 , y=1055)
#clicar no icone do google na barra de tarevas
pyautogui.click (x=745 , y=36)
#clicar em nova aba
pyautogui.typewrite('youtube')
#escrever youtube na area de pesquisa
pyautogui.press ('enter')
#apertar a tecla enter
time.sleep(2)
#esperar um pouco para a pag carregar
pyautogui.click (x=99 , y=329)
#clicar no link do youtube