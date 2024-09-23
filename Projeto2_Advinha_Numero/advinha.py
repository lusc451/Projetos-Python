'''
PROJETO Nº 2 - ADVINHAR O NÚMERO ALEATÓRIO

A INTENÇÃO POR TRÁS DESSE PROJETO É APENAS APLICAR CONHECIMENTOS BÁSICOS DE LÓGICA DE PROGRAMAÇÃO
UTILIZANDO A LINGUAGEM PYTHON PARA ELABORAR UM JOGO DE ADVINHAÇÃO DE UM NÚMERO ALEATÓRIO. 

APÓS A FINALIZAÇÃO DESSE PROJETO, IREI UTILIZAR DA LÓGICA DELE PARA IMPLEMENTAR ESSE JOGO EM FORMATO
WEB UTILIZANDO A BIBLIOTECA FLASK.
'''

import random

limite = input("Digite um número: ")

if limite.isdigit():
    limite = int(limite)
    
    if limite <= 0:
        print("\nDigite um número maior que 0!")
        quit()
else:
    print("\nDigite um valor numérico!")
    quit()

num_aleatorio = random.randint(0, limite)

tentativas = 0

while True:
    tentativas += 1
    advinha = input("\nTente advinhar o número aleatório: ")
    
    if advinha.isdigit():
        advinha = int(advinha)
    else:
        print("\nDigite um valor numérico!")
        continue
    
    if advinha == num_aleatorio:
        print("\nVocê acertou!")
        break
    elif advinha > num_aleatorio:
        print("O número digitado é maior que o número aleatório")
    else:
        print("O número digitado é menor que o número aleatório")
        
print("\nVocê acertou em ", tentativas, " tentativas")