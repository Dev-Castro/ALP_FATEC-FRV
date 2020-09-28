# Estrutura Condicional
'''
3) Implemente um programa Python que recebe
dois números inteiros e mostre o resultado da
divisão deles. Se o segundo número é igual a zero,
informe que é impossível devido à divisão por zero. 
'''
n1 = int(input("Digite o 1° Valor: "))
n2 = int(input("Digite o 2° Valor: "))

if n2==0:
    print("Impossível dividir")
else:
    print("%i / %i = %.2f" % (n1, n2, n1/n2))