# Estrutura Condicional
'''
5) Desenhe um fluxograma e implemente um
programa em Python que recebe dois números
reais e informa se são iguais. Caso sejam
diferentes, informe o maior e o menor. 
'''
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

if n1==n2:
    print("São iguais")
else:
    maior = (n1 + n2 + abs(n1 - n2))/2
    if maior==n1:
        print("N1 é maior e N2 é menor")
    else: print("N2 é maior e N1 é menor")