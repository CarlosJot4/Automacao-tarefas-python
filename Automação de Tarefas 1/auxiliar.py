# Pequeno script para pegar a posição atual do cursor do mouse após um atraso de 5 segundos.
# Será necessário para descobrir as coordenadas de clique na tela.
# Salve este código em um arquivo separado, por exemplo, auxiliar.py    
# Execute este script e posicione o cursor do mouse sobre o elemento desejado na tela antes 
# que o tempo acabe.
# O script imprimirá as coordenadas (x, y) no prompt/terminal.
# Você pode então usar essas coordenadas no script principal de automação.      

import pyautogui
import time

time.sleep(5) # espere 5 segundos para posicionar o cursor
print(pyautogui.position()) # imprime a posição atual do cursor no prompt