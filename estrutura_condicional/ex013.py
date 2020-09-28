# Estrutura Condicional
'''
13) Desenhe um fluxograma e implemente um
programa em Python que recebe a idade de uma
pessoa e exibe sua classificação segundo a regra:

12 anos ou menos – criança
De 12 anos a 17 anos – adolescente
De 18 anos a 59 anos – adulto
Mais de 59 anos - idoso
'''
idade = int(input("Digite sua idade: "))

if(idade<=12):
    print("Classificação: criança")
elif(17>=idade>12):
    print("Classificação: adolescente")
elif(59>=idade>=18):
    print("Classificação: adulto")
elif(59<idade):
    print("Classificação: idoso")