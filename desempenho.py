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
            tarefa.get("horas")
            soma_horas += tarefa.get("horas")
            tarefa.get("tecnologia")
            tecnologias.append(tarefa.get("tecnologia"))
            horas.append(tarefa.get("horas"))

    fig1, ax1 = plt.subplots()
    #print (fig1, ax1)

    ax1.pie(horas, labels=tecnologias, autopct='%1.1f%%', shadow=True, startangle=90)

    ax1.axis('equal')
    ax1.set_title("horas empregadas de estudo")

    plt.show()

