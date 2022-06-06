def falar_opcoes():
    from utils import falar
    falar('Qual função deseja?')

def ouvir_opcoes():
    from utils import ouvir
    from funcoes_calculadora.conversor import conversor
    from funcoes_calculadora.tabela_verdade import tabela_verdade
    from funcoes_calculadora.plano_cartesiano import plano_cartesiano
    funcoes_calc = [conversor, tabela_verdade, plano_cartesiano]

    while True:
        funcao_chamada = ouvir()
        # ouve até encontrar 1,2 ou 3
        if funcao_chamada == '1' or funcao_chamada == '2' or funcao_chamada == '3':
            break
    
    # chama função de acordo com seu index
    funcoes_calc[int(funcao_chamada)-1]()

def mostrar_opcoes():
    from utils import tela
    tela("Qual função deseja?\n\n[1] - Converção numérica    \n\n[2] - Tabela verdade            \n\n[3] - Plano Cartesiano         ")


def calculadora():
    from threading import Thread

    Thread(target=mostrar_opcoes).start()
    Thread(target=falar_opcoes).start()
    Thread(target=ouvir_opcoes).start()