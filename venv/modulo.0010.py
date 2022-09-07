# DESFIO LISTA MULTIPLAS

from itertools import zip_longest

produtos = ['prduto1', 'prduto2', 'prduto3', 'prduto4', 'prduto5']
precos = ['R$500,00', 'R$1500,00', '2700,00', 'R$5000,00']

for produto, preco in zip_longest(produtos, precos):
    print(f'produto : {produto} encontrado no valor de {preco}')
