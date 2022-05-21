def converter_decimal(num, base):
    res = ''
    while (num>0):
        # adiciona resto no texto
        res += str(num%base)
        # muda valor atual do número
        num = num//base
    # retorna texto invertido 
    return res[::-1]

def perguntar_conversao():
    from utils import falar
    falar('Diga a conversão')

def mostrar_exemplo_conversao():
    from utils import tela
    tela('Diga a conversão (ex: 10 em base 2)')

def ouvir_conversao():
    from utils import ouvir, tela
    frase_conversor = ouvir()

    palavras = frase_conversor.split()

    numero_encontrado = False
    numero = 0
    base = 0

    for palavra in palavras:
        # tenta converter palavra em numero
        try: 
            # se der certo, número ou base encontrado
            if (numero_encontrado):
                base = int(palavra)
            else:
                numero = int(palavra)
            numero_encontrado = True
        except:
            pass

    resultado_convertido = converter_decimal(numero,base)
    tela(f'Número {numero} convertido para base {base}:\n{resultado_convertido}')

def conversor():
    # zerando caminho para importar funções de diretórios acima
    import sys
    sys.path.append('')

    from threading import Thread
    from utils import ouvir, tela



    Thread(target=perguntar_conversao).start()
    Thread(target=mostrar_exemplo_conversao).start()
    Thread(target=ouvir_conversao).start()
