from tkinter.messagebox import NO


def agenda():
    from utils import enviar_tarefa, agendar_tarefa, tocar
    from datetime import datetime
    import threading
    
    #Armazenando dia
    def coletar_dia():
        from utils import ouvir
        try:
            threading.Thread(target=tocar, args=["start.mp3"]).start()
            dia = int(ouvir())
            if dia != None:
                ano = int(datetime.today().strftime('%Y'))
                diaa= int(datetime.today().strftime('%d'))
                mes = int(datetime.today().strftime('%m'))
                if dia <= diaa:
                    mes = mes+1
                    if mes == 13:
                        mes = 1
                        ano = ano+1 
                if dia < 10:
                    dia = str(f"0{dia}")
                if mes < 10:
                    mes = str(f"0{mes}")
                data = str(f"{dia}/{mes}/{ano}")
                threading.Thread(target=coletar_tarefa, args=[data]).start()
                agendar_tarefa("Qual tarefa deseja estudar?")
        except:
            return coletar_dia()
    
    #Armazenando tarefa
    def coletar_tarefa(data):
        from utils import ouvir
        threading.Thread(target=tocar, args=["start.mp3"]).start()
        tarefa = str(ouvir())
        if tarefa != None:
            threading.Thread(target=coletar_tempo, args=[data,tarefa]).start()
            agendar_tarefa("Quantas horas deseja estudar?")
    
    #Armazenando tempo
    def coletar_tempo(data, tarefa):
        from utils import ouvir
        try:
            threading.Thread(target=tocar, args=["start.mp3"]).start()
            tempo = float(ouvir())
            if tempo != None:
                enviar_tarefa(data, tarefa, tempo)
                agendar_tarefa("Tarefa Agendada!")
        except:
            return coletar_tempo(data, tarefa)
 
    threading.Thread(target=coletar_dia).start()
    agendar_tarefa("Qual dia deseja estudar?")