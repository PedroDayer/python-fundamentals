'''
Funcao print => passamos argumento na funcao 
ex: print(oi) ; oi = argumento 
'''

#funcao com argumentos nao nomeados
print(12, 32)
print(2, 98)
#nota-se que a funcao print, por padrao, da uma quebra de linha(\n) e tambem um espaçamento(sepador) entre os argumentos

print('------------')

#Podemos separar os argumentos que nao sao nomeados por separadores(quaisquer valor) 
print(12, 32, sep="@")
print(2, 98, sep='PEDRO')
print(2, 98, "dawd", sep='')

print('------------')

print(12.4, 32, sep="@", end="##")
print(2, 98, sep='PEDRO', end='\n')
print(2, 98, sep='')

#quando nao colocado o argumento end, tem-se o comportamento padrao da funcao print (pular linha \n)

'''
RESUMO

print: é um comando que recebe vaaaarios argumentos e os mais diversos

argumento:
sep = argumento de separador para argumentos quaisquer nao nomeados(manipula a separacao de argumentos(valores))
end = argumento do final de linha(manipula o separador de linha)
'''