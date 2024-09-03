from time import sleep


def menu():
    continuar = 1
    while continuar:
        continuar = int(input("Opções:\n 0 - Sair \n 1 - Iniciar\nEscolha: "))
        if continuar:
            jogar()
        else:
            print("Saindo...")
            sleep(1)


def jogar():
    jogada = 0

    while ganhou() == 0:
        print(f"\nJogador {jogada % 2 + 1}")
        exibe()
        linha = int(input("\nLinha: "))
        coluna = int(input("Coluna: "))

        if tabuleiro[linha - 1][coluna - 1] == 0:
            if (jogada % 2 + 1) == 1:
                tabuleiro[linha - 1][coluna - 1] = 1
            else:
                tabuleiro[linha - 1][coluna - 1] = -1
        else:
            print("Posição já ocupada, tente novamente!")
            jogada -= 1

        if ganhou():
            print(f"Jogador {jogada % 2 + 1} ganhou após {jogada + 1} rodadas")

        jogada += 1


def ganhou():
    # checando as linhas
    for i in range(3):
        soma = tabuleiro[i][0] + tabuleiro[i][1] + tabuleiro[i][2]
        if soma == 3 or soma == -3:
            return 1

    # checando colunas
    for i in range(3):
        soma = tabuleiro[0][i] + tabuleiro[1][i] + tabuleiro[2][i]
        if soma == 3 or soma == -3:
            return 1

    # checando diagonais
    diagonal1 = tabuleiro[0][0] + tabuleiro[1][1] + tabuleiro[2][2]
    diagonal2 = tabuleiro[0][2] + tabuleiro[1][1] + tabuleiro[2][0]
    if diagonal1 == 3 or diagonal1 == -3 or diagonal2 == 3 or diagonal2 == -3:
        return 1

    return 0


def exibe():
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == 0:
                print(" _ ", end=' ')
            elif tabuleiro[i][j] == 1:
                print(" x ", end=' ')
            elif tabuleiro[i][j] == -1:
                print(" o ", end=' ')

        print()


tabuleiro = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]

menu()

