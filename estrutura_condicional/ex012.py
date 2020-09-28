# Estrutura Condicional
'''
12) Desenhe um fluxograma e implemente um
programa em Python que recebe os três lados de
um triângulo e, se os valores corresponderem a
lados de um triângulo, informe se é isósceles,
equilátero ou escaleno.

Isósceles: Dois lados iguais e um diferente

Equilátero: Três lados iguais

Escaleno: Três lados com medidas diferentes
'''
A = int(input("Lado a: "))
B = int(input("Lado b: "))
C = int(input("Lado c: "))

if (A == B and B != C or B == C and C != A or A == C and C != B):
    print("TRIANGULO ISOSCELES")

elif (A == B == C):
    print("TRIANGULO EQUILATERO")

elif (A != B != C):
   print("TRIANGULO ESCALENO")