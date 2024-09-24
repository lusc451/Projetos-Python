'''
PROJETO Nº 7 - MÁQUINA CAÇA-NÍQUEL.

NESSE CÓDIGO, VAMOS ELABORAR UMA MÁQUINA DE CAÇA-NÍQUEL, NO QUAL O USUÁRIO IRÁ "DEPOSITAR" UMA QUANTIA EM
DINHEIRO, E PODERÁ JOGAR ATÉ SEU SALDO SE ESGOTAR OU DECIDIR SAIR, CASO O USUÁRIO GANHE, O VALOR SERÁ
ACRESCIDO NO SEU SALDO, PARA QUE POSSA CONTINUAR JOGANDO OU SACAR ESSE SALDO.

**OBS: PROJETO APENAS PARA TESTES DE CONHECIMENTOS EM PYTHON, NÃO FAVORECENDO OU APOIANDO QUALQUER TIPO DE APOSTA ILEGAL**
'''
import random

# Definindo constantes para o caça-níquel
MAX_LINHAS = 3  # Número máximo de linhas disponíveis para apostar
MAX_APOSTAS = 100  # Valor máximo permitido para aposta por linha
MIN_APOSTAS = 1  # Valor mínimo permitido para aposta por linha

LINHAS = 3  # Número de linhas do caça-níquel
COLUNAS = 3  # Número de colunas do caça-níquel

# Dicionário que representa os símbolos disponíveis e a quantidade de cada um
cont_simbolos = {
    "A": 2,  # Símbolo 'A' aparece 2 vezes
    "B": 4,  # Símbolo 'B' aparece 4 vezes
    "C": 6,  # Símbolo 'C' aparece 6 vezes
    "D": 8   # Símbolo 'D' aparece 8 vezes
}

# Dicionário que representa o valor de multiplicação para cada símbolo ao calcular ganhos
valor_simbolos = {
    "A": 5,  # Ganho multiplicado por 5 se o símbolo 'A' estiver alinhado
    "B": 4,  # Ganho multiplicado por 4 se o símbolo 'B' estiver alinhado
    "C": 3,  # Ganho multiplicado por 3 se o símbolo 'C' estiver alinhado
    "D": 2   # Ganho multiplicado por 2 se o símbolo 'D' estiver alinhado
}

# Função para verificar se há três símbolos alinhados em uma linha
def verifica_ganho(colunas, linhas, aposta, valores):
    ganhos = 0
    linhas_ganhos = []
    
    # Percorre cada linha para verificar se há símbolos iguais
    for linha in range(linhas):  # Loop que passa por todas as linhas nas quais o usuário apostou
        simbolo = colunas[0][linha]  # Obtém o símbolo da primeira coluna da linha atual
        
        # Verifica cada coluna na linha para ver se todos os símbolos são iguais
        for coluna in colunas:  # Percorre todas as colunas da linha atual
            checar_simbolo = coluna[linha]
            if simbolo != checar_simbolo:
                break  # Sai do loop se encontrar um símbolo diferente
        else:
            # Adiciona os ganhos caso todos os símbolos sejam iguais na linha
            ganhos += valores[simbolo] * aposta
            linhas_ganhos.append(linha + 1)  # Adiciona a linha (1-indexada) na lista de linhas vencedoras
            
    return ganhos, linhas_ganhos

# Função para girar o caça-níquel e gerar os símbolos aleatoriamente
def giro(linhas, colunas, simbolos):
    todos_simbolos = []
    
    # Preenche a lista 'todos_simbolos' com a quantidade adequada de cada símbolo
    for simbolo, cont_simbolos in simbolos.items():  # Percorre o dicionário de símbolos
        for _ in range(cont_simbolos):  # Adiciona cada símbolo o número de vezes especificado
            todos_simbolos.append(simbolo)
            
    todas_colunas = []
    
    # Gera aleatoriamente os símbolos para cada coluna
    for _ in range(colunas):  # Cria cada coluna (há tantas colunas quanto especificado em 'colunas')
        coluna = []
        simbolo_atual = todos_simbolos[:]  # Copia a lista de todos os símbolos disponíveis
        
        # Preenche cada linha da coluna com um símbolo aleatório
        for _ in range(linhas):  # Gera o símbolo para cada linha da coluna
            value = random.choice(simbolo_atual)  # Escolhe um símbolo aleatório
            simbolo_atual.remove(value)  # Remove o símbolo escolhido para evitar duplicação
            coluna.append(value)  # Adiciona o símbolo à coluna atual
            
        todas_colunas.append(coluna)  # Adiciona a coluna completa à lista de colunas
        
    return todas_colunas

# Função para visualizar os símbolos após o giro
def visualiza_giro(colunas):
    for linha in range(len(colunas[0])):  # Percorre cada linha do caça-níquel
        for i, coluna in enumerate(colunas):  # Percorre cada coluna na linha atual
            if i != len(colunas) - 1:
                print(coluna[linha], end=" | ")  # Adiciona um separador " | " entre os símbolos
            else:
                print(coluna[linha], end="")  # Não adiciona separador no final da linha
                
        print()  # Move para a próxima linha

# Função para solicitar um depósito do usuário
def deposito():
    while True:  # Continua pedindo o depósito até que o usuário insira um valor válido
        valor = input("Digite o valor a ser depositado: R$ ")
        if valor.isdigit():
            valor = int(valor)
            if valor > 0:
                break  # Sai do loop se um valor válido for inserido
            else:
                print("O valor a ser depositado deve ser maior que 0!")
        else:
            print("Digite um valor numérico!")
    return valor

# Função para solicitar o número de linhas que o usuário deseja apostar
def num_linhas():
    while True:  # Continua pedindo o número de linhas até que o usuário insira um valor válido
        linhas = input("Digite o número de linhas que vai apostar (1-" + str(MAX_LINHAS) + ")? ")
        if linhas.isdigit():
            linhas = int(linhas)
            if 1 <= linhas <= MAX_LINHAS:
                break  # Sai do loop se um número de linhas válido for inserido
            else:
                print("Digite um número válido de linhas!")
        else:
            print("Digite um valor numérico para as linhas!")
    return linhas

# Função para solicitar o valor da aposta por linha
def aposta():
    while True:  # Continua pedindo o valor da aposta até que um valor válido seja inserido
        valor = input("Digite o valor a ser apostado em cada linha: R$ ")
        if valor.isdigit():
            valor = int(valor)
            if MIN_APOSTAS <= valor <= MAX_APOSTAS:
                break  # Sai do loop se o valor da aposta estiver no intervalo permitido
            else:
                print(f"O valor a ser apostado deve estar entre R$ {MIN_APOSTAS} - R$ {MAX_APOSTAS}!")
        else:
            print("Digite um valor numérico!")
    return valor

# Função para realizar os giros e calcular o saldo do usuário
def qtd_giros(saldo):
    linhas = num_linhas()
    
    while True:  # Continua pedindo a quantidade a ser apostada até que o saldo seja suficiente
        val_apostado = aposta()
        total_aposta = val_apostado * linhas
        
        if total_aposta > saldo:
            print(f"Você não tem saldo suficiente para apostar essa quantidade, seu saldo atual é de R$ {saldo}")
        else:
            break  # Sai do loop se o usuário tem saldo suficiente para a aposta
        
    print(f"Você está apostando R$ {val_apostado} em {linhas} linhas. A aposta total é igual a R$ {total_aposta}!")
    
    caca_niquel = giro(LINHAS, COLUNAS, cont_simbolos)  # Gira o caça-níquel
    visualiza_giro(caca_niquel)  # Mostra o resultado do giro
    ganhos, linhas_ganhos = verifica_ganho(caca_niquel, linhas, val_apostado, valor_simbolos)  # Verifica os ganhos do usuário
    print(f"Você ganhou R${ganhos}.")
    print(f"Você ganhou nas linhas: ", *linhas_ganhos)
    
    return ganhos - total_aposta  # Retorna o lucro ou prejuízo após o giro

# Função principal que controla o fluxo do jogo
def main():
    saldo = deposito()  # Recebe o depósito inicial do usuário
    
    while True:  # Continua o jogo até que o usuário decida sair
        print(f"Seu saldo atual é de R$ {saldo}")
        girar = input("Aperte enter para girar (aperte Q para sair)")
        if girar == 'q':
            break  # Sai do loop e encerra o jogo se o usuário inserir 'q'
        saldo += qtd_giros(saldo)  # Atualiza o saldo do usuário após cada giro
        
    print(f"Você saiu com R$ {saldo}")  # Exibe o saldo final do usuário quando o jogo termina

# Executa o programa
main()
