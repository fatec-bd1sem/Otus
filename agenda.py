def agenda():
    from utils import enviar_tarefa
    from tkinter import Tk
    from utils import agendar_tarefa
    from datetime import datetime
    import threading
    
    #Armazenando dia
    def coletar_dia():
        from utils import ouvir
        dia = int(ouvir())
        if dia != None:
            janela = Tk()
            janela.geometry("300x200")
            janela.configure(background="#0F2027")
            janela.title("Assistente Virtual OTUS")
            agendar_tarefa(janela,"Qual tarefa deseja estudar?")
            threading.Thread(target=coletar_tarefa).start()
            janela.mainloop()
        return dia
    
    #Armazenando tarefa
    def coletar_tarefa():
        from utils import ouvir
        tarefa = str(ouvir())
        if tarefa != None:
            janela = Tk()
            janela.geometry("300x200")
            janela.configure(background="#0F2027")
            janela.title("Assistente Virtual OTUS")
            agendar_tarefa(janela,"Quanto tempo deseja estudar?")
            threading.Thread(target=coletar_tempo).start()
            janela.mainloop()
        return tarefa
    
    #Armazenando tempo
    def coletar_tempo():
        from utils import ouvir
        tempo = float(ouvir())
        return tempo

    #Tema interface
    janela = Tk()

    #Tamanho interface
    janela.geometry('300x200')
    janela.configure(background="#0F2027")
    janela.title("Assistente Virtual OTUS") 

    #Pergunta dia 
    agendar_tarefa(janela,"Qual dia deseja estudar?")
    threading.Thread(target=coletar_dia).start()
    janela.mainloop()

    #Pegando data atual
    mes = str(datetime.today().strftime('%m'))
    ano = str(datetime.today().strftime('%Y'))
    #Pegando do arquivo agenda
    dia = coletar_dia()
    data = str(f"{dia}/{mes}/{ano}")
    tarefa = coletar_tarefa()
    tempo = coletar_tempo()

    enviar_tarefa(data, tarefa, tempo)