# Expressões Aritméticas
'''
5) Implemente um algoritmo (fluxograma) e o 
programa em Python que recebe a largura de uma
parede quadrada e a largura de um azulejo quadrado,
calcula e mostra quantos azulejos são necessários
para preencher completamente a parede
'''
parede = float(input("parede: "))
azuleijo = float(input("azuleijo: "))

aa = azuleijo**2
ap = parede**2

res = ap/aa

print(res)