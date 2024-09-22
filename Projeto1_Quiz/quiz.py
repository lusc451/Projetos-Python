'''
PROJETO Nº 1 - QUIZ SOBRE ANIMES

A INTENÇÃO POR TRÁS DESSE PROJETO É APENAS APLICAR CONHECIMENTOS BÁSICOS DE LÓGICA DE PROGRAMAÇÃO
UTILIZANDO A LINGUAGEM PYTHON PARA ELABORAR UM QUIZ SOBRE ANIMES. 

APÓS A FINALIZAÇÃO DESSE PROJETO, IREI UTILIZAR DA LÓGICA DELE PARA IMPLEMENTAR ESSE QUIZ EM FORMATO
WEB UTILIZANDO A BIBLIOTECA FLASK, IMPLEMENTANDO MAIS QUESTÕES, RESPOSTAS ATRAVÉS DE FORMS, ETC.
'''

print("Bem vindo ao Quiz de animes!\n")

jogador = input("Gostaria de jogar? (s/n): ").lower()

if jogador != "s":
    quit()
    
print("\nÓtimo! Vamos começar! \n\nUtilize a letra das alternativas como resposta (a, b, c, d). \n")
score = 0

resp = input("""1. Qual é o nome do protagonista de One Piece?\n 
a. Zoro
b. Nami
c. Luffy
d. Sanji

Sua resposta: """).lower()

if resp == "c":
    print("Resposta correta!\n")
    score += 1
else:
    print("Resposta errada!\n")
    
resp = input("""2. Em "Naruto", qual é a besta de cauda que está selada dentro de Naruto Uzumaki?\n 
a. Ichibi
b. Yonbi
c. Kyuubi
d. Nanabi

Sua resposta: """).lower()

if resp == "c":
    print("Resposta correta!\n")
    score += 1
else:
    print("Resposta errada!\n")
    
resp = input("""3. Qual é o nome do vilarejo de onde vem Gon Freecss em Hunter x Hunter?\n 
a. Yorknew City
b. Whale Island
c. Heaven’s Arena
d. Isla Baleia

Sua resposta: """).lower()

if resp == "d":
    print("Resposta correta!\n")
    score += 1
else:
    print("Resposta errada!\n")
    
resp = input("""4. Qual o nome do titã que Eren Yeager se transforma em Attack on Titan?\n 
a. Titã Blindado
b. Titã Colossal
c. Titã Fêmea
d. Titã de Ataque

Sua resposta: """).lower()

if resp == "d":
    print("Resposta correta!\n")
    score += 1
else:
    print("Resposta errada!\n")
    
print("Você acertou " + str(score) + " Perguntas!")
print("Você acertou " + str((score / 4) * 100) + "% das perguntas!")