# Estrutura Condicional
'''
8) Desenhe um fluxograma e implemente um
programa em Python que recebe três números
inteiros e informe se são números consecutivos em
ordem crescente.
'''
n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))
n3 = int(input("Número 3: "))

if (n2==n1+1 and n3==n2+1):
    print("São consecutivos")
else: print("Não são consecutivos")
