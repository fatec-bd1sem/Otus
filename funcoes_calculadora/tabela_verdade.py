def tabela_verdade():
    # zerando caminho para importar funções de diretórios acima
    import ttg
    import sys
    sys.path.append('')
    
    from utils import ouvir, falar
    falar('Qual tabela-verdade você deseja visualizar?')
    frase = ouvir()

    ##tabelas verdade
    def conjuncao(): 
        print(ttg.Truths(['p', 'q'], ['p and q']))

    def disjuncao():
        print(ttg.Truths(['p', 'q'], ['p or q']))
    
    def implicacao():
        print(ttg.Truths(['p', 'q'], ['p xor q']))
    
    def bicondicional():
        print(ttg.Truths(['p', 'q'], ['p = q']))
    
    def exclusive_disjunction():
        print(ttg.Truths(['p', 'q'], ['p != q']))

    

    palavras = frase.split()
    palavras_chave = ['e', 'ou', 'se', 'igual', 'desigual']
    funcoes = [conjuncao, disjuncao, implicacao, bicondicional, exclusive_disjunction]
    
    for palavra in palavras:
        if palavra in palavras_chave:
            comando = palavras_chave.index(palavra)
            funcoes[comando]()
            break



        




