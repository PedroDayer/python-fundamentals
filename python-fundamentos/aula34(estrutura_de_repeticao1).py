# ESTRUTURA DE REPETICAO - WHILE + BREAK

'''
Operadores de atribuição:
= += -= *= /= //= **= %=
'''

contador = 1
condicao2 = True
contador2 = 10

while contador < 10:
  print('oi')

  contador += 1 # ou seja => condicao = condicao + 1

while condicao2:
  nome = input('Qual o seu nome: ')

  if nome == 'sair':
    break

  print(f'seu nome é {nome}')


print('saiu')  

contador2 *= '5' # repetição...
print(contador2)