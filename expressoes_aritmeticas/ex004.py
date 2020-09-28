# Expressões Aritméticas
'''
4) Implemente um algoritmo (fluxograma) e o 
programa em Python que recebe o raio de uma
circunferência, calcula e mostra sua área
e seu perímetro
'''
from math import pi

raio = float(input('Raio: '))

a = pi * raio**2
p = 2 * pi * raio

print('Área: %.2f' % a)
print('Perímetro: %.2f' % p)
