hora_informada = input('Que horas são? ')

try:

  hora = int(hora_informada)

  if hora >= 0 and hora <=11 :
    print("Bom dia!")
  elif hora >=12 and hora <=17 :
    print('Boa tarde!')
  elif hora >=18 and hora <=23 :
    print('Boa noite!')
  else:
    print('Valor invalido!') 
    
except:
  print(f'{hora_informada} nao se trata de um numero')    