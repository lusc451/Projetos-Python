'''
PROJETO Nº 3 - JOGO DE PEDRA, PAPEL E TESOURA

A INTENÇÃO POR TRÁS DESSE PROJETO É APENAS APLICAR CONHECIMENTOS BÁSICOS DE LÓGICA DE PROGRAMAÇÃO
UTILIZANDO A LINGUAGEM PYTHON PARA ELABORAR UM JOGO DE PEDRA, PAPEL E TESOURA. 

APÓS A FINALIZAÇÃO DESSE PROJETO, IREI VERIFICAR A VIABILIDADE DE IMPLEMENTAR ESSE JOGO NO FORMATO WEB
UTILIZANDO A BIBLIOTECA FLASK.
'''
import random

jogador_vence = 0
computador_vence = 0

escolhas = ['pedra', 'papel', 'tesoura']

while True:
    escolha_jogador = input("Escolha entre Pedra/Papel/Tesoura ou digite Q para sair: ").lower()
    if escolha_jogador == "q":
        break
        
    if escolha_jogador not in escolhas:
        continue
        
    num_aleatorio = random.randint(0, 2)
    # pedra = 0, papel = 1, tesoura = 2
    escolha_computador = escolhas[num_aleatorio]
    print("\nO computador escolheu ", escolha_computador)
    
    if escolha_jogador == "pedra" and escolha_computador == "tesoura":
        print("\nVocê ganhou!")
        jogador_vence += 1
    elif escolha_jogador == "papel" and escolha_computador == "pedra":
        print("\nVocê ganhou!")
        jogador_vence += 1    
    elif escolha_jogador == "tesoura" and escolha_computador == "papel":
        print("\nVocê ganhou!")
        jogador_vence += 1
        
    else:
        print("\nVocê perdeu!")
        computador_vence += 1

print("\nVocê ganhou ", jogador_vence, " vezes.")
print("\nO computador ganhou ", computador_vence, " vezes.")
