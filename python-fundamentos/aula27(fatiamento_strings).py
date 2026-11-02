# FATIAMENTO DE STRINGS
''' Quando usar?
Extrair trechos fixos de um texto: Pegar apenas os primeiros ou últimos caracteres de uma palavra ou código (ex: extrair o DDD de um telefone ou os 3 primeiros dígitos de um CPF);
Separar dados padronizados;
Inverter uma string.
'''

'''
lembre-se que strings sao itaraveis(cada letra de um palavra possui um indice, podendo ser acessado) => 
ex:
nome = 'Pedro' 
print(nome[2]) => d
'''

'''
Fatiamento [i:f:p] [::]
string[inicio : fim : passo]
passo = de quanto em quanto ele vai pular 
'''

'''
A funcao len retorna a quantidade de caracteres da string
'''

nome = 'Olá Mundo'
print(nome[4:8]) # obs: se omitir(4:) ele vai até o final

print(len(nome))
print(len(nome[7]))
print(nome[0: len(nome): 1])
print(nome[0: len(nome): 2])
print(nome[:: -1]) # inversao da string

