from utils import apresentar_codigo_exemplo


def auxiliar():
    from utils import ouvir,tocar,apresentar_codigo_exemplo,tela
    import threading

    def coletar_funcao():
        try:
            threading.Thread(target=tocar, args=["start.mp3"]).start()
            funcao = str(ouvir())
            if funcao != None:
                threading.Thread(target=coletar_linguagem, args=[funcao]).start()
                tela(f"{funcao} em qual linguagem?\n-PHP\n-JavaScript\n-Python\n-Java\n-C++")
        except:
            return coletar_funcao()

    def coletar_linguagem(funcao):
        try:
            threading.Thread(target=tocar, args=["start.mp3"]).start()
            linguagem = str(ouvir())
            if linguagem != None:
                apresentar_codigo_exemplo(funcao,linguagem)
        except:
            return coletar_funcao()

    threading.Thread(target=coletar_funcao).start()
    tela("Qual função está buscando?\n-Condições\n-Laços de repetição\n-Variáveis\n-Biblioteca\n-Funções\n-Classes")