"""
variaveis são usadas para salvar algo na memoria
é possivel jogar quase qualquer coisa dentro de uma variavel

PEP8(documentacao do python): inicie variáveis com letras minusculas, pode usar numero
e underline(_) 
"""

nome_completo = "Pedro Augusto B Dayer"
soma_dois_mais_dois = 2 + 2
int_um = int("1")

print("nome:",nome_completo, soma_dois_mais_dois)

print(int("1"), type(int("1")))
print(int_um, type(int_um), end="\n\n")

nome = "Pedro"
idade = 21
maior_de_idade = idade>=18
print(nome, idade, maior_de_idade)