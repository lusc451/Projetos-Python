'''
PROJETO Nº 4 - LIVRO DE AVENTURAS.

NESSE CÓDIGO, O USUÁRIO IRÁ PASSAR POR UMA SÉRIE DE DECISÕES EM SUA AVENTURA, BASEADO EM LIVROS DE RPG,
CADA ESCOLHA DO USUÁRIO O LEVA PARA UM CAMINHO DIVERENTE COM CONSEQUÊNCIAS DIFERENTES. 

APÓS A FINALIZAÇÃO DESSE PROJETO, IREI VERIFICAR A VIABILIDADE DE IMPLEMENTAR ESSE JOGO NO FORMATO WEB
UTILIZANDO A BIBLIOTECA FLASK.
'''

nome = input("Digite seu nome: ")
print("\nBem vindo (a), ", nome, " a essa aventura!")

resposta = input("Você está em uma trilha, a sua frente há dois caminhos, o da esquerda e o da direita. Por qual caminho você gostaria de ir? ").lower()

if resposta == "esquerda":
    resposta = input("\nVocê chegou até um rio, você pode dar a volta pelo rio ou nadar através dele. Digite 'volta' para dar a volta no rio ou 'nadar' para nadar através do rio: ").lower()
    
    if resposta == "nadar":
        print("\nVocê tentou nadar através do rio, mas foi comido por um jacaré.")
    elif resposta == "volta":
        print("\nVocê andou por vários quilômetros, ficou sem água ou comida e perdeu o jogo.")
    else:
        print("\nEssa não é uma opção válida, você perdeu!")

elif resposta == "direita":
    resposta = input("\nVocê chegou até uma ponte suspensa, não aparenta ser bem firme, você quer atravessar a ponte ou voltar para a trilha? Digite 'atravessar' para atravessar a ponte ou 'volta' para voltar a trilha: ").lower()
    
    if resposta == "atravessar":
        resposta = input("\nVocê atravessou a ponte e encontrou um estranho. Você fala com ele? S ou N? ").lower()

        if resposta == "s":
            print("\nVocê falou com o estranho, ele lhe ofereceu abrigo, comida, e se ofereceu para guiá-lo de volta para sua casa. Você ganhou!")
        elif resposta == "n":
            print("\nVocê ignorou o estranho, voltou pela ponte, mas no meio do caminho, a ponte se quebra. Você perdeu!")
        else:
            print("\nEssa não é uma opção válida, você perdeu!")
    elif resposta == "volta":
        print("\nVocê voltou para a trilha, mas quando chegou lá, o outro caminho estava impedido por árvores que haviam caído. Você perdeu!")
    else:
        print("\nEssa não é uma opção válida, você perdeu!")
    
else:
    print("\nEssa não é uma opção válida, você perdeu!")