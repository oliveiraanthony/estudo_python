# DESAFIO SALAÃO DE BELEZA

# CALCULAR PRESO DO CORTE DE CABELO GRANDES QUE ÍRA SEGUIR AS SEGUINTE REGRAS
# º SE SEU CABELO ESTIVER COM OU BAIXO DE 20CM VOCÊ PAGA O VALOR DE R$ 50,00
# ºSE SEU CABELO ESTIVER ENTRE 21CM A 30CM VOCÊ PAGARAR O VALOR DE R$70,00,
# ºSE SEU CABELO ESTIVER ENTRE 31CM A 50CM VOCÊ PAGARAR O VALOR DE R$100,00,
# ºACIMA DE 50CM CONSULTAR A RECEPÇÃO

tamanho_atual_cabelo = 25

if tamanho_atual_cabelo <= 20:
    print("você pagara o valor de R$ 50,00")
elif tamanho_atual_cabelo >= 21 and tamanho_atual_cabelo <= 30:
    print("você pagara o valor de R$ 70,00")
elif tamanho_atual_cabelo >= 31 and tamanho_atual_cabelo <= 50:
    print("você pagara o valor de R$ 100,00")
else:
    print("procurar a recepção")
