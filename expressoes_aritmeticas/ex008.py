# Expressões Aritméticas
'''
8) Implemente um algoritmo (fluxograma) e o 
programa em Python que recebe o raio de uma
esfera, calcula e mostra seu volume
'''
from math import pi

raio = float(input("raio: "))

volume = 4 * pi * raio**3 / 3

print(volume)