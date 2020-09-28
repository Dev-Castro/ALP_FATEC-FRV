# Estrutura Condicional
'''
2) Calculo condicional
'''
n1 = int(input("Digite o 1° Valor: "))
n2 = int(input("Digite o 2° Valor: "))

if n1 > 0 and n2 > 0:

    if n1 > n2:
        res = n1 -n2
    else:
        res = n2 -n1
else:
    
    if n1 > n2:
        res = -n2 -n1
    else:
        res = -n1 -n2

print("Resultado: ", res)