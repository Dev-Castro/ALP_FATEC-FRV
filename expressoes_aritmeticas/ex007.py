# Expressões Aritméticas
'''
7) Implemente um algoritmo (fluxograma) e o 
programa em Python que recebe o raio da base
e a altura de um cilindro, calcula e mostra
seu volume
'''
from math import pi

raio = float(input("raio: "))
altura = float(input("altura: "))

volume = pi * raio**2 * altura

print(volume)