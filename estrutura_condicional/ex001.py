# Estrutura Condicional
'''
1) Controle de entrada
'''
n1 = int(input("Digite o 1° Valor (1 a 9): "))
n2 = int(input("Digite o 2° Valor (1 a 9): "))

if n1 < 0 or n1 > 9 or n2 < 0 or n2 > 9:
    print("Valor Inválido!")
else:
    print("Valores Válidos!")