'''
PROJETO Nº 6 - DESAFIO DE MATEMÁTICA.

NESSE CÓDIGO, VAMOS ELABORAR UM DESAFIO NO QUAL SERÃO EXIBIDOS PROBLEMAS MATEMÁTICOS, NO QUAL O USUÁRIO DEVERÁ
SOLUCIONAR, NÃO SERÁ EXIBIDO UM NOVO PROBLEMA MATEMÁTICO ATÉ O USUÁRIO SOLUCIONAR O PROBLEMA EXIBIDO. 
'''
import random

OPERADORES = ['+', '-', '*']
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMAS = 5

def gerar_problema():
    esquerda = random.randint(MIN_OPERAND, MAX_OPERAND)
    direita = random.randint(MIN_OPERAND, MAX_OPERAND)
    
    operador = random.choice(OPERADORES)
    
    expressao = str(esquerda) + " " + operador + " " + str(direita)
    resposta = eval(expressao)
    return expressao, resposta

for i in range(TOTAL_PROBLEMAS):
    expressao, resposta = gerar_problema()
    while True:
        tentativa = input("Problema nº" + str(i + 1) + ": " + expressao + " = ")
        if tentativa == str(resposta):
            break
        