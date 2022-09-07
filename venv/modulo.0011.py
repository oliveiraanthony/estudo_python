# DESAFIO ENUMERANT

frutas = ['maça', 'laranja', 'uva', 'pessago']
for i, fruta in enumerate(frutas, 0):
    if i == 3:
        print(f'{i} {fruta} em PROMOÇÃO')
    else:
        print(f'{i} {fruta}')
