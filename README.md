
# Minicurso de Introdução a Python 3
## Pedro Figueirêdo


Depois de executar com sucesso o nosso


```python
print("Hello World")
```

    Hello World


Podemos passar para as etapas do nosso minicurso.

### Cronograma do minicurso
1. Tipos de Objetos
    * Números
    * Strings
    * Listas
    * Tuplas
    * Dicionários
    * Booleanos
1. Operadores de Comparação
    * Igual e Diferente
    * Menor e Maior
    * Operadores de Comparação Aninhados com Operadores Lógicos
1. Estruturas Condicionais
    * If, else e elif
1. Laços de Repetição
    * While
    * For
1. Projeto Final
    * __Agenda Telefônica__
    * Facilidades do Python Úteis para o Projeto
1. Extra - List Comprehension

## Tipos de Objetos

### Números:

Há dois tipos de números em Python: números inteiros e números de ponto flutuante (reais).
Todas as operações mostradas podem ser feitas com ambos os tipos.


### <font color='red'>Alerta de comparação com C</font>
Em C, numa divisão de inteiros, o resultado é **inteiro**, ou seja, trunca-se o valor resultante.


```python
# Adição
4+5
```




    9




```python
# Subtração
3-10
```




    -7




```python
# Multiplicação
0.5*3
```




    1.5




```python
# Divisão
5/2
```




    2.5




```python
# Potenciação
3**2
```




    9




```python
# Radiciação (Na verdade, é tornar o expoente um número menor que 1)
4**0.5
```




    2.0




```python
# Ordem de operadores pode ser alterada com parênteses
(3 + 2) * (9 - 2)
```




    35



### Strings:

São sequências de caracteres entre ' ' ou " ".

### <font color='red'>Alerta de comparação com C</font>
Em C, não existe, por padrão, o tipo string. Usa-se um vetor de elementos do tipo char para trabalhar-se com strings.
Isso requer conhecimento em manipulação de ponteiros, que pode ser um pesadelo para muita gente!


```python
# Pode ter uma palavra só
A = 'String'
```


```python
# Pode ser uma frase inteira
B = "Isso também é uma string"
```


```python
# Pode-se concatenar strings
A + B
```




    'StringIsso também é uma string'



##### Algumas funções já vêm implementadas nativamente:


```python
A = "Pedro é um belo nome"
```


```python
# Informa o número de caracteres na string
len(A)
```




    20




```python
# Transforma para maiúsculo
A.upper()
```




    'PEDRO É UM BELO NOME'




```python
# Transforma para minúsculo
A.lower()
```




    'pedro é um belo nome'




```python
# Divide a string a cada espaço em branco
A.split()
```




    ['Pedro', 'é', 'um', 'belo', 'nome']



### Listas:

São conjuntos de objetos organizados entre [ ].

### <font color='red'>Alerta de comparação com C</font>
O equivalente para listas, em C, são os **arrays**, que, assim como as strings, dependem de manipulação de ponteiros.
Em Python, diferentemente de C, listas aceitam objetos arbitrários. Não há restrições de tipos para seus elementos.


```python
lista_exemplo1 = [1,7,4,5,6,30]
lista_exemplo2 = ["Pedro","João","José","Maria","Leopoldo","Bob Esponja"]
lista_pythonica = [1, "Python", "Java", 72, "IEEE <3", 42]
```

##### Usa-se a indexação para referir-se a elementos específicos da lista!

Lembrando que, assim como C, **a indexação começa a partir do 0**



```python
# Retorna o quarto elemento da lista_exemplo1
lista_exemplo1[3]
```




    5




```python
# Retorna uma nova lista contento os elementos A PARTIR do terceiro elemento (índice 2) da lista_pythonica
lista_pythonica[2:]
```




    ['Java', 72, 'IEEE <3', 42]




```python
# Retorna uma nova lista contento os elementos ATÉ o quinto elemento (índice 4) da lista_pythonica
lista_exemplo2[:4]
```




    ['Pedro', 'João', 'José', 'Maria']



##### Pode-se fazer muitas outras operações com listas:


```python
# Gera uma nova lista contendo 3 vezes os elementos da lista_exemplo1
lista_exemplo1 * 3
```




    [1, 7, 4, 5, 6, 30, 1, 7, 4, 5, 6, 30, 1, 7, 4, 5, 6, 30]




```python
# Adiciona um novo elemento ao final da lista
lista_exemplo2.append("Jorge Amado")
print(lista_exemplo2)
```

    ['Pedro', 'João', 'José', 'Maria', 'Leopoldo', 'Bob Esponja', 'Jorge Amado']



```python
# Exclui-se um elemento da lista (por padrão, exclui-se o último, mas pode-se passar o índice por parâmetro)
lista_pythonica.pop()
```




    42




```python
# Pode-se inverter a ordem dos elementos da lista
lista_exemplo2.reverse()
print(lista_exemplo2)
```

    ['Jorge Amado', 'Bob Esponja', 'Leopoldo', 'Maria', 'José', 'João', 'Pedro']


### Tuplas:

São similares a listas, com a diferença de serem imutáveis. Foram pensadas para guardar valores que não deveriam ser modificados, como dias da semana ou meses num ano, por exemplo.
São representados por valores entre **( )**.

### <font color='red'>Alerta de comparação com C</font>
Poderia-se traçar uma semelhança com um array em C, com o detalhe de receber o identificador **const**, que significaria que os itens do array não deveriam ser mudados.


```python
# Tuplas não devem ser mudadas. Caso tente, o interpretador irá gerar um erro!
nova_tupla = (3,4,10,"Imutável",21)

nova_tupla[3] = "Mudei!"
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-215-cffa1a14fdf4> in <module>()
          2 nova_tupla = (3,4,10,"Imutável",21)
          3 
    ----> 4 nova_tupla[3] = "Mudei!"
    

    TypeError: 'tuple' object does not support item assignment


### Dicionários:

São pares de objetos organizados como CHAVE e VALOR. Em python, esse grupo é representado por {CHAVE : VALOR}.

### <font color='red'>Alerta de comparação com C</font>
Não existe um equivalente nativo para dicionários em C. Esse tipo de dado é introduzido apenas com a biblioteca STD, no C++.


```python
# Criação de um dicionário
meu_dicionario = {"chave1":"valor1", "chave2":"valor2"}
```


```python
# Obtenção do valor do objeto cuja chave é: 'chave1'
meu_dicionario["chave1"]
```




    'valor1'



**Assim como as listas, os dicionários aceitam tipos variados para o campo VALOR.**


```python
# Dicionário com tipos diferentes
dicionario_invocado = {"chave1":123, "Pedro":"Nome Bonito Demais"}
```


```python
# Obtenção do valor do objeto cuja chave é "Pedro"
dicionario_invocado["Pedro"]
```




    'Nome Bonito Demais'




```python
# Vale tudo mesmo!
dicionario_invocado2 = {"chave1":"IEEE", "chave2":["Lista", "Também", "Vale"]}

dicionario_invocado2
```




    {'chave1': 'IEEE', 'chave2': ['Lista', 'Também', 'Vale']}




```python
# Adicionando novos elementos
dicionario_invocado["novo_chave"] = "Novo elemento"
dicionario_invocado2["chave3"] = ["Será", ["Que", "Funciona?"]]

print("Dicionário 1: ", dicionario_invocado)
print("Dicionário 2: ", dicionario_invocado2)
```

    Dicionário 1:  {'chave1': 123, 'Pedro': 'Nome Bonito Demais', 'novo_chave': 'Novo elemento'}
    Dicionário 2:  {'chave1': 'IEEE', 'chave2': ['Lista', 'Também', 'Vale'], 'chave3': ['Será', ['Que', 'Funciona?']]}


##### Há métodos nativos implementados que facilitam a vida!


```python
# Retorna todas as chaves do dicionário
dicionario_invocado.keys()
```




    dict_keys(['chave1', 'Pedro', 'novo_chave'])




```python
# Retorna todas os valores do dicionário
dicionario_invocado2.values()
```




    dict_values(['IEEE', ['Lista', 'Também', 'Vale'], ['Será', ['Que', 'Funciona?']]])




```python
# Retorna todos os pares (CHAVE,VALOR) do dicionário
meu_dicionario.items()
```




    dict_items([('chave1', 'valor1'), ('chave2', 'valor2')])



##### Se olharmos para o nosso projeto final (Agenda telefônica), já imagina-se que usar dicionário é uma boa!


```python
agenda_telefonica = {"Pedro": "+55 83 9 1234-5321"}

print(agenda_telefonica["Pedro"])
```

    +55 83 9 1234-5321


### Booleanos:

Tipo de dado que tem duas possibilidades: verdadeiro (<font color='green'>True</font>) ou falso (<font color='red'>False</font>).

### <font color='red'>Alerta de comparação com C</font>
Não existe um equivalente nativo para booleanos em C. Usam-se os inteiros 1 e 0 para representar verdadeiro e falso, respectivamente.


```python
IEEE_e_inovador = True
Dormi_mais_de_tres_horas_ontem = False
```


```python
IEEE_e_inovador
```




    True




```python
Dormi_mais_de_tres_horas_ontem
```




    False



## Operadores de Comparação:

Estão presentes em todas as linguagens de programação. Servem para avaliar expressões lógicas.
**Retornam um booleano.**

### <font color='red'>Alerta de comparação com C</font>
Todos os operadores mostrados aqui têm representação fiel em C. Funcionam da mesma maneira e têm mesma sintaxe.

### Igual e Diferente ( == e !=)

Avaliam se os operandos são iguais ou se são diferentes.


```python
True == False
```




    False




```python
IEEE_e_inovador != Dormi_mais_de_tres_horas_ontem
```




    True




```python
2 != 2
```




    False




```python
# Strings representadas por aspas simples ou duplas têm mesmo valor
'' == ""
```




    True



### Menor e Maior ( <, <=, > e >=)

Avaliam se os operandos são menores, menores ou iguais, maiores, maiores ou iguais.


```python
2 <= 3
```




    True




```python
# Python considera o valor de ascII para avaliar caracteres
'a' < 'b'
```




    True




```python
10 > 11
```




    False




```python
# Número de caracteres em 'Pedro' é maior que em 'IEEE'
len("Pedro") >= len("IEEE")
```




    True



### Operadores de Comparação Aninhados com Operadores Lógicos

Trata-se de impor mais de uma comparação ao mesmo tempo na expressão booleana.
Unem-se duas ou mais operadores de comparação utilizando os operadores lógicos **E** e **OU**.

### <font color='red'>Alerta de comparação com C</font>
Funciona da mesma forma que na linguagem C. A diferença está na representação dos símbolos de **E** e **OU**. Em C, são representados por && e ||, respectivamente. Já em Python, é mais intuitivo: **and** e **or**.


```python
x = 3

# 3 é maior que 2 e é menor que 5
3 > 2 and 3 < 5
```




    True




```python
y = 10

# 10 não é maior que 11 nem é menor que 9
y > 11 or y < 9
```




    False




```python
# Para o operador OU, basta uma das expressões dar True, para que o resultado seja True
x < y or 1 > 99
```




    True




```python
# Para o operador E, basta uma das expressões dar False, para que o resultado seja False
x < y and 1 > 99
```




    False



## Estruturas Condicionais

Impõem condições ao código, mudando o curso de execução, de acordo com parâmetros.

### If, else, elif

Estrutura condicional básica de linguagens de programação.
Avalia uma expressão com operador de comparação ( =, <, >, !=).
**Se (if), Senão(else), SenãoSe(elif).**

### <font color='red'>Alerta de comparação com C</font>
Uma das mudanças reside no SenãoSe(elif), que não têm representação em C (é preciso fazer um novo bloco if dentro do else para ter resultado igual).
A segunda é que **não há necessidade de se colocar {}** em Python. O que está dentro de um bloco é **definido pela indentação**. Para sinalizar o início de um bloco, coloca-se o símbolo '**:**'.


```python
# Três maneiras diferentes de utilizar a função print. Todas têm mesmo efeito!
A = 6
B = 5
if (A < B):
    print("{} é menor que {}".format(A,B))
elif(A == B):
    print(A, "é igual a", B)
else:
    print(str(A) + " é maior que " + str(B))
```

    6 é maior que 5



```python
participou_do_minicurso = False
numero_de_linguagens_aprendidas = 0

if(participou_do_minicurso):
    numero_de_linguagens_aprendidas += 1
    print("Aprendi Python!")
elif(numero_de_linguagens_aprendidas == 0):
    print("Uma pena, ainda não aprendi nenhuma linguagem de programação.")
else:
    print("Não fui ao minicurso de Python, mas pelo menos eu sei programar em outra linguagem")
```

    Uma pena, ainda não aprendi nenhuma linguagem de programação.


## Laços de Repetição

Repetem um bloco de código enquanto uma condição não for atingida.

### While

Laço de repetição que tem uma expressão booleana. Sai-se do laço, caso ela tenha valor <font color='red'>False</font>.
Há um bloco else opcional que executa na saída do laço.

### <font color='red'>Alerta de comparação com C</font>
Tem sintaxe e semântica muito parecidos com C. Única mudança será a adição do bloco else opcional que executará na saída do laço while.


```python
# Não executa-se o bloco dentro do while, caso a expressão retorne False desde a primeira execução

while(False):
    print("Executei dentro do While!")
else:
    print("Executei quando acabou o laço while.")
```

    Executei quando acabou o laço while.



```python
x = 0

while(x < 10):
    x += 1
    print("Executei", x, "vez(es) até agora!")
else:
    print("Valor de x ao sair do laço: " + str(x))
```

    Executei 1 vez(es) até agora!
    Executei 2 vez(es) até agora!
    Executei 3 vez(es) até agora!
    Executei 4 vez(es) até agora!
    Executei 5 vez(es) até agora!
    Executei 6 vez(es) até agora!
    Executei 7 vez(es) até agora!
    Executei 8 vez(es) até agora!
    Executei 9 vez(es) até agora!
    Executei 10 vez(es) até agora!
    Valor de x ao sair do laço: 10


### For

Laço de repetição que percorre um conjunto de elementos que estão em uma sequência ou qualquer outro item iterável (lista, dicionário, string, por exemplo).

### <font color='red'>Alerta de comparação com C</font>
Em C, para todo laço for há três campos: o primeiro de inicialização de uma variável contadora, o segundo para conduzir o número de iterações através de uma operação booleana e a terceira é executada em todo final de iteração (geralmente usado para incrementar o contador).
**Para python, tudo isso é simplificado.** Basta indicar o intervalo que se deseja iterar sobre, ou ainda mais útil, basta informar qual o objeto iterável (lista, etc) se deseja percorrer e o python lida com toda a manipulação de variáveis contadoras.


```python
# Para iterar sobre algo por 10 vezes:

for i in range(0,10):
    print("Iteração", i + 1)
```

    Iteração 1
    Iteração 2
    Iteração 3
    Iteração 4
    Iteração 5
    Iteração 6
    Iteração 7
    Iteração 8
    Iteração 9
    Iteração 10



```python
# Iterando sobre uma lista de contatos na Agenda Telefônica (PROJETO)!

agenda = {"Pedro":"+55 83 9 1234-5432", "Nathália":"+55 83 9 2045-5239", "Fernanda":"+55 83 9 1334-1223"}

for contato in agenda.items():
    print(contato[0] + ": " + contato[1])
```

    Pedro: +55 83 9 1234-5432
    Nathália: +55 83 9 2045-5239
    Fernanda: +55 83 9 1334-1223


## Projeto Final

Essa seção é reservada para a explicação do projeto final do minicurso de Python.


### Agenda Telefônica

O problema consistirá de três etapas: 
1. Construção da agenda telefônica a partir do arquivo inicial dado;
1. Inserção de N novos contatos na lista sendo estes requisitados pelo usuário, onde N é o último dígito do ano em que você nasceu;
1. Printar na tela apenas os contatos cujo último digito do telefone é maior ou igual ao último dígito da sua idade **E** cujo nome começa com uma letra do alfabeto posterior à primeira letra do seu nome.


### Facilidades do Python úteis para o projeto

* Ler da entrada comum (teclado):


```python
# Comando para ler uma string do teclado

nome = input("Digite o seu nome: ")

# Para ler um inteiro, usar conversão de objetos

idade = int(input("Digite sua idade: "))
```

    Digite o seu nome: Pedro
    Digite sua idade: 19


* Acessar último elemento de uma lista qualquer:


```python
lista_comum = [1,2,3,45,"Olá","Mundo"]
data_de_nascimento = "06/02/1993"

# Pode-se usar o índice -1 para se referir ao último elemento da lista ou qualquer outro objeto iterável

print("Último termo da Lista comum:", lista_comum[-1])
print("Último número da Data de nascimento:", data_de_nascimento[-1])
```

    Último termo da Lista comum: Mundo
    Último número da Data de nascimento: 3


## Extra - List Comprehension

Resolvi colocar esse assunto extra, caso alunos que estejam mais adiantados, terminem o projeto antes do final do minicurso, além de servir como material extra para que vocês vejam em casa.

A list comprehension é uma funcionalidade do Python derivada das linguagens funcionais (Haskell, OCaml, etc), nas quais expressões matemáticas são resolvidas em uma única linha.

Nela, é possível montar uma lista cujos elementos seguem uma regra.


```python
# Cria uma lista com elementos de 1 a 10
nova_lista = [x for x in range(1,11)]
print(nova_lista)
```

    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



```python
# Aplicabilidade para o projeto!
agenda = {"Pedro":"+55 83 9 9642-2332", "Isabel":"+55 83 9 2232-0902", "Mario":"+55 83 9 9342-3323"}

nomes = [nome for nome in agenda.keys()]
telefones = [numero for numero in agenda.values()]

print("Nomes:", nomes)
print("Telefones:", telefones)
```

    Nomes: ['Pedro', 'Isabel', 'Mario']
    Telefones: ['+55 83 9 9642-2332', '+55 83 9 2232-0902', '+55 83 9 9342-3323']



```python
# Aninhado também vale! Matriz 10x10 com elementos de cada linha indo de 1 a 10.

matriz = [[elemento for elemento in range(1,11)] for linha in range(1,11)]

print(matriz)
```

    [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]

