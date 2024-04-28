
# **Resumo Introdução a Ciência de Dados com Python**

## **Instalação do Python**
[Para a Instalação acesse o site oficial](https://www.python.org)

Caso tenha dúvidas sobre a instalação acesse o [Guia de instalação no Windows](https://python.org.br/instalacao-windows/)

## **Baixando e configurando a IDE**
Nesse tutorial vamos utilizar o VSCode por alguns motivos:
- Gratuito
- Suporta multiplas tecnologias
- Boa performance

Para a instalação acesse o site oficial [AQUI](https://code.visualstudio.com).

# **Começando a codificar**

Com tudo configurado o primeiro passo é criar um arquivo com a extenção **.py**

## **Tipos de Dados no Python**
Os tipos de dados definem as características e comportamentos de um valor, com isso podemos fazer cálculos com tipos numéricos, concatenações e extrações em string entre outros.
Os principais tipos são:


| Tipo | Exemplos |
| :---------- | :---------- |
| Texto | str |
| Numérico | int, float, complex |
| Sequência | list, tuple, range |
| Mapa | dict |
| Coleção | set, frozenset |
| Boleano | bool |
| Binário | bytes, bytearray, memoryview |

### 1. Tipos numéricos

- **Números Inteiros**
  - São representados pela classe `int()`
  - Exemplos: -100, -10, -1, 0, 1, 10, 100

- **Números de ponto Flutuante**
  - são representados pela classe `float()`
  - São incluídos todos os Números racionais
  - Exemplos: 1.5, 96.4578, 1.97853254326548

### 1. Tipos boleanos e Strings

- **Valores boleanos**
  - São representados pela classe `bool()`
  - Em python é uma subclasse de `int()`
  - É usado para representar os valores verdadeiro e falso
  - 0 representa `false` e 1 representa `true`

- **Strings**
  - são utilizados para representar valores alfanuméricos
  - São incluídos todos os Números racionais
  - Exemplos: "python", 'python', """python""", "'python'", "p"

  Para saber mais sobre os tipos de dados no python consulte a biblioteca no [Site Oficial](https://docs.python.org/3/library/stdtypes.html).

## **Modo Interativo**

o interpretador python permite ao usuário escrever o código e visualizar o resultado na hora.

### Iniciando o modo Interativo

para iniciar o modo interativo do existem duas formas, a primeira é chamando o interpretador `python`, o segundo é executando o script com a flag -i `python -i app.py`.

### Funções dir e help

### dir
Sem argumentos `dir()`, retorna a lista de nomes no escopo local atual. Com um argumento `dir(100)`, retorna a lista de atributos válidos para o objeto.

### help
Invoca o sistema de ajuda integrado. É possível fazer buscas em modo interativo ou informar por parâmetro qual o nome do módulo, função, classe, método ou variável.

```

help()

help(100)

```

Para saber mais sobre o modo interativo e as funções dir e help acesse o material adicional [Aqui](https://wiki.python.org.br/ModoInterativo).

## **Variáveis e Constantes no Python**
Variáveis ou constantes são utilizados para armazenar valores.
Exemplo:
`name = "Áurea"` ou `NAME = "Áurea"`

### Variáveis
São valores que podem sofrer alterações no decorrrer da execução do código. Esses valores recebem o nome de variáveis, pois elas nascem e não precisam permanecer com o mesmo valor durante a execução do código. Exemplos:

```
idade = 21
nome = "Áurea"

print(f"Meu nome é {nome} e eu tenho {idade} anos de idade.")

idade, nome = (22, "Aurea Souza")

```
No código acima definimos as variáveis `idade` e `nome`, e logo após mudamos o valor das mesmas, pois se trata de uma váriavel.

### Constantes
As constantes são definidas no início do código e permanecem imutáveis. No python não existe uma palavra reservada para declarar uma variável como constante, mas as boas práticas definiram que elas devem ser escritas com todas as letras em capslock `VARIAVEL_CONSTANTE`. Exemplos:

```
ABS_PATH = 'URL'
DEBUG = true
STATES = ['SP', 'RJ', 'MG']

```

## **Conversões de Tipos de Variáveis**

### 1. Inteiro para float
```
preco = 10
print(preco)

preco = float(preco) #conversão com a função float
print(preco)

preco = 10 / 2 #conversão com divisão
print(preco)
```

### 2. Float para inteiro
```
preco = 10.3
print(preco)

preco = int(preco) #conversão com a função int
print(preco)

preco = 21 // 2 #conversão com divisão por inteiro
print(preco)

```

### 3. Conversão por divisão
```
preco = 10
print(preco) 

print(preco / 2) #converte para float

print(preco // 2) #converte para inteiro
```

### 4. Numérico para string (texto)
```
preco = 10.
idade = 28

print(str(preco))
print(str(idade))

texto = f"idade {idade} preço {preco}" #Converte diretamete no texto
print(texto)

```
### 5. String para Numérico
```
preco = "10.50"
idade = "28"

print(float(preco)) #converte para float

print(int(idade)) #converte para inteiro

```

### 6. Erro de conversão
```
preco = "python"

print(float(preco))
```
Nesta execução o código irá exibir uma mensagem informando que não é possível converter o valor. `ValueError: could not convert string to float: 'python'`

## **Funções de Entrada e Saída**

### Lendo valores com a função input
A função builtin input é utilizada quando queremos ler dados da entrada padrão (teclado). Ela recebe um argumento do tipo string, que é exibido para o usuário na saída padrão (tela). A função lê a entrada, converte para string e retorna o valor. Exemplo:
```
nome = input("Informe o seu nome: ")
>>> Informe o seu nome:

```
Para saber mais sobre a função input acesse: [Aqui](https://docs.python.org/3/library/functions.html#input) .

### Exibindo valores com a função print

A função builtin print é utilizada quando queremos exibir dados na saída padrão (tela). Ela recebe um argumento obrigatório e 4 argumentos opicionais (sep, end, file, flush). Todos os objetos são convertidos em string, separados por sep e terminados em end. A string final é exibida ao usuário. Exemplo:

```
nome = "Áurea"
sobrenome = "Souza"

print(nome, sobrenome)
print(nome, sobrenome, end="...\n")
print(nome, sobrenome, sep="-")

>>> Áurea Souza
>>> Áurea Souza...
>>> Áurea-Souza
```
Para saber mais sobre a função print acesse: [Aqui](https://docs.python.org/3/library/functions.html#print).


## **Operadores aritméticos**

Os operadores executam operações matemáticas, como adição, subtração, multiplicação, etc.

## Adição, subtração, multiplicação

```
print(1 + 1) #adição
>>> 2

print(10 - 2) #subtração
>>> 8

print(4 * 3) #multiplicação
>>> 12

```

## Divisão e divisão inteira
```
print(3 / 2) #divisão normal
print(3 // 2) #divisão inteira
>>> 1.5
>>> 1

```

## Módulo 
Faz a divisão dos números e retorna o valor restante.

```
print(10 % 3)
>>> 1
```

## Exponenciação
```
print(4 ** 2)
>>> 16

```

## **Precedência dos operadores**
No Python a Precedência de operadores ocorre da mesma forma que a tradicional utilizada na matemática, a seguir está representada a ordem correta:

  1. Parentesis
  2. Expoentes
  3. Multiplicações e Divisões
  4. Somas e Subtrações

## **OPERADORES DE COMPARAÇÃO**
São utilizados para comparar dois valores.

### Igual (==)
```
saldo = 100
saque = 200

print(saldo == saque)
>>> False
```

### Diferente (!=)
```
saldo = 100
saque = 200

print(saldo != saque)
>>> True
```

### Maior ou Maior Igual (>, >=)
```
saldo = 100
saque = 200

print(saldo > saque)
>>> False
```
```
saldo = 100
saque = 100

print(saldo >= saque)
>>> True
```

### Menor ou Menor Igual (<, <=)
```
saldo = 100
saque = 200

print(saldo < saque)
>>> True
```

## **OPERADORES DE ATRIBUIÇÃO**

### Atribuição simples

```
saldo = 50
print(saldo)
```

## Atribuições compostas
Atribuições podem ser feitas por todos os operadores, adicionando o sinal de igual na frente.

```
Saldo = 500
Saldo += 200 #Adição
>>> 700

Saldo = 500
Saldo -= 200 #Subtração
>>> 300

Saldo = 500
Saldo *= 2 #Multiplicação
>>> 1000

Saldo = 500
Saldo /= 2 #Divisão
>>> 250.0

Saldo = 500
Saldo //= 2 #Divisão inteira
>>> 250

Saldo = 500
Saldo %= 480 #Módulo
>>> 20

Saldo = 4
Saldo **= 2 #Exponenciação
>>> 16

```

## **OPERADORES LOGICOS**

### Operador E (and)
```
saldo = 1000
saque = 200
limite = 100

print(saldo >= saque and saque <= limite)
>>> False

```

### Operador OU (or)
```
saldo = 1000
saque = 200
limite = 100

saldo >= saque or saque <= limite
>>> True

```

### Operador de negação (not)

```
contatos_emergencia = []
not 1000 > 1500
>>> True

not contatos_emergencia
>>> True

not "saque 1500;"
>>> False

not ""
>>> True

```

## **OPERADORES DE IDENTIDADE**
Verifica se um valor é igual ao outro. Exemplos:
```

curso = "Curso de Python"
nome_curso = curso

saldo, limite = 200, 200

print(curso is nome_curso)
>>> True

print(curso is not nome_curso)
>>> False

print(saldo is limite)
>>> True

```

## **OPERADORES DE ASSOCIAÇÃO**
Verifica se o valor está em algum lugar. Exemplos:
```

frutas = ["laranja", "uva", "limão"]

print("limão" in frutas)
>>> True

print("limão" not in frutas)
>>> False

print("abacaxi" in frutas)
>>> False

```

## **IDENTAÇÃO E BLOCOS**
Como o python utiliza a identação do código para a delimitação de blocos de comando?

O papel da identação no código é facilitar a legibilidade e manutenção do mesmo, mas no python ela também exerce um papel mais importante, através da identação o interpretador consegue determinar onde o bloco se inicia e onde ele termina.

Exemplo no python:

```
def sacar(valor):
    saldo = 500
    if saldo >= valor:
        print("valor sacado")
    else:
        print("Sem dinheiro no caixa")
        
print("Obrigada por ser nosso cliente!")

sacar(100)

```

A cada 4 espaços é identificado um novo bloco.

## **ESTRUTURAS CONDICIONAIS**

### Estrutura IF e ELSE
A estrutura if e else é utilizada para a comparação entre variáveis ou valores, ela funciona analizando uma condição e retorna um valor se a condição for verdadeira e retorna outro valor caso seja falsa. Exemplo:

```
saldo = 1000.0
saque = float(input("Informe o valor do saque: "))

if saque <= saldo:
    saldo_restante = saldo - saque
    print(f"Saldo Efetuado com sucesso! Saldo Restante: R$ {saldo_restante}")
else:
    print(f"Saldo insuficiente para saque no valor de R$ {saque}")
```
### Estrutura IF/ELIF/ELSE
A estrutura if elif e else é utilizada para fazer mais de uma comparação na mesma estrutura if. Exemplo:

```
nota = float(input("Informe a sua nota: "))

if nota >= 9:
    print("Aprovado com Excelência!")

elif nota >= 6:
    print("Aprovado.")

else:
    print("Reprovado.")

```

### Estrutura condicional alinhada

Dentro de uma estrutura condicional é possível inserir if dentro de if sem problemas, apenas é preciso se atentar a identação de bloco.

### Estrutura condicional Ternária
Verificações simples em 1 linha, ela é utilizada quando é preciso fazer uma verificação simples que exige um if, mas que não é nescessário utilizar a estrutura completa.

```
saque = 600
saldo = 500

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")
```

## **ESTRUTURAS DE REPETIÇÃO**

### Estrutura for

1. Exemplo Exponenciação
No exemplo a seguir foi criada uma estrutura for que pega cada item da lista `lista` e exibe através da função `print` o número elevado a 2.
```
lista = [1,2,3,4,5,6,7,8,9]

for multiplicacao in lista:
    
    print(multiplicacao ** 2)

>>> 1
>>> 4
>>> 9
>>> 16
>>> 25
>>> 36
>>> 49
>>> 64
>>> 81
```
2. Exemplo sequencia de números
Neste exemplo a função for vai iterar cada número da sequencia range iniciando de 0 até o número 4.
```
for i in range(5):
    print(i)

>>> 0
>>> 1
>>> 2
>>> 3
>>> 4
```
3. Exemplo Letras
O exemplo a seguir analisa cada caracter que foi cadastrado pelo usuário e retorna apenas aqueles que constam na variável VOGAIS. 
```
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
	if letra.upper() in VOGAIS:
		print(letra, end="")

print()  # adiciona uma quebra de linha
```


### Estrutura range
A função range cria uma sequência de números a partir de um início para um fim, ela recebe 3 argumentos: stop (obrigatório - responsável por indicar até quantos números a lista será criada), start (opicional - indica a partir de qual número a sequência se inicia) e step (opicional - indica o intervalo entre os números da sequência)
```
list(range(4))

for numero in range(21):

    print(numero, end=" ")

>>> 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20  

print(" \n")

for numero in range(0, 51, 5):
    print(numero, end=" ")

>>> 0 5 10 15 20 25 30 35 40 45 50 
```

### Comando While
O comando while executa um bloco de código enquando uma condição especificada for verdadeira. Normalmente é utilizada quando não se sabe a quantidade de vezes que o loop precisa ser repetido para atingir algum resultado.

1. Exemplo de contagem regressiva
Nesse exemplo enquando o contador for maior que 0 ele vai exibir o valor e subtrair mais um número, quando chegar em 0, a mensagem a ser exibida será `Fogo!`.
```
contador = 5

while contador > 0:
    print(contador)
    contador -= 1

print("Fogo!")`

>>> 5
>>> 4
>>> 3
>>> 2
>>> 1
>>> Fogo!

```
2. Exemplo Menu Bancário
Este código cria um simples sistema de menu para operações bancárias. 
```
opcao = -1
while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))
        
    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
else:
    print("Obrigado por usar nosso sistema bancário, até logo!")
```

3. Exemplo 
Enquanto o usuário digitar qualquer valor que não seja 10 o código irá se repetir, mas no momento que o usuário digitar 10 o comando irá se encerrar.
```
while True:
    numero = int(input("Informe um número: "))
    if  numero == 10:
        break
    
    print(numero)

```

## **STRING E FATIAMENTO**

### Métodos mais úteis da classe STRING
```
curso = "     pYthOn   "
 
 # Maiúscula, Minúscula e Título
 print(curso.upper()) #Maiúscula
>>> "     PYTHON   "
 
 print(curso.lower()) #Minúscula
>>> "     python   "
 
 print(curso.title()) #Formato de Título, a primeira em maiúsculo e o restante em minúsculo
>>> "     Python   "
 

 # Eliminando espaços em branco da esquerda e direita
 print(curso.strip()) #Retira os espaços da direita e esquerda
>>> "pYthOn"
 
 print(curso.lstrip()) #Retira os espaços da esquerda
>>> "pYthOn   "
 
 print(curso.rstrip()) #Retira os espaços da direita
 >>> "     pYthOn"
 
```

### Junções e centralização

```

curso = "Python"


print(curso.center(10,"#")) #Centraliza a string em 10 caracteres e adiciona # para isso
>>> ##Python##

print(".".join(curso)) #Adiciona . entre cada caracter da string
>>> P.y.t.h.o.n

```

###  **Interpolação de variáveis**

### Old Stile % (Não recomendada)
```
nome = "Áurea"
idade = 21
linguagem = "Python"

print("Olá, me chamo %s. Tenho %d anos de idade, e estou matriculada no curso de %s. Método old." % (nome, idade, linguagem))

>>> Olá, me chamo Áurea. Tenho 21 anos de idade, e estou matriculada no curso de Python. Método old.
```

###  Método format
```
nome = "Áurea"
idade = 21
linguagem = "Python"

# print("Olá, me chamo {}. Tenho {} anos de idade, e estou matriculada no curso de {}. Método format sem nomeação.".format(nome, idade, linguagem))
>>> Olá, me chamo Áurea. Tenho 21 anos de idade, e estou matriculada no curso de Python. Método format sem nomeação.

# print("Olá, me chamo {2}. Tenho {1} anos de idade, e estou matriculada no curso de {0}. Método format com índice.".format(linguagem, idade, nome))
>>> Olá, me chamo Áurea. Tenho 21 anos de idade, e estou matriculada no curso de Python. Método format com índice.

# print("Olá, me chamo {name}. Tenho {age} anos de idade, e estou matriculada no curso de {linguage}. Método format nomeado.".format(name=nome, age=idade, linguage=linguagem))
>>> Olá, me chamo Áurea. Tenho 21 anos de idade, e estou matriculada no curso de Python. Método format nomeado.

```

###  Método f string
```
nome = "Áurea"
idade = 21
linguagem = "Python"

print(f"Olá, me chamo {nome}. Tenho {idade} anos de idade, e estou matriculada no rso de {linguagem}. Método f string")
>>> Olá, me chamo Áurea. Tenho 21 anos de idade, e estou matriculada no curso de Python. Método f string

PI = 3.14159
print(f"O valor de PI é {PI:.2F}")
>>> O valor de PI é 3.14

print(f"O valor de PI é {PI:10.2F}")
>>> O valor de PI é       3.14

```


### Fatiamento de Strings
```
nome = "Aurea de Souza Angelo"

print(nome[0])
>>> A

print(nome[:6])
>>> Aurea

print(nome[6:])
>>> de Souza Angelo

print(nome[6:12])
>>> de Sou

print(nome[1:2:3])
>>> ure

print(nome[:])
>>> Aurea de Souza Angelo

print(nome[::-1])
>>> olegnA azuoS ed aeruA
```

### String de múltiplas linhas ou triplas
```
nome = "Áurea"

mensagem = f'''
Olá, meu nome é {nome},
estou aprendendo Python.

Essa mensagem foi feita com quebra de página através do recurso de strings múltiplas
'''
print(mensagem)
>>>

Olá, meu nome é Áurea,
estou aprendendo Python.

Essa mensagem foi feita com quebra de página através do recurso de strings múltiplas

```
> Para saber mais sobre as funções com variáveis strings [Clique Aqui](https://docs.python.org/pt-br/3/library/string.html)
> Material adicional [Aqui](https://docs.python.org/pt-br/3/library/stdtypes.html#textseq
).
