import speech_recognition as sr
import os

#importa funções
from agenda import agenda
from desempenho import desempenho
from quiz import quiz

comandos = ['agenda','desempenho','quiz']
funcoes = [agenda, desempenho, quiz]


def procura_comando(frase):
    #separa frase em palavras para análise
    palavras = frase.split(' ')

    #confere cada palavra
    for palavra in palavras:
        #se a palavra for um comando, executa comando
        if palavra in comandos:
            numero_comando = comandos.index(palavra)
            funcoes[numero_comando]()
            break


rec = sr.Recognizer()
while True:
    with sr.Microphone() as mic:
        rec.adjust_for_ambient_noise(mic)
        audio=rec.listen(mic)
        try:
            frase=rec.recognize_google(audio,language="pt-BR")
            print(frase)
            procura_comando(frase)
 
        except:
            #speak('please, try again')
            print("erro")
os.system('pause')
