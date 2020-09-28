# Expressões Aritméticas
'''
13) Implemente um algoritmo (fluxograma) e o programa em
Python que leia o total de um objeto em estoque, o total vendido
de objetos do mesmo tipo, calcule e mostre o percentual de
objetos vendidos.
Total de um Objeto em Estoque (TE) ----------- 100 %
Total Vendido de Objetos (TV) ------------ X %
X = TV * 100 / TE
'''
# TE: Total Estoque
TE = int(input("Total de estoque: "))
# TV: Total Vendido
TV = int(input("Total vendido: "))

X = TV*100/TE

print("%.1f %%" % X)