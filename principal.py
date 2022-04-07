from keyboard import record

import pyttsx3 
import os
             
from utils import ouvir, procurar_comando, tocar

while True:
    print('PRESSIONE ENTER PARA FALAR')
    record(until="enter")
    tocar('start.mp3')
    frase = ouvir()
    comando_encontrado = procurar_comando(frase)
    #os.system('cls')



