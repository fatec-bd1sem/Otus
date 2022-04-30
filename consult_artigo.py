import webbrowser
from utils import tocar
from tkinter import ttk
from tkinter import *
from utils import falar
from utils import ouvir
import threading

#----------------------------------------------------------------------------------------------------------

#programa alojado dentro da função para ser executado simultaneamente com a interface
def consult_art():
    while True:
        falar('DIGA O NÚMERO DO ITEM QUE DESEJA PESQUISAR EM VOZ ALTA:')
        threading.Thread(target=tocar, args=["start.mp3"]).start()
        escolha = ouvir() #variavel escolha recebe valor dito pelo usuario
        new = 0

            #caso escolha seja verdadeira, executa comando para abrir navegador com url pré-determinada
        if escolha == '1':
            webbrowser.open('https://ftp.unicamp.br/pub/apoio/treinamentos/logica/logica.pdf', new=new)
            webbrowser.open('https://www.seduc.ce.gov.br/wp-content/uploads/sites/37/2012/06/informatica_logica_de_programacao.pdf', new=new)
            webbrowser.open("https://dicasdeprogramacao.com.br/download/ebook-logica-de-programacao-para-iniciantes.pdf", new=new)
            interface.destroy() #após navegador ser aberto, fechará a interface e pausa a repetição
            break

        elif escolha == '2':
            webbrowser.open('http://antigo.scl.ifsp.edu.br/portal/arquivos/2016.05.04_Apostila_Python_-_PET_ADS_S%C3%A3o_Carlos.pdf', new=new)
            webbrowser.open('https://irias.com.br/blog/python-mysql-criando-um-crud-completo/', new=new)
            interface.destroy()
            break

        elif escolha == '3':
            webbrowser.open('https://www.devmedia.com.br/instalando-e-configurando-a-nova-versao-do-mysql/25813', new=new)
            webbrowser.open('http://www.telecentros.sp.gov.br/saber/apostilas/antigas/apostila_sql.pdf', new=new)
            interface.destroy()
            break

        elif escolha == '4':
            webbrowser.open('https://www.caelum.com.br/apostila/apostila-java-orientacao-objetos.pdf', new=new)
            webbrowser.open('http://docente.ifsc.edu.br/vilson.junior/ed/IP_07_Java_Introducao.pdf', new=new)
            webbrowser.open('http://campeche.inf.furb.br/tccs/2007-I/2007-1leandrosalvattipisckevf.pdf', new=new)
            interface.destroy()
            break

        elif escolha == '5':
            webbrowser.open('http://www.etelg.com.br/paginaete/downloads/informatica/php.pdf', new=new)
            webbrowser.open('https://alexandrebbarbosa.wordpress.com/2016/09/04/php-pdo-crud-completo/comment-page-1/', new=new)
            interface.destroy()
            break

        elif escolha == '6':
            webbrowser.open('https://www1.univap.br/wagner/AulasCs(1Bim).pdf', new=new)
            webbrowser.open('https://www.caelum.com.br/apostila/apostila-csharp-orientacao-objetos.pdf', new=new)
            webbrowser.open('https://macoratti.net/11/04/C_MySQL_CRUD.pdf', new=new)
            interface.destroy()
            break

        else:
            falar("Diga um valor compatível com a lista!") # caso escolha do usuraio seja incompativel com itens da lista

#-------------------------------------------------------------------------------------------------

#DESENVOLVIMENTO DA INTERFACE
interface = Tk()
interface.geometry('800x650+250+5')
interface.title("Artigos úteis Online")
img_fundo = PhotoImage(file="imagens\\fundo_consult.png")
lab_fundo = Label(interface, image=img_fundo)
lab_fundo.pack()
texto = ttk.Label(interface, text="DIGA O NÚMERO DO ITEM QUE DESEJE PESQUISAR EM VOZ ALTA: ", font=("Arial 17"),
                  foreground='white', background='#0F2027')
texto.place(relx=0.5, rely=0.4, anchor='center')
texto = ttk.Label(interface, text="[ 1 ] LÓGICA DE PROGRAMAÇÃO\n\n[ 2 ] LINGUAGEM PYTHON\n\n[ 3 ] MySQL\n\n[ 4 ] LINGUAGEM JAVA\n\n[ 5 ] LINGUAGEM PHP\n\n[ 6 ] LINGUAGEM C#", font=("Arial 17"),
                  foreground='white', background='#0F2027')
texto.place(relx=0.3, rely=0.7, anchor='center')
threading.Thread(target=consult_art).start() # executar função de consulta simultaneamente com interface


interface.mainloop() #executa a abertura da interface
