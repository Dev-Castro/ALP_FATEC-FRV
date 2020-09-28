# Expressões Aritméticas
'''
6) Implemente um algoritmo (fluxograma) e o 
programa em Python que recebe a largura e a
altura de uma parede retangular, e a largura
e altura de um azulejo retangular, calcula e
mostra quantos azulejos são necessários para
preencher completamentea parede
'''
parede = input("largura e altura da parede: ").split()
larguraP = float(parede[0])
alturaP = float(parede[1])
azuleijo = input("largura e altura do azuleijo: ").split()
larguraA = float(azuleijo[0])
alturaA = float(azuleijo[1])

aa = larguraA * alturaA
ap = larguraP * alturaP

res = ap/aa

print(res)