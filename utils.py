#FUNÇÕES DE VOZ ------------------------------------------------------
def falar(frase):
    #iniciando fala
    engine = pyttsx3.init()
    engine.say(frase)  
    engine.runAndWait()

def procurar_comando(frase):
    #importa funções dos demais arquivos
    from agenda import agenda
    from desempenho import desempenho
    from quiz import quiz

    comandos = ['agenda','desempenho','quiz']
    funcoes = [agenda, desempenho, quiz]

    encontrado = False
    
    #separa frase em palavras para análise
    palavras = frase.split(' ')

    #confere cada palavra
    for palavra in palavras:
        #verifica se a palavra é um comando
        if palavra in comandos:
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
def informacoes_agenda():
    #abre arquivo .json com informações
    with open('dados_agenda.json','r') as file:
        import json
        dados_agenda = file.read()
        dados_agenda = json.loads(dados_agenda)
    #retorna informações
    return dados_agenda




#FUNÇÕES DE NOTIFICAÇÃO -------------------------------------------------
def notificar(titulo, texto):
    import subprocess
    comando = """
    [Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] > $null;
    $Template = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent([Windows.UI.Notifications.ToastTemplateType]::ToastText02);
    $RawXml = [xml] $Template.GetXml()
    ($RawXml.toast.visual.binding.text|where {$_.id -eq "1"}).AppendChild($RawXml.CreateTextNode('"""+titulo+"""')) > $null
    ($RawXml.toast.visual.binding.text|where {$_.id -eq "2"}).AppendChild($RawXml.CreateTextNode('"""+texto+"""')) > $null;
    $SerializedXml = New-Object Windows.Data.Xml.Dom.XmlDocument;
    $SerializedXml.LoadXml($RawXml.OuterXml);
    $Toast = [Windows.UI.Notifications.ToastNotification]::new($SerializedXml);
    $Toast.Tag = "PowerShell";
    $Toast.Group = "PowerShell";
    $Toast.ExpirationTime = [DateTimeOffset]::Now.AddMinutes(5);
    $Notifier = [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier("OTUS");
    $Notifier.Show($Toast);
    """
    process=subprocess.Popen(["powershell","& {" + comando + "}"],stdout=subprocess.PIPE);

def notificar_lembretes_hoje():
    from datetime import date
    #pega dia atual
    hoje = date.today()
    #converte para formato dd/mm/aaaa
    hoje = hoje.strftime("%d/%m/%Y")
    #inicia lembrete
    lembrete = 'Lembre-se de:\n'
    #pega informações da data de hoje
    data_infos = informacoes_agenda()
    data_infos = data_infos[hoje]
    #para cada atividade, adiciona ao lembrete final
    for atividade in data_infos:
        tecnologia = atividade['tecnologia']
        horas = atividade['horas']
        lembrete += f"> estudar {tecnologia} por {horas} horas\n"
    #notifica lembrete final
    notificar("Lembrete",lembrete)


