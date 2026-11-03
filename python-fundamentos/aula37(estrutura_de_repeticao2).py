# WHILE + CONTINUE

'''
formas de utilizar o continue para pular uma repetição(quando achar o 'continue' ele voltar para o inicio do laço)
'''

contador = 0 

while contador <= 100:
  contador += 1

  if contador == 6:
    print('nao vou mostrar o 6')
    continue

  print(contador)

  if contador == 40:
    break

print('saiu!')