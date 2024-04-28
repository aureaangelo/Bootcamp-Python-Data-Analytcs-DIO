#CALCULAR A DIVISÃO DA COMPRA ENTRE AMIGOS

#Declaração de variáveis
valor_compra = input("Informe o Valor Total da Compra: ")
quantidade_pessoas = input("Informe a quantidade de pessoas: ")

#Cálculo do valor inteiro da divisão
valor_divisao_float = float(valor_compra) // int(quantidade_pessoas)
print(valor_divisao_float)

#Descobrir o valor restante
centavos_restantes = float(valor_compra) - (valor_divisao_float * int(quantidade_pessoas))
print(centavos_restantes)

#Analizar se será divisão inteira ou alguém precisará pagar a mais
if centavos_restantes > 0: 

    print(f'Uma pessoa terá que pagar R$ {int(valor_divisao_float) + centavos_restantes} e o restante precisa pagar R$ {int(valor_divisao_float)}.')

else:

    print(f'Todos precisarão pagar R$ {int(valor_divisao_float)}.')