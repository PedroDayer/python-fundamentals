nome = 'Pedro Augusto'

caracter = len(nome)
novo_nome = ''

contador = 0
while contador < caracter: 

  letra = (nome[contador])

  novo_nome += '*'+ letra 
  contador +=1

novo_nome += '*'
print(novo_nome)