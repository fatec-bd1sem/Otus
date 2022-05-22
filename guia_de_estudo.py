from tkinter import *
from utils import falar, ouvir, tocar
import threading
from PIL import ImageTk, Image
from tkinter import ttk, Tk
import tkinter as tk

#função para limitar resposta apenas para sim e não
def refinar():
    esc = ""
    while esc != "sim" or esc != "não":
        threading.Thread(target=tocar, args=["start.mp3"]).start()
        esc = ouvir()
        threading.Thread(target=tocar, args=["success.mp3"]).start()
        if esc == "sim":
            return (esc)

        if esc == "não":
            return (esc)

        else:
            falar("Diga 'SIM' ou 'NÃO'")
            print("Diga 'SIM' ou 'NÃO'")

#comando para limpar label
def limpar():
    texto = ttk.Label(interface, text="IREI AJUDAR A ENCONTRAR UMA NOVA TECNOLOGIA PARA VOCÊ ESTUDAR !",
                      font=("Arial 15"), foreground='#0F2027', background='#0F2027')
    texto.place(relx=0.5, rely=0.5, anchor='center')
    texto = ttk.Label(interface, text="IREI AJUDAR A ENCONTRAR UMA NOVA TECNOLOGIA PARA VOCÊ ESTUDAR !",
                      font=("Arial 15"), foreground='#0F2027', background='#0F2027')
    texto.place(relx=0.5, rely=0.6, anchor='center')
    texto = ttk.Label(interface, text="DIGA SIM OU NÃO", font=("Arial 17"), foreground='#0F2027', background='#0F2027')
    texto.place(relx=0.5, rely=0.7, anchor='center')

#programa
def questionario():
    texto = ttk.Label(interface, text="BEM VINDO AO GUIDA DE ESTUDOS", font=("Arial 17"), foreground='white', background='#0F2027')
    texto.place(relx=0.5, rely=0.5, anchor='center')
    texto = ttk.Label(interface, text="IREI AJUDAR A ENCONTRAR UMA NOVA TECNOLOGIA PARA VOCÊ ESTUDAR !",font=("Arial 15"),foreground='white', background='#0F2027')
    texto.place(relx=0.5, rely=0.6, anchor='center')
    texto = ttk.Label(interface, text="DIGA SIM OU NÃO", font=("Arial 17"), foreground='white', background='#0F2027')
    texto.place(relx=0.5, rely=0.7, anchor='center')
    falar("Bem vindo ao guia de estudo !IREI AJUDAR A ENCONTRAR UMA NOVA TECNOLOGIA PARA VOCÊ ESTUDAR !, Diga SIM ou Não")
    resp = refinar()
    print(limpar())

    if resp == "sim":
        texto = ttk.Label(interface, text="Deseja aprender uma linguagem orientada a objetos?", font=("Arial 17"), foreground='white',
                          background='#0F2027')
        texto.place(relx=0.5, rely=0.5, anchor='center')
        falar("Deseja aprender uma linguagem orientada a objetos?")
        resp = refinar()
        print(limpar())

        #Linguagem orientada a objetos
        if resp == "sim":
            texto = ttk.Label(interface, text="Linguagem de plataforma WEB?", font=("Arial 17"), foreground='white', background='#0F2027')
            texto.place(relx=0.5, rely=0.5, anchor='center')
            falar("Linguagem de plataforma WEB?")
            resp = refinar()
            print(limpar())

            if resp == "sim":

                texto = ttk.Label(interface, text="PHP", font=("Arial 17"), foreground='white', background='#0F2027')
                texto.place(relx=0.5, rely=0.5, anchor='center')
                texto = ttk.Label(interface, text="PHP é uma linguagem de script de uso geral popular que é especialmente adequada\n para desenvolvimento web. Rápido, tabulação e pragmático, o PHP potencializa tudo !",
                                  font=("Arial 15"), foreground='white', background='#0F2027')
                texto.place(relx=0.5, rely=0.6, anchor='center')
                falar("PHP é uma linguagem de script de uso geral popular que é especialmente adequada para desenvolvimento web. Rápido, tabulação e pragmático, o PHP potencializa tudo !")

            else:
                texto = ttk.Label(interface, text="Linguagem de plataforma Mobile ?", font=("Arial 17"), foreground='white',
                                  background='#0F2027')
                texto.place(relx=0.5, rely=0.5, anchor='center')
                falar("Linguagem de plataforma Mobile?")
                resp = refinar()
                print(limpar())

                if resp == "sim":

                    texto = ttk.Label(interface, text="JAVA", font=("Arial 17"), foreground='white', background='#0F2027')
                    texto.place(relx=0.5, rely=0.5, anchor='center')
                    texto = ttk.Label(interface, text="O Java é uma linguagem de programação orientada a objetos e é uma das linguagens \nmais utilizadas pelas empresas na atualidade no desenvolvimento de aplicações Mobile.",
                                      font=("Arial 15"), foreground='white', background='#0F2027')
                    texto.place(relx=0.5, rely=0.6, anchor='center')
                    falar("O Java é uma linguagem de programação orientada a objetos e é uma das linguagens mais utilizadas pelas empresas na atualidade no desenvolvimento de aplicações Mobile.")

                else:

                    texto = ttk.Label(interface, text="Linguagem de plataforma Desktop? (Máquina Local)", font=("Arial 17"),
                                          foreground='white', background='#0F2027')
                    texto.place(relx=0.5, rely=0.5, anchor='center')
                    falar("Linguagem de plataforma Desktop? (Máquina Local)")
                    resp = refinar()
                    print(limpar())

                    if resp == "sim":
                        texto = ttk.Label(interface, text="C#", font=("Arial 17"), foreground='white',
                                              background='#0F2027')
                        texto.place(relx=0.5, rely=0.5, anchor='center')
                        texto = ttk.Label(interface,
                                              text="C# é uma linguagem de programação, multiparadigma, de tipagem forte, \ndesenvolvida pela Microsoft como parte da plataforma .NET",
                                              font=("Arial 15"), foreground='white', background='#0F2027')
                        texto.place(relx=0.5, rely=0.6, anchor='center')
                        falar("C sharp é uma linguagem de programação, multiparadigma, de tipagem forte,desenvolvida pela Microsoft como parte da plataforma dót NET")

                    else:

                        texto = ttk.Label(interface, text="Python", font=("Arial 17"), foreground='white', background='#0F2027')
                        texto.place(relx=0.5, rely=0.5, anchor='center')
                        texto = ttk.Label(interface, text="Python é uma linguagem de programação de alto nível, interpretada de script, \nimperativa, orientada a objetos, funcional, de tipagem dinâmica e forte.",
                                          font=("Arial 15"), foreground='white', background='#0F2027')
                        texto.place(relx=0.5, rely=0.6, anchor='center')
                        falar("Paiton é uma linguagem de programação de alto nível, interpretada de script,imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte.")

        else:
            #direciona para banco de dados
            texto = ttk.Label(interface, text="Banco de Dados MySQL", font=("Arial 17"), foreground='white', background='#0F2027')
            texto.place(relx=0.5, rely=0.5, anchor='center')
            texto = ttk.Label(interface,
                              text="O MySQL é um sistema de gerenciamento de banco de dados,\n que utiliza a linguagem SQL com recurso de interface gráfica.",
                              font=("Arial 15"), foreground='white', background='#0F2027')
            texto.place(relx=0.5, rely=0.6, anchor='center')
            falar("O My SQL é um sistema de gerenciamento de banco de dados que utiliza a linguagem SQL com recurso de interface gráfica.")

    else:
        texto = ttk.Label(interface, text="Volte mais tarde ! até mais !", font=("Arial 17"), foreground='white',
                          background='#0F2027')
        texto.place(relx=0.5, rely=0.5, anchor='center')
        falar("Linguagem de plataforma WEB?")
        falar("Volte mais tarde ! até mais !")


#interface
def guia_de_estudo():
    global interface
    interface = Tk()
    image = Image.open("imagens\\fundo_consult.png")
    photo = ImageTk.PhotoImage(image, master=interface)
    fundo = tk.Label(interface, image=photo)
    fundo.image = image
    fundo.pack()
    interface.geometry('800x650+250+5')
    interface.title("Guia de estudo")
    threading.Thread(target=questionario).start() # executar função simultaneamente com interface
    interface.mainloop() #executa a abertura da interface
