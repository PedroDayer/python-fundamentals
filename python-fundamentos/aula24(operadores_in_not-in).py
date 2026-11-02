# OPERADORES IN e NOT IN

'''
in = estar entre
not int = nao estar entre 
'''


'''
Strings sao iteraveis (navegaveis letra por letra, pois possuem indice - parecido com um array)

0  1  2  3  4
P  E  D  R  O
'''
nome = 'Pedro'
print(nome[2])

print('d' in nome)
print(10 * '-')
print('à' in nome)
print('à' not in nome)

print(10 * '-')
nome = input("Digite o seu nome: ")
encontrar = input("Digite o que deseja encontrar: ")

if encontrar in nome:
  print(f'{encontrar} esta em {nome}')
else: 
  print(f'{encontrar} nao esta em {nome}')