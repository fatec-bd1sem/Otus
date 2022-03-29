from keyboard import record
from time import sleep
import speech_recognition as sr
import pyttsx3 
import os
import subprocess

#importa funções dos demais arquivos
from agenda import agenda
from desempenho import desempenho
from quiz import quiz

comandos = ['agenda','desempenho','quiz']
funcoes = [agenda, desempenho, quiz]

#iniciando fala
engine = pyttsx3.init()

def notificar(titulo, texto):
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

def procurar_comando(frase):
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

def falar(frase):
    engine.say(frase)  
    engine.runAndWait()
                    
def ouvir():
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
                    comando_encontrado = procurar_comando(frase)

                except:
                    #speak('please, try again')
                    print("erro")
                    pass
                    
while True:
    print('PRESSIONE ENTER PARA FALAR')
    record(until="enter")
    #os.system('cls')
    ouvir()
            

