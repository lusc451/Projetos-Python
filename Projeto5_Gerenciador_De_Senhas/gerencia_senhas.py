'''
PROJETO Nº 5 - BANCO DE SENHAS.

NESSE CÓDIGO, VAMOS ORGANIZAR E ARMAZENAR AS SENHAS DO USUÁRIO JUNTO COM SEU USERNAME GERANDO
UM ARQUIVO DE TEXTO CRIPTOGRAFADO. 

PARA ACESSAR O BANCO DE SENHAS, O USUÁRIO DEVERÁ CRIAR E INSERIR UMA SENHA MESTRA PARA DESBLOQUEAR
E VISUALIZAR SUAS SENHAS ARMAZENADAS

**OBS: POR SE TRATAR DE UM CÓDIGO DE TESTES, NÃO UTILIZAR USERNAMES E SENHAS REAIS, POR MOTIVOS DE SEGURANÇA**
'''
from cryptography.fernet import Fernet

'''
def escreve_key(): # Função para gerar Key para criptografia
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''

# Função para ler a Key de criptografia
def ler_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

# Input para criar senha mestra e criptografar a senha mestra
senha_mestra = input("Qual será sua senha mestra? ")
key = ler_key() + senha_mestra.encode()
fer = Fernet(key)

def visualizar():
    with open('senhas.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            nome, senha = data.split("|")
            print("Username:", nome, "| Senha:", fer.decrypt(senha.encode()).decode())

def adicionar():
    nome = input("Username da conta: ")
    senha = input("Senha da conta: ")
    
    with open('senhas.txt', 'a') as f:
        f.write(nome + "|" + fer.encrypt(senha.encode()).decode() + "\n")


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