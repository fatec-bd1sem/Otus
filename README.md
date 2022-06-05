<h1 align="center">OTUS</h1>

<p align="center">
<img src="https://user-images.githubusercontent.com/36649454/167738690-ab4cf4cd-1bb7-4e08-b1cf-78c8dbb7a848.png" width=450px>

<br>
<p align="left">
O API a ser desenvolvido é uma assistente virtual acionada por comando de voz, tendo como público alvo alunos de programação que buscam inovar seus métodos de estudo e organizar seus horários.



## Requisitos:
 - Responder a comandos de voz ou sons específicos<br>
 - Possuir no mínimo oito ações de naturezas distintas<br>
 - Responder aos comandos em som, texto ou ação<br>
<br>



## Backlog do Produto

 - Comando de voz (Imprescindível)
 - Interface (Desejável) 
 - Agenda (Imprescindível)
 - Desempenho de estudos (Desejável)
 - Guia de estudo (Imprescindível)
 - Busca por artigos (Imprescindível)
 - Auxiliar de linguagem (Desejável)
 - Dicas e boas práticas de programação (Imprescindível)
 - Calculadora lógica (Imprescindível)
 - Music Player (Desejável)
 <hr>

## Cronograma
<details>
 <summary>1º sprint - 25/03 á 14/04</summary><br>
 - Agenda<br>
 - Desempenho de estudo<br>
 - Mockup de interface<br>
 <img src="https://user-images.githubusercontent.com/36649454/168403057-93a92485-1d42-47ca-b38b-170c97ce6f61.png" height=250px>
 <img src="https://user-images.githubusercontent.com/36649454/168403301-18119c76-ad47-4922-b764-9768e9f49f7d.png" height=250px>

<hr>

 <b>[Tarefas no Jira](https://github.com/fatec-bd1sem/Otus/files/8696015/sprint1.pdf)</b>
 <br>

 <b>Gráfico de Burndown</b>
 <br>
 ![image](https://user-images.githubusercontent.com/59184811/168484736-37a60122-cb39-4e7b-b6a9-21bc38cad026.png)

</details>


<details>
 <summary>2º sprint - 25/04 á 15/05</summary><br>
 - Guia de estudos<br>
 - Busca por artigos<br>
 - Auxiliar de linguagem<br>

<hr> 
 
 <b>[Tarefas no Jira](https://github.com/fatec-bd1sem/Otus/files/8696044/Tarefas_Jira_Sprint_2.pdf)<b/>
 <br>
 
 <b>Gráfico de Burndown</b>
 <br>
 ![image](https://user-images.githubusercontent.com/59184811/168485529-45118439-b08c-407c-9c9c-c268228f491d.png)

 </details>
 
 <details>
 <summary>3º sprint - 16/05 á 27/05</summary><br>
  - Dicas e boas práticas de programação<br>
  - Calculadora lógica<br>
  - Music player<br>
  
 </details>
- Feira de soluções - 15/06 
<hr>

### Tecnologias Utilizadas
 - Python<br>
 - Jira<br>
 - GitHub<br>
 - Figma<br>

### Bibliotecas Utilizadas
 - SpeechRecognition 
 - pyttsx3
 - tkinter
 - Pillow
 - ttkthemes
 - tkcalendar
 - pygame
 - matplotlib
 
<br>

 ### Equipe
 - [Beatrice Lopes](https://github.com/beatricelopes)<br>
 - [Breno do Nascimento](https://github.com/Breno30)<br>
 - [Carlos Torres](https://github.com/CarlosTorres2305)<br>
 - [Davi Gusmão](https://github.com/Davign10)<br>
 - [Gabriel Vieira](https://github.com/DevBielgrazi)<br>
 - [Guilherme Santana](https://github.com/1SGuilherme)<br>
 - [Wallace Honorato](https://github.com/WallaceHS20)<br>
<br>

### Tutorial para rodar o Projeto
<details>
<summary>passo a passo</summary>

1. Clone o projeto
```
git clone https://github.com/fatec-bd1sem/Otus.git
```

2. Baixe o PyAudio para sua versão do python [nesse link](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)

>De acordo com suas configurações<br>
![image](https://user-images.githubusercontent.com/59184811/160920480-39c560db-9320-4381-a883-8ada2a3448b2.png)


3. Na pasta onde foi feito o download, instale as bibliotecas com os comandos abaixo
```
pip install PyAudio-0.2.11-cp310-cp310-win_amd64.whl
```

```
pip install SpeechRecognition keyboard pyttsx3 tk ttkthemes tkcalendar pygame matplotlib Pillow truth-table-generator
```

4. Execute o arquivo principal.py na pasta `Otus`

</details>
