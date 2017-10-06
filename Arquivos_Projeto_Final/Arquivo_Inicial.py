nomes =[]
telefones = []

# Lendo o arquivo de entrada com os contatos
aux = []

with open("input.txt","r") as input_file:
    for line in input_file:
        aux = ([x for x in line.split()])
        nomes.append(aux[0])
        telefones.append(aux[1])
aux.clear()


# Codifiquem a partir daqui. Há duas listas: uma com os nomes e a outra com os telefones dos contatos.


# Passo 1: Contruir a agenda


# Passo 2: Inserir novos contatos a partir do teclado


# Passo 3: Printar na tela apenas os contatos que passarem de uma certa condição