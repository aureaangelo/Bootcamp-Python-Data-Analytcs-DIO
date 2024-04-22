# **Aula Versionamento de Código com Git e Github**

## O que é versionamento de código?

É o **controle de versões** para cada atualização de um novo arquivo. Esse controle é necessário principalmente para garantir que nenhum arquivo se perca.

## Sistema de Controle de Versão

- Registra o histórico de atualizações
- Gerencia o histórico e as versões do arquivo
- Organiza, controla e garante a segurança dos arquivos

### Quais os tipos?

1. VCS Centralizado (CVCS)
- Tem um Servidor Centralizado
- Nele existe o banco de versões
- Ex: CVS, Subversion

2. VCS Descentralizado (DVCS)
- Tem servidores locais e Centralizado
- Cada servidor possui sua cópia do arquivo gerenciado
- Também posssui o banco de versões na Centralizado
- No servidor local clona o repositório completo
- Possibilita o trabalho flexível, pois funciona como um backup do arquivo completo
- É possível trabalhar sem internet
- Ex: Git, Mercurial

## **O que é Git?**
- É um Sistema de Controle de Versão Descentralizado (DVCS)
- Gratuito e OpenSource
- Leve e Rápido
- Possui um fluxo Básico

Alguns comandos exemplo:
```
git commit -> Grava alterações no seu repositório
git pull -> Puxa alterações do repositório remoto para o seu repositório local
git push -> Empurra alterações do repositório local para o repositório remoto

```
[Documentação do site oficial do Git sobre o que ele é.](https://git-scm.com/docs/git)

## **O que é Github?**
É uma plataforma de hospedagem de código para controle de versões com git.

> [! Dica]
> [Sintaxe Básica de Gravação e Formatação no Github](https://docs.github.com/pt/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)



## **Configurando o Git**

[Instalando o Git](https://git-scm.com/downloads)

Após a instalação seguir os passsos a seguir:

- Escolher uma pasta para no Explorador de arquivos
- Clicar com o botão direto
- Escolher a opção Git Bash
- No terminal iniciar os comandos a seguir:

```
git config 
git config --global user.name "Nome"
git config --global user.email email.com
git config --global init.default Branch main
git config --global --list
```

A opção `--global` se refere as configurações globais do usuário no computador, porém podem existir situações onde esta opção não seja a ideal. Portanto existem a opção `--system` que vai aplicar as configurações a todos os usuários do computador, e `--local` que vai aplicar as configurações apenas ao repositório local.

O comando `git config --global --list` serve para retornar as configurações globais que estão configuradas no usuário.

Os demais códigos foram usados para definir as configurações essenciais para iniciar um repositório no Git.

[Para saber mais configurações no Git.](https://git-scm.com/docs/git-config)

## **Como hospedar um repositório no Github**

- **No Github**
  - Criar repositório
  - Clicar em <>Code
  - Copiar a URL https

- **No Git Bash**
  - Copiar o seguinte código `git clone URL`
  - Este código irá clonar o repositório criado no repositório local

**Ativação do repositório**

- **No Github**
  - Settings -> <> Developer Settings -> Personal Access Tokens -> Tokens -> Generate New Token (Classic)
  - Configurações:
    - Note: Para que?
    - Expiration: Tempo de duração do Token
    - Select Scopes: Limitações do Token
  - Copiar o código que aparecer para ativar diretamente no git
  - Este código é a senha para conectar o git no Github

- **No Git Bash**
  - Escrever o código no terminal `git config --global credential.helper store`
  - Após isso repetir o processo de clonagem


## **Criando e Clonando Repositórios**

### **1.Transformar um diretório local em repositório git**
- **No git bash**
  - Criar a pasta `mkdir Nome-da-Pasta`
  - Entrar na pasta `cd Nome-da-Pasta`
  - Criar subdiretório .git `git init`
  - Conectar com o repositório remoto `git remote add origin URL`
  - Para verificar o status do .git escrever `git status`
  - Para verificar se a conexão já está ativa:
    - Entrar na pasta .git `cd git`
    - Verificar configurações `cat config`
    - Retornar a pasta do repositório `cd..`


### **2.Clonar um repositório git existente**

- **No git bash**
  - Clonar o repositório `git clone URL`
  - Ou:
  - Clonar o repositório com outro nome `git clone URL Novo-Nome`

## **Salvando alterações no repositório local**

**Criando o Exemplo**
 - Criar a pasta `mkdir Nome-da-Pasta`
 - Entrar na pasta `cd Nome-da-Pasta`
 - Criar subdiretório .git `git init`
 - Criar arquivo README.md `touch README.md`
 - Verificar o status `git status`
 - Escrever algo no arquivo README

 >[Site para escrever e visualizar a criação de README.md](https://readme.so/pt/editor)

**Criando commits**
 - Adicionar os arquivos da área de trabalho para a área de preparação `git add`
 - Verificar o que tem na área de preparação `git status`
 - Adicionar os arquivos da área de preparação no commit `git commit -m "Commit Inicial"`
 - Verificar o status dos commits `git log`

### **Adicionar pasta a gitignore para não aparecer no git**
**Criando o Exemplo**
- Criar a pasta `mkdir Nome-da-Pasta`
- Criar arquivo .md na pasta `touch Nome-da-Pasta/Arquivo.md`
- Adicionar pasta Nome-da-Pasta ao arquivo gitignore `echo Nome-da-Pasta/> .gitignore`
- Verificar se a pasta já é ignorada pelo status `git status`
- Adicionar o arquivo gitignore para a área de preparação `git add .`
- Criar um novo commit com as novas atualizações `git commit -m "Adicionando a pasta gitignore"`
- Verificar o histórico de commits `git log`


## **Desfazendo alterações no repositório local**

   - **Remover o .git a força**

     - Para remover o arquivo .git a força e todo o histórico de commit do repositório execute o código `rm -rf .git`.

  - **Restaurar arquivos**

     - Para restaurar arquivos para o último commit de atualizações execute o código `git restore Nome-do-Arquivo`, isso apagará todas as alterações que foram feitas até o último commit registrado.

  - **Alterar a mensagem do último commit**

    - Para alterar a mensagem do último commit execute o código `git commit --amend -m"Nova Mensagem"`.

### **Retornar alterações com o comando reset**
  - Para todos os comandos a seguir é preciso copiar o código hash do commit que deseja retornar as alterações, para isso no terminal digite o seguinte código `git log`, e copie o código hash.

1. **Retornar alterações para a área de preparação**

    - `git reset --soft codigo-hash`

2.  **Retornar alterações para a área de trabalho**

    - `git reset --mixed codigo-hash`, este código também pode ser feito sem o --mixed, da seguinte forma: `git reset codigo-hash`

3. **Apagar tudo até o commit desejado**

    - `git reset --hard codigo-hash`

    - Para verificar o histórico completo de atualizações em commits execute o código `git reflog`

4. **Exclui arquivo da área de preparação**

    - `git reset Pasta/Arquivo`

5. **Restaurar arquivo para a área de preparação**

    - `git restore --staged Pasta/Arquivo`

[Para saber mais sobre os comandos de reset nos commits](https://git-scm.com/docs/git-reset)
