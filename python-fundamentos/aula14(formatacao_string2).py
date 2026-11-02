# FORMATACAO DE STRING COM Format

'''
String é um objeto e dentro dele possui alguns metodos, como a função format( ... .format)
'''

a = 'A'
b= 'dawdawda'
c = 1.1

string = '{nome1} {nome1} {nome1} {nome2} {nome3:.2f}'
formato = string.format(nome1=a, nome2=b, nome3=c) #chamado de parametro nomeados

print(formato)

#-----

nome = "Pedro"
idade = 21

formatacao = '{1} tem {0} anos'
print(formatacao.format(nome, idade))