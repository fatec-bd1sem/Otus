#FUNÇÕES INTERFACE ----------------------------------------------------
from tkinter import LEFT


def comando_botao_ouvir():
    from utils import ouvir, procurar_comando, tocar
    tocar('start.mp3')
    frase = ouvir()
    comando_encontrado = procurar_comando(frase)
    #os.system('cls')

def perguntar(window, pergunta, respostas):
    from tkinter import ttk
    #Limpa tela
    for componente in window.winfo_children():
        componente.destroy()
        
    #Pergunta
    label_pergunta = ttk.Label(window, text=pergunta,
                                font = ('Helvetica', 15, 'bold'))
    label_pergunta.place(relx=0.5, rely=0.1, anchor='center')


    #Resposta
    label_respostas = []
    for idx, resposta in enumerate(respostas):
        #calcula altura das respostas
        altura_y = (idx+2)/10
        #adiciona resposta a array
        label_respostas.append( ttk.Label(window, text=f'{idx+1}) {resposta}',
                                            font = ('Helvetica', 13, 'bold')) )
        #pega última resposta (-1) adicionada
        label_respostas[-1].place(relx=0.3, rely=altura_y, anchor='w')


#FUNÇÕES DE VOZ ------------------------------------------------------

def tocar(audio):
    from pygame import mixer 
    import pathlib
    caminho_pasta = str(pathlib.Path().resolve())
    caminho_audio = f"{caminho_pasta}\Audios\{audio}"
    mixer.init()
    mixer.music.load(caminho_audio)
    mixer.music.play()

def falar(frase):
    import pyttsx3
    #iniciando fala
    engine = pyttsx3.init()
    engine.say(frase)  
    engine.runAndWait()

def procurar_comando(frase):
    #importa funções dos demais arquivos
    from agenda import agenda
    from desempenho import desempenho
    from guia_de_estudo import guia_de_estudo
    from auxiliar import auxiliar
    from consult_artigo import artigo
    from calculadora import calculadora
    from dicas import dicas as dica
    from musicplayer import musicplayer
    

    comandos = ['agenda','desempenho','guia','auxiliar','artigos', 'calculadora', 'dica', 'tocar']
    funcoes = [agenda, desempenho, guia_de_estudo, auxiliar, artigo, calculadora, dica, musicplayer]

    encontrado = False
    
    #separa frase em palavras para análise
    palavras = frase.split(' ')

    #confere cada palavra
    for palavra in palavras:
        #verifica se a palavra é um comando
        if palavra in comandos:
            #toca som de finalização
            tocar('success.mp3')
            #encontra número do comando na lista
            numero_comando = comandos.index(palavra)
            #executa comando 
            funcoes[numero_comando]()
            encontrado = True
            break

    #retorna se comando foi encontrado na frase
    return encontrado

def ouvir():
    import speech_recognition as sr
    comando_encontrado = False
    rec = sr.Recognizer()
    
    while True:
        #caso tenha encontrado comando, para de ouvir
        if (comando_encontrado):
            os.system('cls')
            break
        
        #caso não tenha encontrado comando, continua ouvindo
        else:
            print('OUVINDO...')
            with sr.Microphone() as mic:
                rec.adjust_for_ambient_noise(mic)
                audio=rec.listen(mic)
                try:
                    #envia áudio para o google
                    frase=rec.recognize_google(audio,language="pt-BR")
                    print(f'Você disse: {frase}')
                    return frase
                
                except:
                    #speak('please, try again')
                    print("erro")
                    pass

#FUNÇÕES DE TAREFAS -------------------------------------------------
def marcar_tarefa_feita(dia, index_tarefa):
    import json
    #importa dados da agenda
    dados = informacoes_agenda()
    #marca tarefa como feita
    dados[dia][index_tarefa]['feito'] = 'S'
    #transforma em string
    dados = json.dumps(dados)
    #grava novo json no arquivo
    with open('dados_agenda.json', 'w') as dados_agenda:
        dados_agenda.write(dados)
        print(dados)
        
def informacoes_agenda():
    #abre arquivo .json com informações
    with open('dados_agenda.json','r') as file:
        import json
        dados_agenda = file.read()
        dados_agenda = json.loads(dados_agenda)
    #retorna informações
    return dados_agenda

#Passar informações para json
def enviar_tarefa(data, tarefa, tempo):
    import json
    import shutil
    import tempfile


    #Pegando arquivo json antigo
    with open("dados_agenda.json", "r", encoding='utf-8') as file, \
        tempfile.NamedTemporaryFile('w', delete=False) as out:
        dados_agenda = json.load(file)
        #Enviando para arquivo json
        dados_agenda[data] =[
        {"tarefa" : tarefa,
         "tempo" : tempo,
         "feito" : "N"}
        ]
        json.dump(dados_agenda, out, ensure_ascii=False, indent=3, separators=(',',':'))
    shutil.move(out.name, 'dados_agenda.json')

#Janela de pergunta    
def agendar_tarefa(pergunta):
    from tkinter import Label, Tk
    
    #Tema interface
    janela = Tk()
    #Tamanho interface
    janela.geometry('300x200')
    janela.configure(background="#0F2027")
    janela.title("Assistente Virtual OTUS")
    
    #Limpa tela
    for componente in janela.winfo_children():
        componente.destroy()

    #Formatacao e fonte pergunta
    label_pergunta = Label(janela, text=pergunta,font = ('Helvetica', 15, 'bold'),background="#0F2027",foreground="#FFFFFF")
    label_pergunta.place(relx=0.5, rely=0.5, anchor='center')

    janela.mainloop()

#FUNÇÕES DE NOTIFICAÇÃO -------------------------------------------------

    
def notificar(titulo, texto, dia, index_tarefa):
    try: 
        import zroya

        zroya.init(" ", "Otus", "Otus", "Otus", "1.0")

        ask_template = zroya.Template(zroya.TemplateType.ImageAndText4)
        ask_template.setFirstLine(titulo)
        ask_template.setSecondLine(texto)
        ask_template.addAction("Já estudei")

        def onAction(nid, action_id):
            marcar_tarefa_feita(dia, index_tarefa)
         
        zroya.show(ask_template, on_action=onAction)

    except:
        print('Erro ao importar zroya')
        print('https://visualstudio.microsoft.com/visual-cpp-build-tools/')


def notificar_lembretes_hoje():
    from datetime import date
    #pega dia atual
    hoje = date.today()
    #converte para formato dd/mm/aaaa
    hoje = hoje.strftime("%d/%m/%Y")
    #pega informações da data de hoje
    data_infos = informacoes_agenda()
    #verifica se data existe no json
    if (hoje in data_infos):
        data_infos = data_infos[hoje]
        #para cada atividade, adiciona ao lembrete final
        for idx, atividade in enumerate(data_infos):
            if atividade['feito'] == 'N':
                tecnologia = atividade['tecnologia']
                horas = atividade['horas']
                lembrete = f"> estudar {tecnologia} por {horas} horas\n"
                #notifica lembrete final
                notificar("Lembrete",lembrete, hoje, idx)

#FUNÇÕES DE AUXILIAR DE LINGUAGEM ------------------------------------------
def codigos_linguagens():
    #abre arquivo .json com informações
    with open('codigos_exemplo.json','r') as arquivo:
        import json
        codigos_exemplo = arquivo.read()
        codigos_exemplo = json.loads(codigos_exemplo)
    #retorna informações
    return codigos_exemplo

def tela(texto):
        from tkinter import Label, Tk

        #Tema interface
        janela = Tk()
        #Tamanho interface
        janela.geometry('900x600')
        janela.configure(background="#0F2027")
        janela.title("Assistente Virtual OTUS")
        
        #Limpa tela
        for componente in janela.winfo_children():
            componente.destroy()

        #Formatacao e fonte pergunta
        label_pergunta = Label(janela, justify=LEFT, text=texto,font = ('Helvetica', 15, 'bold'),background="#0F2027",foreground="#FFFFFF", anchor='e')
        label_pergunta.place(relx=0.5, rely=0.2, anchor='center')

        janela.mainloop()

def apresentar_codigo_exemplo(funcao,linguagem):
    import unicodedata
    from auxiliar import auxiliar
    #pega códigos de exemplo
    code_exemplos = codigos_linguagens()
    try:
        funcao = funcao.lower()
        funcao = unicodedata.normalize("NFD",funcao)
        funcao = funcao.encode("ascii","ignore")
        funcao = funcao.decode("utf-8")
        linguagem = linguagem.lower()
        code_exemplos = code_exemplos[funcao][linguagem]
        tela(f"Exemplo:\n{code_exemplos}")
    except:
        auxiliar()
