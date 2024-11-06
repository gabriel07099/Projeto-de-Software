import pyautogui
import time

# Defina a posição onde o clique será realizado (x, y)
x, y = 1200, 1010  # Altere para as coordenadas desejadas
 
while True:
    pyautogui.click(x, y)
    time.sleep(180)  # Espera 15 segundos antes de clicar novamente