# INVERTER O VALOR DAS VARIÁVEIS A E B

#Declaração de variáveis
A = input("Escreva o valor da variável A: ")
B = input("Escreva o valor da variável B: ")

#Operação de troca de valores
C = A
A = B
B = C

#Exibição do resultado para o usuário
texto = f"A variável A era igual a {C} e passou a ser {A}, já a variável B era {A} e passou a ser {B}."
print(texto)