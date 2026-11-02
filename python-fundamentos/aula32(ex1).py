numero = input('Digite um valor inteiro: ')

try:
  numero_int = int(numero)
  if (numero_int % 2 == 0):
    print(f'{numero} é um número par')
  else:
    print(f'{numero} é um número ímpar') 
except: 
  print(f"{numero} não é um número inteiro ou não se trata de um número")