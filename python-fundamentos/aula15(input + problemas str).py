# INPUT - leitura de dados
'''
Parece estranho, pois guardamos o valor da "escrita" do usuario numa variavel na mesma linha, ao mesmo tempo em que a funcao input permite um placeholder(texto) para o usuario
'''

nome = input('Qual o seu nome? ')

print("O seu nome é", nome)
print(f'O seu nome é {nome}')
print(f'O seu nome é {nome=}') #Uma forma de pegar o nome da variavel + o seu valor

#----
#Um problema que acontece por ser str

numero1 = input("Digite um numero: ")
numero2 = input("Digite um outro numero: ")

print(f'A soma é: {numero1 + numero2}') # ao inves da soma, há uma concatenacao de string

# como resolver? Basta fazer a conversao de string para int, levando em consideracao uma possivel checagem dos valores antes da conversao, tendo em vista que se o usuario digitar 'a' o sistema quebra pois nao consegue converter
'''
ex: 
int_numero_1 = int(numero1)
int_numero_2 = int(numero2)
print(f'soma {int_numero_1 + int_numero_2}')
'''