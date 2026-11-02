# INTERPOLACAO BASICA DE STRINGS - vem la da linguagem C

'''
s - string
d e i - int
f - float
x e X - hexadecimal
'''

nome = 'Pedro'
preco = 1000.23123
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %04x' % (1500, 1500))