# Expressões Aritméticas
'''
10) Implemente um algoritmo (fluxograma) e o programa em
Python que leia três números reais, calcula a média ponderada e
mostre o resultado.
Média Aritmética = n1 . 2 + n2 .3 + n3 . 5 / 10
'''
n1 = float(input("n1: "))
n2 = float(input("n2: "))
n3 = float(input("n3: "))

#pesos
a = 2
b = 3
c = 5
pesos = a+b+c

media = (n1*a + n2*b + n3*c) / pesos

print(media)