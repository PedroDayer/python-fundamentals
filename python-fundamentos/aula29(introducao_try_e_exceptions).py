# INTRODUCAO AO TRY/EXCEPTION => captura de erros

'''
o try/catch, no python, é o try/exception
'''

numero = input("Informe um numero, irei dobrar ele: ")
 
try:
  numero_float = float(numero)
  print(f'numero {numero} dobrado = {numero_float * 2: .3f}')
except:
  print(f'{numero} não é um número')