# PEP 636 - Correspondência de padrões estruturais: Tutorial
# autor: Michel
# data: 04/09/2022
#
# turorial baseado no 
# PEP 636 – Structural Pattern Matching: Tutorial
# https://peps.python.org/pep-0636/

# 

###   1   ###
voto = input("informe seu voto: ")

print("resposta 1")
# seleção padrão python
if voto == 'candidato1':
  print("candidato-1")
elif voto == 'candidato2':
  print("candidato-2")
else:
  print("voto nulo")
  
  
print("resposta 2")
# usando a correspondência de padrões estruturais - SPM
match voto:
  case  'candidato1':
    print("candidato-1")
  case 'candidato2':
    print("candidato-2")
  case _:  # opcional
    print("voto nulo")
  
# comparando os dois códigos acima
# if voto == 'candidato1':  -->  case  'candidato1':
# else:     -->   case _:
