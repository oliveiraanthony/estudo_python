# DESAFIO FILTRE

vagas = [['vagas', 1200], ['vagas', 2550], ['vagas', 5000]]


def vagas_aberta(vagas):
    if vagas[1] > 2500:
        return True
    else:
        return False


print(list(filter(vagas_aberta, vagas)))
