# Estrutura Condicional
'''
10) Desenhe um fluxograma e implemente um
programa em Python que recebe a idade de uma
pessoa e informe se possui direito a desconto.
Regra para obter o desconto é necessário ter
menos de 6 anos ou ser idoso (ter a partir de 60
anos).
'''

idade = int(input("Digite sua idade: "))

if (60>idade>6):
    print("Não tem direito ao desconto")
else: print("Tem direito ao desconto")