import time
import random

palavras = "Amarelo", "Mãe", "Pai", "Garfo", "Pedra", "Mesa", "Porta", "Umbigo", "Mouse", "Teclado", "Óculos", "Óleo",\
    "Cinta", "Mito", "Cela", "Nota", "Tenso", "Caso", "Gado"
palavra_secreta = random.choice(palavras).upper()
underline = []
letra_escolhida_pelo_jogador = []
tentativas = 6
acertos = 0

for c in palavra_secreta:
    underline.append('_')

print("=" * 20)
print("JOGO DA FORCA")
print("=" * 20)

print("Seja bem-vindo, eu sou seu assistente virtual! Deseja inicar o jogo?")
jogar = input("S para sim ou N para não: ").upper()

if jogar == "S":
    print()
    print("\033[33mVocê tem 6 tentativas para descobrir a palavra. Caso contrário, você perde!")
    print("\033[39mEscolhendo a palavra...")
    time.sleep(2)
    print("\033[32mPalavra escolhida com sucesso!")
    print(f"\033[39mA palavra escolhida tem {len(palavra_secreta)} letras.")
    print(underline)
    print()
else:
    print("Até a próxima!")
    exit(0)

while True:
    letra = input("Escolha uma letra: ").upper()[:1]
    letra_escolhida_pelo_jogador.append(letra)
    print(f"Letras já tentadas: {letra_escolhida_pelo_jogador}")

    if letra in palavra_secreta:
        underline[palavra_secreta.index(letra)] = letra
        print("Situação da forca:", underline)
        acertos += 1
        print()
    else:
        tentativas -= 1
        print(f"Você errou! Que pena... Restam {tentativas} tentativa(s).")
        print()

    if tentativas <= 0:
        print("Você perdeu!")
        break
    if acertos == len(palavra_secreta):
        print("Parabéns, você ganhou!!")
        break
