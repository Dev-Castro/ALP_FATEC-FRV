# Estrutura Condicional
'''
15) Uma empresa tem uma colônia de férias para seus
funcionários, onde cada funcionário pode reservar somente um
apartamento por período de permanência. Em cada apartamento
podem ficar até seis pessoas. Existem dois tipos de apartamentos
(tipo 1 e 2). O valor da diária é dado pela tabela abaixo:

Quantidade de Pessoas        Diária      Diária   
    no Apartamento          tipo1(R$)   tipo2(R$)
        1                     20,00       25,00
        2                     28,00       34,00
        3                     35,00       42,00
        4                     42,00       50,00
        5                     48,00       57,00
        6                     53,00       63,00

Desenhe um fluxograma e implemente um programa em Python
que calcule e mostre o valor a ser pago por uma família qualquer.
Obs.: neste problema você deve identificar a entrada,
processamento e saída.
'''
# Entrada

quantidade = int(input("Digite a quantidade de pessoas: "))
tipo = int(input("Digite o tipo de diária: "))

d1 = [20,28,35,42,48,53]
d2 = [25,34,42,50,57,63]

# Processamento

if (tipo==1):
    valor = d1[quantidade-1]
elif(tipo==2):
    valor = d2[quantidade-1]

# Saída

print("O valor a ser pago por esta família é: R$ %i,00" % valor)