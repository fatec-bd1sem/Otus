def converter_decimal(num, base):
    res = ''
    while (num>0):
        # adiciona resto no texto
        res += str(num%base)
        # muda valor atual do número
        num = num//base
    # retorna texto invertido 
    return res[::-1]

def conversor():
    print('função conversor chamada')
