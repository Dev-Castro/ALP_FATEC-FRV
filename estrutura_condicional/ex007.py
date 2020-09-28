# Estrutura Condicional
'''
7) Desenhe um fluxograma e implemente um
programa em Python que recebe quatro números
reais e informe se há algum repetido ou não.
'''
entrada = input().split()

L = []
repete = False

for i in entrada:
    i = float(i)
    L.append(i)

for x in L:
    
    if L.count(x)>=2:
        repete = True

if repete:
    print("Tem número repetido")
else: print("Os números não se repetem")