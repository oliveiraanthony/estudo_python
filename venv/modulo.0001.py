# registro Funcionario

# obtenha nome do funcionario
# obtenha idade do funcionario
# registrar forma automatica  a data de cadastro do funcionario,usuando a data
# de registro
# para cada funcionario que se registrar na empresa ,ele recebera um dos seguin
# tes cartoes,
# que sera sorteado de forma aleatoria
from datetime import datetime
import random

nome_funcioanrio = input('qual seu nome completo')
idade_funcionario = int(input("qual sua idade ?"))
data_cadastro = datetime.now()
cartoes = ['$500,00', '$100,00', '$150,00', '$200,00']
cartao = random.choice(cartoes)
# guarde informaçoes sobre a data de aniversario(dd/mm/aaaa)
data_niver = datetime.strptime(
    input('qual sua data de aniversairo? d/m/aaaa'), '%d/%m/%Y')


# gerar apresentação do funcionario

# mensangem de boas vinda
print('==============seja bem vindo================ ')
# exiba as seguintes informaçoes
print(f'óla meu {nome_funcioanrio}, seu registro {data_cadastro.day}',
      '/{data_cadastro.month}/{data_cadastro.year}',
      'parabens,hove um sorteio  e voce ganhou um cartão de vale',
      'compras no valor de', '{cartao}')
