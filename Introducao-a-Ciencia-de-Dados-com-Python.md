
# **Resumo Introdução ao Python**

## **Variáveis e Constantes**
Variáveis ou constantes são utilizados para armazenar valores.
Exemplo:
`name = "Áurea"` ou `NAME = "Áurea"`

### **Variáveis**
Os valores variáveis são valores que podem mudar ao longo do tempo. No Python elas são definidas com o nome da variável em letra minúscula e _. Exemplos:
```
name = "Áurea"
nome_completo = "Áurea Angelo"
```

### **Constantes**
Valores constantes são valores que não serão modificados ao longo do código, normalmente são utilizados para definir algum valor que é essencial e não pode ser alterado. No python não existe uma palavra para declarar valores constantes, mas há um consenso na comunidade que valores constantes são definidos com o nome completo em capslock. Exemplo:
```
ABS_PATH = 'URL'
DEBUG = true
```

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


