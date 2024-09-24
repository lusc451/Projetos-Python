'''
PROJETO Nº 7 - MÁQUINA CAÇA-NÍQUEL.

NESSE CÓDIGO, VAMOS ELABORAR UMA MÁQUINA DE CAÇA-NÍQUEL, NO QUAL O USUÁRIO IRÁ "DEPOSITAR" UMA QUANTIA EM
DINHEIRO, E PODERÁ JOGAR ATÉ SEU SALDO SE ESGOTAR OU DECIDIR SAIR, CASO O USUÁRIO GANHE, O VALOR SERÁ
ACRESCIDO NO SEU SALDO, PARA QUE POSSA CONTINUAR JOGANDO OU SACAR ESSE SALDO.

**OBS: PROJETO APENAS PARA TESTES DE CONHECIMENTOS EM PYTHON, NÃO FAVORECENDO OU APOIANDO QUALQUER TIPO DE APOSTA ILEGAL**
'''
import random

MAX_LINHAS = 3 # CONSTANTE COM O NÚMERO DE LINHAS NO CAÇA-NÍQUEL
MAX_APOSTAS = 100 # CONSTANTE COM O VALOR MÁXIMO A SER APOSTADO
MIN_APOSTAS = 1 # CONSTANTE COM O VALOR MÍNIMO A SER APOSTADO

LINHAS = 3 # CONSTANTE COM O NÚMERO DE LINHAS DO CAÇA-NÍQUEL
COLUNAS = 3 # CONSTANTE COM O NÚMERO DE COLUNAS DO CAÇA-NÍQUEL

# DICIONÁRIO COM OS "SIMBOLOS" CONTIDOS NAS LINHAS DO CAÇA-NÍQUEL E SUAS QUANTIDADES
cont_simbolos = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

# DICIONÁRIO INFORMANDO O VALOR DE MULTIPLICAÇÃO DE CADA SIMBOLO
valor_simbolos = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

# FUNÇÃO QUE IRÁ VERIFICAR SE HÁ 3 SIMBOLOS ALINHADOS EM UMA LINHA E VALIDAR OS GANHOS DO USUÁRIO
def verifica_ganho(colunas, linhas, aposta, valores):
    ganhos = 0
    linhas_ganhos = []
    
    # LOOP FOR QUE PERCORRE CADA LINHA, VERIFICA O SIMBOLO CONTIDO NELA
    for linha in range(linhas):
        simbolo = colunas[0][linha]
        
        for coluna in colunas:
            checar_simbolo = coluna[linha]
            if simbolo != checar_simbolo:
                break
        else:
            ganhos += valores[simbolo] * aposta
            linhas_ganhos.append(linha + 1)
            
    return ganhos, linhas_ganhos

# FUNÇÃO PARA GIRAR O CAÇA-NÍQUEL, FUNÇÃO QUE IRÁ GERAR ALEATÓRIAMENTE OS SIMBOLOS QUE CADA LINHA E COLUNA TERÁ E SUAS QUANTIDADES
def giro(linhas, colunas, simbolos):
    todos_simbolos = []
    
    # LOOP FOR PARA PERCORRER O DICIONÁRIO DE SIMBOLOS E DISTRIBUIR NA VARIÁVEL "TODOS_SIMBOLOS"
    for simbolo, cont_simbolos in simbolos.items():
        for _ in range(cont_simbolos):
            todos_simbolos.append(simbolo)
            
    todas_colunas = []
    
    # LOOP FOR PARA INSERIR SIMBOLO EM UMA COLUNA E LINHA E REMOVER ESSA OPÇÃO DE SIMBOLO CASO JÁ TENHA ULTRAPASSADO O VALOR MÁXIMO ESTIPULADO NO DICIONÁRIO (EX. A = 2)
    for _ in range(colunas):
        coluna = []
        simbolo_atual = todos_simbolos [:]
        for _ in range(linhas):
            value = random.choice(simbolo_atual)
            simbolo_atual.remove(value)
            coluna.append(value)
            
        todas_colunas.append(coluna)
        
    return todas_colunas

# FUNÇÃO PARA VISUALIZAR OS SIMBOLOS QUE ESTÃO SENDO INSERIDOS NAS LINHAS E COLUNAS
def visualiza_giro(colunas):
    for linha in range(len(colunas[0])):
        for i, coluna in enumerate(colunas):
            if i != len(colunas) -1:
                print(coluna[linha], end=" | ")
            else:
                print(coluna[linha], end="")
                
        print()
    
# FUNÇÃO PARA DEPOSITAR UM VALOR NO SALDO A SER APOSTADO
def deposito():
    # LOOP WHILE PARA RECEBER O VALOR A SER DEPOSITADO, BEM COMO AS CONDICIONAIS NECESSÁRIAS PARA VALIDAR SE O DEPÓSITO ESTÁ SENDO FEITO CORRETAMENTE
    while True:
        valor = input("Digite o valor a ser depositado: R$ ")
        if valor.isdigit():
            valor = int(valor)
            if valor > 0:
                break
            else:
                print("O valor a ser depositado deve ser maior que 0!")
        else:
            print("Digite um valor numérico!")
    return valor

# FUNÇÃO PARA O USUÁRIO DEFINIR A QUANTIDADE DE LINHAS QUE IRÁ APOSTAR NO CAÇA-NÍQUEL
def num_linhas():
    # LOOP WHILE PARA VALIDAR SE O NÚMERO DE LINHAS A SEREM APOSTADAS ESTÃO SENDO INSERIDAS CORRETAMENTE
    while True:
        linhas = input("Digite o número de linhas que vai apostar (1-" + str(MAX_LINHAS) + ")? ")
        if linhas.isdigit():
            linhas = int(linhas)
            if 1 <= linhas <= MAX_LINHAS:
                break
            else:
                print("Digite um número válido de linhas!")
        else:
            print("Digite um linhas numérico!")
    return linhas

# FUNÇÃO PARA O USUÁRIO DEFINIR O VALOR QUE SERÁ APOSTADO POR LINHA
def aposta():
    while True:
        valor = input("Digite o valor a ser apostado em cada linha: R$ ")
        if valor.isdigit():
            valor = int(valor)
            if MIN_APOSTAS <= valor <= MAX_APOSTAS:
                break
            else:
                print(f"O valor a ser apostado deve estar entre R$ {MIN_APOSTAS} - R$ {MAX_APOSTAS}!")
        else:
            print("Digite um valor numérico!")
    return valor

def qtd_giros(saldo):
    linhas = num_linhas()
    
    while True:
        val_apostado = aposta()
        total_aposta = val_apostado * linhas
        
        if total_aposta > saldo:
            print(f"Você não tem saldo suficiente para apostar essa quantidade, seu saldo atual é de R$ {saldo}")
        else:
            break
        
    print(f"Você está apostando R$ {val_apostado} em {linhas} linhas. A aposta total é igual a R$ {total_aposta}!")
    
    caca_niquel = giro(LINHAS, COLUNAS, cont_simbolos)
    visualiza_giro(caca_niquel)
    ganhos, linhas_ganhos = verifica_ganho(caca_niquel, linhas, val_apostado, valor_simbolos)
    print(f"Você ganhou R${ganhos}.")
    print(f"Você ganhou nas linhas: ", *linhas_ganhos)
    
    return ganhos - total_aposta

# FUNÇÃO PRINCIPAL, FUNÇÃO NA QUAL SERÁ CONFERIDO O SALDO DO USUÁRIO, O NÚMERO DE LINHAS A SER APOSTADO E VALIDAR SE O USUÁRIO TEM SALDO PARA APOSTAR
def main():
    saldo = deposito()
    
    while True:
        print(f"Seu saldo atual é de R$ {saldo}")
        girar = input("Aperte enter para girar (aperte Q para sair)")
        if girar == 'q':
            break
        saldo += qtd_giros(saldo)
        
    print(f"Você saiu com R$ {saldo}")
    

main()