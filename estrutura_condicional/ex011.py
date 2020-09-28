# Estrutura Condicional
'''
11) Desenhe um fluxograma e implemente um
programa em Python que recebe os três
coeficientes de uma equação do segundo grau,
calcule e informe as raízes reais. O coeficiente do
primeiro termo deve ser diferente de zero. Se não
houver raiz ou se houver apenas uma, informe com
mensagem apropriada.

Fórmula de Bhaskara:

𝑥 = −𝑏 ± √Δ / 2.a

Δ = 𝑏² − 4.𝑎.𝑐

Se o Delta é negativo, não existem raízes reais.
Se o Delta é igual a zero, as raízes são iguais
Se o Delta é positivo, existem duas raízes diferentes
e reais.
'''
import math

a = int(input("\nPrimeiro coeficiente: "))
b = int(input("Segundo coeficiente: "))
c = int(input("Terceiro coeficiente: "))

# Delta
print("\nΔ = b² - 4.a.c")
print("%i² - 4.%i.%i" % (b,a,c))
d1 = b**2
d2 = 4*a*c
print("%.2f - %.2f" % (d1,d2))
d3 = d1 - d2
print("%.2f\n" % d3)

if (d3<0):
    print("Não existem raízes reais")

elif (d3==0):
    print("As raízes são iguais\n")
    x = (-b + math.sqrt(d3))/2*a
    print("x = %.2f" % x)

else:
    print("Existem duas raízes diferentes e reais\n")

    print("x1 = -b+√Δ / 2.a")
    print("x1 = -(%i)+√%i / 2.%i" % (b,d3,a))
    x11 = -b+math.sqrt(d3)
    x12 = 2*a
    print("%.2f / %.2f" % (x11,x12))
    x13 = x11/x12
    print("\nx1 = %.2f\n" % x13)

    print("x2 = -b-√Δ / 2.a")
    print("x2 = -(%i)-√%i / 2.%i" % (b,d3,a))
    x21 = -b-math.sqrt(d3)
    x22 = 2*a
    print("%.2f / %.2f" % (x21,x22))
    x23 = x21/x22
    print("\nx2 = %.2f" % x23)
