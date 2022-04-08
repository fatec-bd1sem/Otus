def quiz():
    from ttkthemes import ThemedTk
    from utils import perguntar
    
    #define tema
    window = ThemedTk(theme="arc")

    #define tamanho da tela
    window.geometry('400x450')

    ''' 
    #É passada a pergunta com as possíveis respostas 
    perguntar(window,
            "Qual área deseja estudar?",
            ['Web',
            'Desktop',
            'Mobile'])
    '''
 
    window.mainloop()
