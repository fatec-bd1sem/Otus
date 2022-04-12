import json
from utils import informacoes_agenda
data = informacoes_agenda()

for dia in data:
    data[dia]
    for tarefa in data[dia]:
        tarefa.get("horas")
        print(tarefa.get("horas"))
