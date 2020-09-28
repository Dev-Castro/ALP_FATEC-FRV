# Expressões Aritméticas
'''
3) Implemente um algoritmo (fluxograma) e o 
programa em Python que recebe a largura e a 
altura de um retângulo, calcula e mostra
sua área e seu perímetro.
'''

largura = float(input("largura: "))
altura = float(input("altura: "))

a = largura * altura
p = largura*2 + altura*2

print('Área: %.1f' % a)
print('Perímetro: %.1f' % p)