# VERIFICAR SE ENTROU OU NAO

'''
Parecido com que faziamos com um console.log("entrou")
A diferença é que é um pouco mais escável de se manter no programa

None = nao False e nao True
'''

condicao = False
passou_no_if = None # declaracao da variavel antes do escopo do if

if condicao:
  passou_no_if = True
  print("faça algo...")
else: 
  print("nao faça algo!")

if passou_no_if is None: # ou seja, se estiver com o mesmo valor que atribuimos inicialmente na declaracao de     variaveis significa dizer que ele nao passou no if(nao entrou no escopo do if para mudar de valor(true))
  print("nao passou no if")
else:
  print("passou no if")