from tkinter import ttk
from ttkthemes import ThemedTk
from tkinter import *
from utils import falar
import threading
import speech_recognition as sr
import timer
import time

#FILTRO DE AUDIO PARA DECISÃO APENAS SIM OU NÃO
def apurado():
    r = sr.Recognizer()
    mic = sr.Microphone()

    with mic as fonte:
        while True:
            try:
                r.adjust_for_ambient_noise(fonte)
                print("OUVINDO...")
                audio = r.listen(fonte)  # falar
                print("Enviando para reconhecimento...")
                resp = r.recognize_google(audio, language="pt-BR")

                if resp == "sim":
                    return (resp)
                    break

                if resp == "não":
                    return (resp)
                    break

                else:
                    falar("Diga 'SIM' ou 'NÃO'")
                    print("Diga 'SIM' ou 'NÃO'")

            except:
                falar("Não entendi, Desculpe, pode repetir ?")
                print("Não entendi, Desculpe, pode repetir ??")

#TITULO PERSONALIZADO
def titulo(msg):
    tam = len(msg) + 4
    print("~" * tam)
    print(f"  {msg}")
    print("~" * tam)
def Inicial():

    #interface
    interface = ThemedTk(theme="arc")
    interface.geometry('800x650+250+5')
    texto = ttk.Label(interface, text="BEM VINDO AO GUIA DE ESTUDOS",font=("Arial 19"), foreground='black')
    texto.place(relx=0.5, rely=0.2, anchor='center')
    texto = ttk.Label(interface, text="IREI AJUDAR A ENCONTRAR UMA NOVA TECNOLOGIA PARA VOCÊ ESTUDAR !",font=("Arial 15"), foreground='black')
    texto.place(relx=0.5, rely=0.4, anchor='center')
    texto = ttk.Label(interface, text="DIGA 'SIM' OU 'NÃO'",font=("Arial 17"), foreground='black')
    texto.place(relx=0.5, rely=0.6, anchor='center')
    # comandos
    threading.Thread(target=linguaj).start()
    interface.mainloop()




def linguaj():
    falar("Bem vindo ao guia de estudo !IREI AJUDAR A ENCONTRAR UMA NOVA TECNOLOGIA PARA VOCÊ ESTUDAR !, Diga SIM ou Não")
    esc = apurado()
    #interface
    # define tamanho da tela
    lg1 = ThemedTk(theme="arc")
    lg1.geometry('800x650+250+5')
    texto = ttk.Label(lg1, text="Deseja aprender uma linguagem orientada a objetos?",font=("Arial 20"), foreground='black')
    texto.place(relx=0.5, rely=0.5, anchor='center')
    #comandos
    if esc == "sim":
        threading.Thread(target=POOweb).start()
    lg1.mainloop()


def POOweb():
    falar("Deseja aprender uma linguagem orientada a objetos?")
    esc = apurado()
    #interface
    # define tamanho da tela
    lg4 = ThemedTk(theme="arc")
    lg4.geometry('800x650+250+5')
    texto232 = ttk.Label(lg4, text="Linguagem de plataforma WEB ?",font=("Arial 20"), foreground='black')
    texto232.place(relx=0.5, rely=0.5, anchor='center')
    #comandos
    if esc == "sim":
        threading.Thread(target=PERF).start()
        lg4.mainloop()
    else:
        threading.Thread(target=DeskTop).start()


#Progamação de Linguagens POO

def PERF():
    falar("Linguagens de plataforma WEB ?")
    esc = apurado()
    #interface
    # define tamanho da tela
    lg6 = ThemedTk(theme="arc")
    lg6.geometry('800x650+250+5')
    #comandos
    if esc == "sim":
        threading.Thread(target=PHPPOOR).start()

    else:
        threading.Thread(target=JAVAPOOR).start()
    lg6.mainloop()

def PHPPOOR():
    #interface
    # define tamanho da tela
    lg7 = ThemedTk(theme="arc")
    lg7.geometry('800x650+250+5')
    texto = ttk.Label(lg7, text="PHP & HTML5",font=("Arial 20"),foreground='black')
    texto.place(relx=0.5, rely=0.2, anchor='center')
    texto = ttk.Label(lg7, text="PHP é uma linguagem de script de uso geral popular que é especialmente adequada\n para desenvolvimento web. Rápido, tabulação e pragmático, o PHP potencializa tudo !",font=("Arial 14"),foreground='black')
    texto.place(relx=0.5, rely=0.4, anchor='center')
    texto2 = ttk.Label(lg7, text="https://www.cursoemvideo.com/curso/html5/",font=("Arial 20"),foreground='black')
    texto2.place(relx=0.5, rely=0.7, anchor='center')
    threading.Thread(target=PHPPOO).start()
    #comandos
    lg7.mainloop()
    lg7.command = lg7.destroy()

def PHPPOO():
    falar("P.H.P")
    falar("Aqui está o link que você poderá usar para começar seu conhecimento")
    #interface
    # define tamanho da tela
    lg77 = ThemedTk(theme="arc")
    lg77.geometry('800x650+250+5')
    #comandos

def JAVAPOOR():
    lg78 = ThemedTk(theme="arc")
    lg78.geometry('800x650+250+5')
    texto = ttk.Label(lg78, text="JAVA",font=("Arial 20"), foreground='black')
    texto.place(relx=0.5, rely=0.2, anchor='center')
    texto = ttk.Label(lg78, text="O Java é uma linguagem de programação orientada a objetos e é uma das linguagens \nmais utilizadas pelas empresas na atualidade no desenvolvimento de aplicações Mobile.",font=("Arial 14"), foreground='black')
    texto.place(relx=0.5, rely=0.4, anchor='center')
    texto2 = ttk.Label(lg78, text="https://www.cursoemvideo.com/curso/java-poo/",font=("Arial 20"),foreground='black')
    texto2.place(relx=0.5, rely=0.7, anchor='center')
    threading.Thread(target=JAVAPOO).start()
    lg78.mainloop()

def JAVAPOO():
    falar("JAVA")
    falar("Aqui está o link que você poderá usar para começar seu conhecimento")

#-----------------------------------------------------------------------------------------------------------------------

def DeskTop():
    lg440 = ThemedTk(theme="arc")
    lg440.geometry('800x650+250+5')
    texto = ttk.Label(lg440, text="Programação Desktop (Máquina local) ?",font=("Arial 20"),foreground='black')
    texto.place(relx=0.5, rely=0.5, anchor='center')
    # comandos
    threading.Thread(target=Desktop1).start()
    lg440.mainloop()

def Desktop1():
    falar("Programação Desktop (Máquina local) ?")
    esc = apurado()
    lgb4 = ThemedTk(theme="arc")
    lgb4.geometry('800x650+250+5')
    texto = ttk.Label(lgb4, text="Maior interatividade gráfica com o usuário ?",font=("Arial 20"),foreground='black')
    texto.place(relx=0.5, rely=0.5, anchor='center')
    # comandos
    if esc == "sim":
        threading.Thread(target=Desktop2).start()
        lgb4.mainloop()
    else:
        threading.Thread(target=BancoDADOS).start()


def Desktop2():
    falar("Maior interatividade gráfica com o usuário ?")
    esc = apurado()
    # interface
    # define tamanho da tela
    lgA = ThemedTk(theme="arc")
    lgA.geometry('800x650+250+5')
    # comandos
    if esc == "sim":
        threading.Thread(target=CSharpFace).start()
        lgA.mainloop()
    else:
        threading.Thread(target=PythonFace).start()


def CSharpFace():
    lg9 = ThemedTk(theme="arc")
    lg9.geometry('800x650+250+5')
    texto = ttk.Label(lg9, text="C#",font=("Arial 20"), foreground='black')
    texto.place(relx=0.5, rely=0.2, anchor='center')
    texto = ttk.Label(lg9, text="C# é uma linguagem de programação, multiparadigma, de tipagem forte, \ndesenvolvida pela Microsoft como parte da plataforma .NET",font=("Arial 14"), foreground='black')
    texto.place(relx=0.5, rely=0.4, anchor='center')
    texto2 = ttk.Label(lg9, text="https://www.youtube.com/watch?v=dVzJ3bx68FA&list=PLx4x_zx8csUglgKTmgfVFE",font=("Arial 14"),foreground='black')
    texto2.place(relx=0.5, rely=0.6, anchor='center')
    threading.Thread(target=CSharpAudio).start()

    lg9.mainloop()
    StopIteration

def CSharpAudio():
    falar("C.Sharp")
    falar("Aqui está o link que você poderá usar para começar seu conhecimento")
    # comandos

def PythonFace():
    lg4556 = ThemedTk(theme="arc")
    lg4556.geometry('800x650+250+5')
    texto = ttk.Label(lg4556, text="C#",font=("Arial 20"), foreground='black')
    texto.place(relx=0.5, rely=0.2, anchor='center')
    texto = ttk.Label(lg4556, text="Python é uma linguagem de programação de alto nível, interpretada de script, \nimperativa, orientada a objetos, funcional, de tipagem dinâmica e forte.",font=("Arial 14"), foreground='black')
    texto.place(relx=0.5, rely=0.4, anchor='center')
    texto2 = ttk.Label(lg4556, text="https://www.youtube.com/watch?v=dVzJ3bx68FA&list=PLx4x_zx8csUglgKTmgfVFE",font=("Arial 14"),foreground='black')
    texto2.place(relx=0.5, rely=0.6, anchor='center')
    threading.Thread(target=PythonAudio).start()
    # comandos
    lg4556.mainloop()

def PythonAudio():
    falar("Paiton")
    falar("Aqui está o link que você poderá usar para começar seu conhecimento")


def BancoDADOS():
    #interface
    # define tamanho da tela
    lg02 = ThemedTk(theme="arc")
    lg02.geometry('800x650+250+5')
    texto = ttk.Label(lg02, text="MySQL",font=("Arial 20"), foreground='black')
    texto.place(relx=0.5, rely=0.2, anchor='center')
    texto = ttk.Label(lg02, text="O MySQL é um sistema de gerenciamento de banco de dados, \nque utiliza a linguagem SQL como interface.",font=("Arial 14"), foreground='black')
    texto.place(relx=0.5, rely=0.4, anchor='center')
    texto2 = ttk.Label(lg02, text="https://www.cursoemvideo.com/curso/mysql/",font=("Arial 14"),foreground='black')
    texto2.place(relx=0.5, rely=0.6, anchor='center')
    threading.Thread(target=BancoDADOSAud).start()
    #comandos
    lg02.mainloop()

def BancoDADOSAud():
    falar("Recomendamos programação e estruturação em banco de dados My S Q L")
    falar("Aqui está o link que você poderá usar para começar seu conhecimento")

def quiz():
    threading.Thread(target=Inicial).start()
    












