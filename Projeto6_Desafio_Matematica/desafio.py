'''
PROJETO Nº 6 - DESAFIO DE MATEMÁTICA.

NESSE CÓDIGO, VAMOS ELABORAR UM DESAFIO NO QUAL SERÃO EXIBIDOS PROBLEMAS MATEMÁTICOS, NO QUAL O USUÁRIO DEVERÁ
SOLUCIONAR, NÃO SERÁ EXIBIDO UM NOVO PROBLEMA MATEMÁTICO ATÉ O USUÁRIO SOLUCIONAR O PROBLEMA EXIBIDO. 
'''
import random
import time

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

resp_erradas = 0

input("Aperte enter para começar!")
print("--------------------------")

tempo_comeco = time.time()

for i in range(TOTAL_PROBLEMAS):
    expressao, resposta = gerar_problema()
    while True:
        tentativa = input("Problema nº" + str(i + 1) + ": " + expressao + " = ")
        if tentativa == str(resposta):
            break
        resp_erradas += 1
        
tempo_fim = time.time()
tempo_total = tempo_fim - tempo_comeco

print("--------------------------")
print("Mandou bem! Você terminou em ", tempo_total, " segundos!")