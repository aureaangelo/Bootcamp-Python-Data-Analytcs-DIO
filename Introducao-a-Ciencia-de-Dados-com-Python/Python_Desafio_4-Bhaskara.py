
## **CÁLCULO DE BHASKARA NO PYTHON**

#Input para inserir os dados das variáveis para o cálculo
A = input("Escreva o valor de A: ")
B = input("Escreva o valor de B: ")
C = input("Escreva o valor de C: ")

#Calcular o valor de delta
delta = (float(B)**2) - (4 * float(A) * float(C))
print(delta)

#Analisa qual situação o delta se encaixa, negativo, positivo ou igual a 0
if delta<0:
    print(f"A resolução não é possível pois o valor de Delta é negativo no valor de {delta}.")
else:
    #Se o delta for diferente de negativo então ele realiza o cálculo para 0 e para delta positivo
    if delta == 0:
        X = (float(B) * -1)/ 2 * float(A)
        print(f"O valor de delta é 0, portanto o valor de X é {X}")

    else:
        Raiz = delta ** (1/2)
        X1 = (float(B) * -1 + Raiz)/ 2 * float(A)
        X2 = (float(B) * -1 - Raiz)/ 2 * float(A)
        print(f"O valor de Delta é {delta}, sua raiz quadrada é {Raiz}, portanto o valor de X1 é {X1} e o valor de X2 é {X2}")
