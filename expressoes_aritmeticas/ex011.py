# Expressões Aritméticas
'''
11) Implemente um algoritmo (fluxograma) e o programa em
Python que leia dois números inteiros (X e Y), calcule conforme a
fórmula a seguir e mostre o resultado:
Fórmula = (-X) + [ (Y-X) +(-Y) . (X)] + 20
'''
X = int(input("X: "))
Y = int(input("Y: "))

res = (-X) + ((Y-X) +(-Y) * (X)) + 20

print(res)