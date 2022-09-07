# DESAFIO COM DECORENTE
from datetime import datetime


def meu_decorete(funcao):
    def h_atual():
        print('horario atual', datetime.now())

        funcao()

        print('horario apois funcao', datetime.now())
    return h_atual


@meu_decorete
def horario():
    print('horario depois da funcao')


horario()
