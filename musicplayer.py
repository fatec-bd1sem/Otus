from tkinter import *
import tkinter as tk
from pygame import mixer
import os 
import random
import pathlib
from PIL import Image
from PIL import ImageTk
class MP:

  
    def __init__(self, win):
        # Configurações da janela
        win.geometry('300x400')
        win.title('Otus Music Player')
        win.resizable(0, 0)


        # Configurações dos botões
        self.play_restart = tk.StringVar()
        self.pause_resume = tk.StringVar()
        self.play_restart.set('Next')
        self.pause_resume.set('Pause')


        next_button = Button(win, textvariable=self.play_restart, width=10, font=('Arial', 20), command=self.next)
        next_button.place(x=150, y=270, anchor='center')

        pause_button = Button(win, textvariable=self.pause_resume, width=10, font=('Arial', 20), command=self.pause)
        pause_button.place(x=150, y=350, anchor='center')


        
        self.playing_state = False
    
    def next(self):
        
        folder = str(pathlib.Path().resolve())
        path = f"{folder}\musicas"
        file = os.path.join(path, random.choice(os.listdir(path)))
        mixer.init()
        mixer.music.load(file)
        mixer.music.play()
    

    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state = True
            self.pause_resume.set('Resume')
        else:
            mixer.music.unpause()
            self.playing_state = False
            self.pause_resume.set('Pause')

# Iniciar a Musica aleatoria automaticamente
folder = str(pathlib.Path().resolve())
path = f"{folder}\musicas"
file = os.path.join(path, random.choice(os.listdir(path)))
mixer.init()
mixer.music.load(file)
mixer.music.play()
    
#DESENVOLVIMENTO DA INTERFACE
  
root= Tk()   
image = Image.open(f"{folder}/imagens/imgmusic.png")
photo = ImageTk.PhotoImage(image)
fundo = Label(root, image=photo,
                    background= "#0F2027")
fundo.image = image
fundo.place(x=50, y=20)
fundo.pack()


MP(root)
root.configure(background="#0F2027")
root.mainloop()

