from utils import falar
import threading
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk, Tk
import tkinter as tk
import random

def dicas():

    #lista com os locais das imagens que contém as dicas
    locais = ['imagens/imagens_dicas/dica1.png', 'imagens/imagens_dicas/dica2.png', 'imagens/imagens_dicas/dica3.png',
             'imagens/imagens_dicas/dica4.png', 'imagens/imagens_dicas/dica5.png', 'imagens/imagens_dicas/dica6.png',
             'imagens/imagens_dicas/dica7.png', 'imagens/imagens_dicas/dica8.png', 'imagens/imagens_dicas/dica9.png',
             'imagens/imagens_dicas/dica10.png']

    #escolha aleatória de dicas
    global endereco
    endereco = random.choice(locais)

    #DESENVOLVIMENTO DA INTERFACE
    tela_dica = Tk()
    tela_dica.geometry('800x650+250+5')
    tela_dica.title("DICAS")
    tela_dica.configure(background='white')
    image = Image.open(endereco)
    photo = ImageTk.PhotoImage(image, master=tela_dica)
    fundo = tk.Label(tela_dica, image=photo)
    fundo.image = image
    fundo.place(x=4,y=5)
    threading.Thread(target=verificacao).start()
    tela_dica.mainloop()

def verificacao():
        #verificação de escolha para inteligência falar
        if endereco == 'imagens/imagens_dicas/dica1.png':
            falar("Identar o código\nConsidere a identação de código um dos itens mais básicos e ao mesmo tempo importante para um programador, sendo ele iniciante ou avançado. O fato de identificarmos o escopo de condições IF, WHILE e etc., facilita muito entendimento do código, além de deixar mais bonito.")

        elif endereco == 'imagens/imagens_dicas/dica2.png':
            falar("Nomear variáveis de maneira intuitiva\nNomear variáveis pode parecer uma tarefa simples, basta seguir as restrições de cada linguagem e por causa disso os nomes acabam não possuindo sentido ao escopo do código.\nÉ possível encontrar esse tipo de problema em loops usando laços de repetição “FOR” aninhados, onde é comum encontrarmos contadores com nome de x, y, z e etc., variáveis, até mesmo nome de estruturas como Arrays é possível encontrar nomes “bizarros”.")

        elif endereco == 'imagens/imagens_dicas/dica3.png':
            falar("Evite chamar funções para testes em loops\nvamos usar um “FOR” para percorrer os elementos das Arrays, mas o laço “FOR” precisa saber qual é o limite do loop, é nesse momento que geralmente chamamos funções nativas para efetuar a contagem de elementos.\nNo exemplo abaixo chamo a função “count()” para saber a quantidade de elementos na minha Array, temos que levar em consideração que caso nossa Array tenha 500 elementos, iremos chamar a função “count()” 500 vezes.")

        elif endereco == 'imagens/imagens_dicas/dica4.png':
            falar("Evitar condição de negação no IF\nPraticamente não existe programação sem o controle de fluxo usando condições “IF”, a ideia é sempre avaliar se uma condição é verdadeira dentro da condição para executar determinado código.\nPor esse motivo evite sempre que possível usar verificações de negação na condição, sempre que possível avalie primeiro a condição verdadeira e caso falso execute o código do  “ELSE”, isso também torna o código mais legível e menos confuso quando temos “IFs” aninhados.")

        elif endereco == 'imagens/imagens_dicas/dica5.png':
            falar("Nomear funções da maneira intuitiva\nNomear funções é outra tarefa que aparentemente é simples, mas se soubermos escolher nomes mais intuitivos e ligados ao objetivo da função, também podemos tornar nosso código mais legível.")

        elif endereco == 'imagens/imagens_dicas/dica6.png':
            falar("Comentar o código\num comentário detalhando o objetivo do método ou função, seus parâmetros de entrada e de saída podem ajudar em manutenções futuras do código, principalmente se a manutenção for de um profissional que não conhece o sistema")

        elif endereco == 'imagens/imagens_dicas/dica7.png':
            falar('Padronizar nome das constantes\nConstantes são valores que não podem ser alterados durante a execução de uma aplicação, por isso elas merecem um destaque em nossos sistemas.\nUma boa prática é definir um padrão para o nome das constantes sempre em caixa alta, isso ajuda a identifica-las no meio do código')

        elif endereco == 'imagens/imagens_dicas/dica8.png':
            falar("Utilizar blocos try..catch..\nTrabalhar com códigos dentro de blocos try..catch é considerado até uma boa prática de segurança, por exemplo se ocorrer um erro no script PHP para conexão com o banco de dados onde não está sendo usando try..catch, existem situações que será impresso na página o nome do banco de dados.\nAlém disso controlando as EXCEPTIONS da sua aplicação você pode exibir mensagens mais intuitivas para o usuário, evitando aquelas mensagens em ‘inglês” que são padrão da maioria das linguagens de programação.")

        elif endereco == 'imagens/imagens_dicas/dica9.png':
            falar("Não usar valor padrão em argumentos de funções\nQuando escrevemos uma função que necessita receber argumentos de entrada as vezes sentimos a necessidade de deixar um valor padrão nesse argumento, mas garanto que nem mesmo quem escreveu a função vai lembrar desse valor padrão quando precisar debugar em erro, imagine outro programador.")

        elif endereco == 'imagens/imagens_dicas/dica10.png':
            falar("Percorrer loops somente o necessário\nAs vezes precisamos percorrer um loop procurando por apenas uma combinação e mesmo após encontrar essa combinação ainda deixamos o loop executando por uma infinidade de vezes. utilizar o comando break é necessário para interromper a repetição.")
