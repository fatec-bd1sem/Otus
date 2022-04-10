def agenda():
    from ttkthemes import ThemedTk
    from utils import agendar_tarefa
    import threading
    
    #Armazenando dia
    def coletar_dia():
        from utils import ouvir
        dia = int(ouvir())
        if dia != None:
            janela2 = ThemedTk(theme="arc")
            janela2.geometry("300x200")
            agendar_tarefa(janela2,"Qual tarefa deseja estudar?")
            threading.Thread(target=coletar_tarefa).start()
            janela2.mainloop()
        return dia
    
    #Armazenando tarefa
    def coletar_tarefa():
        from utils import ouvir
        tarefa = str(ouvir())
        if tarefa != None:
            janela3 = ThemedTk(theme="arc")
            janela3.geometry("300x200")
            agendar_tarefa(janela3,"Quanto tempo deseja estudar?")
            threading.Thread(target=coletar_tempo).start()
            janela3.mainloop()
        return tarefa
    
    #Armazenando tempo
    def coletar_tempo():
        from utils import ouvir
        tempo = float(ouvir())
        return tempo

    
    #Tema interface
    janela = ThemedTk(theme="arc")

    #Tamanho interface
    janela.geometry('300x200')    

    #Pergunta dia 
    agendar_tarefa(janela,"Qual dia deseja estudar?")
    threading.Thread(target=coletar_dia).start()
    janela.mainloop()