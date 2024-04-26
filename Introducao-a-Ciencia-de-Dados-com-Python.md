
# **Resumo Introdução ao Python**

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



