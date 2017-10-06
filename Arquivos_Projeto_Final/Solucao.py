nomes = []
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

agenda = {}

for i in range(0,len(nomes)):
    agenda[nomes[i]] = telefones[i]

# Passo 2: Inserir novos contatos a partir do teclado

meu_ano_nascimento = 1998
minha_idade = 19
meu_nome = "Pedro"

ultimo_digito_nascimento = int(str(meu_ano_nascimento)[-1])

for i in range(1,ultimo_digito_nascimento + 1):
    nome = input("Digite o nome do contato {}: ".format(i))
    numero = input("Digite o número do contato {}: ".format(i))
    agenda[nome] = numero

# Passo 3: Printar na tela apenas os contatos que passarem de uma certa condição

for contato in agenda.items():
    ultimo_digito_telefone = int(contato[1][-1])
    ultimo_digito_idade = int(str(minha_idade)[-1])
    primeira_letra_nome_contato = contato[0][0]
    primeira_letra_meu_nome = meu_nome[0]

    if ultimo_digito_telefone >= ultimo_digito_idade and primeira_letra_nome_contato > primeira_letra_meu_nome:
        print(contato[0] + ": " + contato[1])
