# CALCULAR O VALOR TOTAL DE VENDA

# Declaração de variáveis
preco = input("Informe o valor unitário do produto: ")

quantidade = input("Informe a quantidade vendida: ")

# Cálculo do valor total de venda
valor_total_venda = float(preco) * float(quantidade)

# Declaração de resultados
print(f'O valor total da venda é de R$ {valor_total_venda}.')