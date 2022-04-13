def desempenho():
    import matplotlib.pyplot as plt
    from utils import informacoes_agenda

    data = informacoes_agenda()
    soma_horas = 0
    tecnologias = []
    horas = []

    for dia in data:
        data[dia]
        for tarefa in data[dia]:
            #soma hora apenas se tarefa foi feita
            if tarefa.get("feito") == "S":
                tecnologia = tarefa.get("tecnologia")
                hora = tarefa.get("horas")
                
                soma_horas += hora

                #verificando se a tecnologia já existe na lista
                if tecnologia in tecnologias:
                    #se existir, soma hora na posição já existente
                    posicao_existente = tecnologias.index(tecnologia)
                    horas[posicao_existente] += hora
                else:
                    #se não, adiciona nova tecnologia
                    tecnologias.append(tecnologia)
                    horas.append(hora)

    fig1, ax1 = plt.subplots()
    #print (fig1, ax1)

    ax1.pie(horas, labels=tecnologias, autopct='%1.1f%%', shadow=True, startangle=90)

    ax1.axis('equal')
    ax1.set_title("Horas empregadas de estudo")

    plt.show()
