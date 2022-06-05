import os
import threading
from tkinter import ttk
global interface

def limpar():
    texto = ttk.Label(interface, text="IREI AJUDAR A ENCONTRAR UMA NOVA TECNOLOGIA PARA VOCÊ ESTUDAR !",
                      font=("Arial 20"), foreground='#0F2027', background='#0F2027')
    texto.place(relx=0.5, rely=0.5) #Ff#fu

#FUNÇÃO PARA LIMPAR LABEL CONJUNTOS
def limparF():
    texto2 = ttk.Label(interface, text="&&&&&&&&&&&&&&&&&&&&&&&&&&&",
                      font=("Arial 20"), foreground='#0F2027', background='#0F2027')
    texto2.place(relx=0.1, rely=0.6)

    texto2 = ttk.Label(interface, text="&&&&&&&&&&&&&&&&&&&&&&&&&&&&",font=("Arial 25"), foreground='#0F2027', background='#0F2027')
    texto2.place(relx=0.1, rely=0.8,)

def falar(frase):
    import pyttsx3
    #iniciando fala
    engine = pyttsx3.init()
    engine.say(frase)
    engine.runAndWait()

def ouvir():
    import speech_recognition as sr
    comando_encontrado = False
    rec = sr.Recognizer()

    while True:
        # caso tenha encontrado comando, para de ouvir
        if (comando_encontrado):
            os.system('cls')
            break

        # caso não tenha encontrado comando, continua ouvindo
        else:
            print('OUVINDO...')
            with sr.Microphone() as mic:
                rec.adjust_for_ambient_noise(mic)
                audio = rec.listen(mic)
                try:
                    # envia áudio para o google
                    frase = rec.recognize_google(audio, language="pt-BR")
                    print(f'Você disse: {frase}')
                    return frase

                except:
                    # speak('please, try again')
                    print("erro")
                    pass

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

def tocar(audio):
    from pygame import mixer
    import pathlib
    caminho_pasta = str(pathlib.Path().resolve())
    caminho_audio = f"{caminho_pasta}\Audios\{audio}"
    mixer.init()
    mixer.music.load(caminho_audio)
    mixer.music.play()

def plano_cartesiano():
    # zerando caminho para importar funções de diretórios acima
    import sys
    sys.path.append('')

    import threading
    from PIL import ImageTk, Image
    from tkinter import ttk, Tk
    import tkinter as tk

    print('função plano_cartesiano chamada')
    global interface
    interface = Tk()
    image = Image.open("imagens\\fundo_consult.png")
    photo = ImageTk.PhotoImage(image, master=interface)
    fundo = tk.Label(interface, image=photo)
    fundo.image = image
    fundo.pack()
    interface.geometry('800x650+250+5')
    interface.title("Plano Cartesiano")
    texto = ttk.Label(interface, text="Produto Cartesiano!", font=("Arial 17"),
                      foreground='white', background='#0F2027')
    texto.place(relx=0.5, rely=0.4, anchor='center')
    threading.Thread(target=produto_cartesianoP).start() #executar função simultaneamente com interface
    interface.mainloop() #executa a abertura da interface

def produto_cartesianoP():
    receptor = ''
    conjunto_A = []
    conjunto_B = []
    cont = 1
    falar("Produto Cartesiano!")

    #CONJUNTO [A]
    while receptor != 'fechar':
        cont_frase = str(cont)      #contador do numero de elemento
        frase = "diga o " + cont_frase + "º elemento do conjunto A ou diga FECHAR"
        print(limpar())             #limpar label para que possa ser coloada na tela
        texto = ttk.Label(interface, text=frase, font=("Arial 20"),foreground='white', background='#0F2027')
        texto.place(relx=0.5, rely=0.4, anchor='center')
        falar(frase)
        threading.Thread(target=tocar, args=["start.mp3"]).start()
        receptor = ouvir()
        threading.Thread(target=tocar, args=["success.mp3"]).start()

        if receptor == "fechar":
            break

        else:
            try:
                #CONVERSÃO DE NUMEROS PARA INTEIROS
                receptor = int(receptor)
                conjunto_A.append(receptor)
                print(conjunto_A)

            except:
                #FATIAMENTO DE STR
                falar("Você deve dizer apenas uma letra")
                coletor = receptor[0:1]
                frase = "Você quis dizer a letra "+coletor
                print(frase)#label
                falar(frase)
                print(limpar())
                falar("Diga SIM ou NÃO")
                cheque = refinar()
                if cheque == "sim":
                    #ADICIONA PRIMEIRA LETRA DA FRASE
                    conjunto_A.append(coletor)
                else:
                    cont = cont - 1

        #RESULTADO ATUAL DO CONJUNTO
        print(limpar())
        texto2 = ttk.Label(interface, text="Conjunto A = " + str( conjunto_A), font=("Arial 17"), foreground='white', background='#0F2027')
        texto2.place(relx=0.1, rely=0.6)

        cont = cont +1

    receptorB = ''
    contB = 1

    #CONJUNTO [B]
    while receptorB != 'fechar':
        cont_frase = str(contB)      #contador do numero de elemento
        frase = "diga o " + cont_frase + "º elemento do conjunto B ou diga FECHAR"
        print(limpar())             #limpar label para que possa ser coloada na tela
        texto = ttk.Label(interface, text=frase, font=("Arial 20"),foreground='white', background='#0F2027')
        texto.place(relx=0.5, rely=0.4, anchor='center')
        falar(frase)
        threading.Thread(target=tocar, args=["start.mp3"]).start()
        receptorB = ouvir()
        threading.Thread(target=tocar, args=["success.mp3"]).start()

        if receptorB == "fechar":
            break

        else:
            try:
                receptorB = int(receptorB)
                conjunto_B.append(receptorB)
                print(conjunto_B)

            except:
                falar("Você deve dizer apenas uma letra")
                coletor = receptorB[0:1]
                frase = "Você quis dizer a letra "+coletor
                print(frase)#label
                falar(frase)
                print(limpar())
                falar("Diga SIM ou NÃO")
                cheque = refinar()
                if cheque == "sim":
                    conjunto_B.append(coletor)
                else:
                    contB = contB - 1

        print(limpar())
        texto2 = ttk.Label(interface, text="Conjunto B = " + str( conjunto_B), font=("Arial 17"), foreground='white', background='#0F2027')
        texto2.place(relx=0.1, rely=0.8)

        contB = contB +1

    #VERIFICAÇÃO DE QUAL CONTA LÓGICA USUARIO IRÁ ESCOLHER
    print(limparF())
    texto2 = ttk.Label(interface, text="'Primeira' [ AxB ]  // 'Segunda' [ BxA ] ", font=("Arial 15"), foreground='white', background='#0F2027')
    texto2.place(relx=0.1, rely=0.6)
    falar("Diga qual seguinte opção deseja?")
    threading.Thread(target=tocar, args=["start.mp3"]).start()
    escolha = ouvir()
    threading.Thread(target=tocar, args=["success.mp3"]).start()

    #TITULO FINAL
    print(limparF())
    print(limpar())
    texto = ttk.Label(interface, text="- - - - SEU PRODUTO CARTESIANO - - - -", font=("Arial 25"), foreground='white', background='#0F2027')
    texto.place(relx=0.5, rely=0.4, anchor='center')


    #CODIFICAÇÃO DA CONTA LÓGICA
    if escolha == "primeira":
        res = [(a, b) for a in conjunto_A for b in conjunto_B]
        print("The Cartesian Product is : " + str(res))
        texto2 = ttk.Label(interface, text="AxB = " + str(res), font=("Arial 12"), foreground='white',background='#0F2027')
        texto2.place(relx=0.1, rely=0.6)


    else:
        res = [(a, b) for a in conjunto_B for b in conjunto_A]
        print("The Cartesian Product is : " + str(res))
        texto2 = ttk.Label(interface, text="BxA = " + str(res), font=("Arial 12"), foreground='white',background='#0F2027')
        texto2.place(relx=0.1, rely=0.6)
