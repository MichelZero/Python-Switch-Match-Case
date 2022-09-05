# PEP 636 - Correspondência de padrões estruturais: Tutorial
# autor: Michel
# data: 04/09/2022
#
# turorial baseado no 
# PEP 636 – Structural Pattern Matching: Tutorial
# https://peps.python.org/pep-0636/

# 

###   2   ###
# teste as 4 linhas, remova o comentario
valor = ['teste1'] # lista contendo 1 item
#valor = ['teste1',1] # lista contendo 2 item
#valor = ['teste1',1,2] # lista contendo 3 item
#valor = ['teste1',1,2,3] # lista contendo 4 item


# usando a correspondência de padrões estruturais - SPM
match valor:
    case [a]:
        print(f'contem 1 item: {a}')
    case [a, b]:
        print(f'contem 2 item: {a}, {b}')
    case [a, b, c]:
        print(f'contem 3 item: {a}, {b}, and {c}')
    case [a, b, c, *ultimo]:
        print(f'mais de 3 items: {a}, {b}, {c}, o ultimo é: {ultimo}')
