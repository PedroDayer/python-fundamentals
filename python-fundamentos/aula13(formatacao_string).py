# f-strings FORMATACAO(uma delas) . f de formatacao

'''
utilizacao do 'f' antes da string para permitir formatar casas decimais e tambem colocar variaveis dentro de uma string ( utilizando chaves )
'''

nome = "Pedro Augusto"
peso = 72
altura = 1.822312

imc = peso / (2 * altura)

linha_2 = f'Seu nome: {nome}'
linha_3 = f'Seu peso: {peso} e altura: {altura: .2f}'
linha_4 = f'Seu IMC: {imc: .3f}'

print("---- Seus dados ----\n")
print(linha_2)
print(linha_3)
print(linha_4, end="\n\n")
