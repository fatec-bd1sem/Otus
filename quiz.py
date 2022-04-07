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






def quiz():

    from ttkthemes import ThemedTk

    #define tema
    window = ThemedTk(theme="arc")

    #define tamanho da tela
    window.geometry('400x450')

    """"
    #É passada a pergunta com as possíveis respostas 
    perguntar(window,
            "Qual área deseja estudar?",
            ['Web',
            'Desktop',
            'Mobile'])
    """
    
    window.mainloop()