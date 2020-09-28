# Estrutura Condicional
'''
6) Desenhe um fluxograma e implemente um
programa em Python que recebe um número real e
informe se é igual a zero, número positivo ou
negativo.
'''
n = float(input("Digite o valor: "))

if n>0:
    print("É positivo")
elif n<0:
    print("É negativo")
else: print("É igual a zero")