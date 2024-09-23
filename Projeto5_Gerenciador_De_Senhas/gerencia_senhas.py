'''
PROJETO Nº 5 - BANCO DE SENHAS.

NESSE CÓDIGO, VAMOS ORGANIZAR E ARMAZENAR AS SENHAS DO USUÁRIO JUNTO COM SEU USERNAME GERANDO
UM ARQUIVO DE TEXTO CRIPTOGRAFADO. 

PARA ACESSAR O BANCO DE SENHAS, O USUÁRIO DEVERÁ CRIAR E INSERIR UMA SENHA MESTRA PARA DESBLOQUEAR
E VISUALIZAR SUAS SENHAS ARMAZENADAS

**OBS: POR SE TRATAR DE UM CÓDIGO DE TESTES, NÃO UTILIZAR USERNAMES E SENHAS REAIS, POR MOTIVOS DE SEGURANÇA**
'''

senha_mestra = input("Qual será sua senha mestra? ")

def visualizar():
    pass

def adicionar():
    conta = input("\nQual o site/sistema da conta? ")
    nome = input("Username da conta: ")
    senha = input("Senha da conta: ")
    
    with open('senhas.txt', 'a') as f:
        f.write("Conta: " + conta + "; Username: " + nome + "; Senha: " + senha + "\n")


while True:
    modo = input("\nGostaria de adicionar uma nova senha ou visualizar suas senhas armazenadas (visualizar, adicionar)? Digite 'Q' para sair. ").lower()
    if modo == "q":
        break
        
    if modo == "visualizar":
        visualizar()
    elif modo == "adicionar":
        adicionar()
    else:
        print("\nModo inválido!")
        continue