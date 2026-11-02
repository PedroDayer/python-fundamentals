numero1 = input("Informe um numero: ")
numero2 = input("Informe um outro numero: ")

numero1 = float(numero1)
numero2 = float(numero2)

if(numero1 > numero2):
  print(f'{numero1=} é maior do que {numero2=}')
elif (numero2 > numero1):
  print(f'{numero2=} é maior do que {numero1=}')
else:
  print(f'Ambos sao iguais. {numero1} = {numero2: 2f}')  