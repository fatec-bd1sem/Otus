from cProfile import label
from tkinter import*
from PIL import Image
from PIL import ImageTk
import pathlib
from utils import ouvir, notificar_lembretes_hoje, comando_botao_ouvir
import threading
#from principal import comando_botao_ouvir



def Interface_principal():
    nossaTela = Tk()
    nossaTela.configure(background="#0F2027")
    nossaTela.geometry("580x400+350+100")
    nossaTela.title("Assistente Virtual OTUS")
    
    caminho_pasta = str(pathlib.Path().resolve())
    im=Image.open(caminho_pasta+"/imagens/agenda.1p.png")
    minhaimgem= ImageTk.PhotoImage(im)
    image1 = Label (nossaTela, image=minhaimgem,
                    compound= TOP,text = "Abrir Agenda",background="#0F2027",foreground="#FFFFFF")
    image1.image=minhaimgem
    
    image1.place(x=300,y=50)
    
    im2=Image.open(caminho_pasta+"/imagens/quizz.p.png")
    minhaimgem2= ImageTk.PhotoImage(im2)
    image2 = Label (nossaTela, image=minhaimgem2,
                    compound= TOP,text = "Abrir Guia de Estudo",background="#0F2027",foreground="#FFFFFF")
    
    image2.image=minhaimgem2
    image2.place(x=420,y=50)
    
    im3=Image.open(caminho_pasta+"/imagens/desempenho.png")
    minhaimgem3= ImageTk.PhotoImage(im3)
    image3 = Label (nossaTela, image=minhaimgem3,
                    compound= TOP,text = "Meu desempenho",background="#0F2027",foreground="#FFFFFF")

    image3.image=minhaimgem3
    image3.place(x=288,y=130)
    
    im4=Image.open(caminho_pasta+"/imagens/linguagem.png")
    minhaimgem4= ImageTk.PhotoImage(im4)
    image4 = Label (nossaTela, image=minhaimgem4,
                    compound= TOP,text = "Auxiliar de Linguagem",background="#0F2027",foreground="#FFFFFF")

    image4.image=minhaimgem4
    image4.place(x=415,y=130)
    
    im5=Image.open(caminho_pasta+"/imagens/calculadora.png")
    minhaimgem5= ImageTk.PhotoImage(im5)
    image5 = Label (nossaTela, image=minhaimgem5,
                    compound= TOP,text = "Abrir calculadora",background="#0F2027",foreground="#FFFFFF")

    image5.image=minhaimgem5
    image5.place(x=293,y=210)
    
    im6=Image.open(caminho_pasta+"/imagens/dica.png")
    minhaimgem6= ImageTk.PhotoImage(im6)
    image6= Label (nossaTela, image=minhaimgem6,
                    compound= TOP,text = "Dica",background="#0F2027",foreground="#FFFFFF")

    image6.image=minhaimgem6
    image6.place(x=449,y=210)
    
    im7=Image.open(caminho_pasta+"/imagens/artigo.png")
    minhaimgem7= ImageTk.PhotoImage(im7)
    image7 = Label (nossaTela, image=minhaimgem7,
                    compound= TOP,text = "Buscar artigos",background="#0F2027",foreground="#FFFFFF")

    image7.image=minhaimgem7
    image7.place(x=301,y=290)
    
    im8=Image.open(caminho_pasta+"/imagens/musicplayer.png")
    minhaimgem8= ImageTk.PhotoImage(im8)
    image8 = Label (nossaTela, image=minhaimgem8,
                    compound= TOP,text = "Tocar Música",background="#0F2027",foreground="#FFFFFF")

    image8.image=minhaimgem8
    image8.place(x=440,y=290)
    
    im9=Image.open(caminho_pasta+"/imagens/otus.png")
    minhaimgem9= ImageTk.PhotoImage(im9)
    image9 = Label (nossaTela, image=minhaimgem9,
                    text = "",background="#0F2027",foreground="#FFFFFF")
    image9.place(x=0,y=70)
    image9.image=minhaimgem9
    
    im5=Image.open(caminho_pasta+"/imagens/mic2.png")
    minhaimgem5= ImageTk.PhotoImage(im5)
    image5 = Button (nossaTela, image=minhaimgem5,command = comando_botao_ouvir, background="#0F2027")
    image5.place(x=90,y=290)
    image5.image=minhaimgem5
    
    text= Label(nossaTela,text="ASSISTENTE VIRTUAL",background="#0F2027",foreground="#FFFFFF",
                font="Verdana 12")
    text.place(x=38,y=20)
    text2= Label(nossaTela,text="COMANDOS DE INTERAÇÕES",background="#0F2027",foreground="#FF3535",
                    font="Verdana 12")
    text2.place(x=292,y=20)

    nossaTela.mainloop()
    
notificar_lembretes_hoje()
Interface_principal()


