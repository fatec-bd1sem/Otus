from keyboard import record

import pyttsx3 
import os
             
from utils import ouvir, procurar_comando

while True:
    print('PRESSIONE ENTER PARA FALAR')
    record(until="enter")
    frase = ouvir()
    comando_encontrado = procurar_comando(frase)
    #os.system('cls')



