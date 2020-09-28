# Estrutura Condicional
'''
14) Desenhe um fluxograma e implemente um
programa em Python que recebe quatro notas de
um aluno, calcule sua média final, mostre sua
média final junto com sua situação:
Média Final = (2.P1 + 2.P2 + 3.P3 + 3.P4) / 10

Situação:
Aprovado – se a nota for igual ou superior a 7.0

Reprovado – se a nota for menor que 5.0

Se a nota é igual ou superior a 5.0 e menor que 7.0,
leia a nota de exame, calcule e mostre a média com
exame e sua situação:

Média com Exame = (Média Final + Exame) / 2
'''
notas = input().split()

P1 = float(notas[0])
P2 = float(notas[1])
P3 = float(notas[2])
P4 = float(notas[3])

Media = ((P1*2)+(P2*3)+(P3*4)+(P4*1))/10

print("Media: %.1f" % Media)

if (Media >= 7.0):
    print("Aluno aprovado.")
    
if (Media < 5.0):
    print("Aluno reprovado.")
    
if (Media >= 5.0 and Media <= 6.9):
    print("Aluno em exame.")
    NE = float(input())
    print("Nota do exame: %.1f" % NE)
    Media_final = (Media + NE)/2

    if (Media_final >= 7.0):
        print("Aluno aprovado.")
    
    if (Media_final <= 6.9):
        print("Aluno reprovado.")

    print("Media final: %.1f" % Media_final)