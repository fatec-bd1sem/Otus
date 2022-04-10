#Ouvindo dia
def coletar_dia():
    from utils import ouvir
    dia = str(ouvir())
    return dia

#Ouvindo tarefa
def coletar_tarefa():
    from utils import ouvir
    tarefa = str(ouvir())
    return tarefa

#Ouvindo Tempo
def coletar_tempo():
    from utils import ouvir
    tempo = str(ouvir())
    return tempo

def agenda():
    from threading import Thread
    from ttkthemes import ThemedTk
    from utils import agendar_tarefa

    #Tema interface
    janela = ThemedTk(theme="arc")

    #Tamanho interface
    janela.geometry('250x100')

    #Pergunta dia 
    agendar_tarefa(janela,"Qual dia deseja estudar?")
    Thread(target=lambda:coletar_dia()).start()
    janela.mainloop()
    
    #Pergunta tarefa após receber dia
    if coletar_dia() != "":
        janela.destroy()
        agendar_tarefa(janela,"Qual tarefa deseja estudar?")
        Thread(target=lambda:coletar_tarefa()).start()
        janela.mainloop()
        #Pergunta tempo após receber tarefa
        if coletar_tarefa() != "":
            janela.destroy()
        agendar_tarefa(janela,"Quanto tempo deseja estudar?")
        Thread(target=lambda:coletar_tempo()).start()
        janela.mainloop()