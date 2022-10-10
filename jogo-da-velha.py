from time import sleep # Biblioteca a fins de formatação

def imprimirMenuPrincipal():
    contadorX = 0
    contadorO = 0
    print ("Qual modo deseja jogar?\n1. Player contra Player\n2. Player contra Máquina\n3. Sair")
    opcao_modo = int(input("Digite a sua opção: "))
    if opcao_modo == 1:
        modoJogador(contadorO, contadorX)
    elif opcao_modo == 2:
        print("Modo em construção...")               #Aqui o usúario escolhe que modo irá jogar
    elif opcao_modo == 3:                                #Ou se optar, sair da aplicação
        print("Saindo...")
        sleep(1)
        exit()
    else:
        print("Por favor, insira uma opção válida!") 
        imprimirMenuPrincipal()
    return contadorO, contadorX

#Função que inicializa o tabuleiro, tanto a fins de cria-lo como limpá-lo
def inicializaTabuleiro():
    matriz = [[' ' for i in range(3)] 
                 for j in range(3)]
    return (matriz)
def jogadorX(contadorX):
    contadorX += 1
    return contadorX
def jogadorO(contadorO):
    contadorO += 1
    return contadorO
def leiaCoordenadaLinha():
    linha = int(input("Insira a linha: "))
    return linha
def leiaCoordenadaColuna ():
    coluna = int(input("Insira a coluna: "))
    return coluna

#Função onde o usuário decide a coordenada de sua jogada no tabuleiro
def jogadaUsuario(matriz, cont, contadorO, contadorX):
    while verificarVencedor(contadorO, contadorX) <= 3:
        while verificarVencedorRodada(matriz, contadorO, contadorX) == 0:
        
            linha = leiaCoordenadaLinha()
            coluna = leiaCoordenadaColuna()
            while validaPosicao(matriz, coluna, linha) == True: #Checando se a posição é válida
                cont += 1
                jogar(matriz,linha,coluna,cont, contadorO, contadorX)
                return matriz,linha,coluna,cont

#Função que adiciona a coordenada ao local desejado pelo usuário na função anterior
def jogar(matriz,linha,coluna,cont, contadorO, contadorX):
    if cont%2 == 0:
        matriz[linha][coluna] = 'O'
        imprimirTabuleiro(matriz)
        print("Vez do jogador X:")

    elif cont%2 != 0:
        matriz[linha][coluna] = 'X'
        imprimirTabuleiro(matriz)
        print("Vez do jogador O:")
    
    verificaVelha(cont)
    jogadaUsuario(matriz, cont, contadorO, contadorX)

#Função que imprime o status do jogo
def imprimePontuacao(contadorO, contadorX):
    print(f"Jogador O está com {contadorO} pontos.")
    print(f"Jogador X está com {contadorX} pontos.")

#Função que verifica o vencedor da partida
def verificarVencedor(contadorO, contadorX):
    if contadorO == 3:
        print("Jogador O venceu!")
        imprimirMenuPrincipal()
    if contadorX == 3:
        print("Jogador X venceu!")
        imprimirMenuPrincipal()
    else:
        return 0
def verificaVelha(cont):
    if cont >= 9:
        print("Deu velha!")
        return True
    else: 
        False

#Função que verifica o vencedor da rodada
def verificarVencedorRodada(matriz, contadorO, contadorX):
    for i in range(3):
        soma = matriz[0][i]+matriz[1][i]+matriz[2][i]
        if soma == "XXX":
            print("Jogador X pontuou")
            contadorX += 1
            imprimePontuacao(contadorO, contadorX)
            modoJogador(contadorO, contadorX)
        if soma == "OOO":
            print("Jogador O pontuou")
            contadorO += 1
            imprimePontuacao(contadorO, contadorX)
            modoJogador(contadorO, contadorX)
    for i in range (3):
        soma = matriz[i][0] + matriz[i][1] + matriz[i][2]
        if soma == "XXX":
            print("Jogador X pontuou")
            contadorX += 1
            imprimePontuacao(contadorO, contadorX)
            modoJogador(contadorO, contadorX)
        if soma == "OOO":
            print("Jogador O pontuou")
            contadorO += 1
            imprimePontuacao(contadorO, contadorX)
            modoJogador(contadorO, contadorX)
        vitoria_diagonal1 = matriz[0][0] + matriz[1][1] + matriz[2][2]
        vitoria_diagonal2 = matriz[0][2] + matriz[1][1] + matriz[2][0]
        if vitoria_diagonal1 == "XXX":
            print("Jogador X pontuou")
            contadorX += 1
            imprimePontuacao(contadorO, contadorX)
            modoJogador(contadorO, contadorX)
        if vitoria_diagonal1 == "OOO":
            print("Jogador O pontuou")
            contadorO += 1
            imprimePontuacao(contadorO, contadorX)
            modoJogador(contadorO, contadorX)
        if vitoria_diagonal2 == "XXX":
            print("Jogador X pontuou")
            contadorX += 1
            imprimePontuacao(contadorO, contadorX)
            modoJogador(contadorO, contadorX)
        if vitoria_diagonal2 == "OOO":
            print("Jogador O pontuou")
            contadorO += 1
            imprimePontuacao(contadorO, contadorX)
            modoJogador(contadorO, contadorX)

    return 0

#Validação de posição, permitindo a jogada
def validaPosicao(matriz, linha, coluna):
    if matriz[linha][coluna] != ' ' and matriz[coluna][linha] != ' ':
        print("Posição inválida!")
        return False
    else:
        return True

#Imprime o tabuleiro
def imprimirTabuleiro(matriz):
    for i in range(3):
        for j in range(3):
            print(f'|{matriz[i][j]}|', end = '')
        print()

#Função chave que inicializa o jogo 
def modoJogador(contadorO, contadorX):
    matriz = inicializaTabuleiro()
    imprimirTabuleiro(matriz)
    jogadaUsuario(matriz, cont, contadorO, contadorX)
cont = 0           #Variável global
imprimirMenuPrincipal() #Chamando a função principal