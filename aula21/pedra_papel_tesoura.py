import random
import time


opcao = True
while opcao:
    def jogar():
        print("Opções:\n pedra, papel ou tesoura")
        usuario = input("Qual você escolhe? ").lower()
        computador = random.choice(['pedra', 'papel', 'tesoura'])

        if usuario == computador:
            # pedra > tesoura e < papel, papel > pedra e < que tesoura, tesoura > papel e < pedra.
            return f'\nVocê escolheu {usuario} e o computador escolheu {computador}. Deu empate!'

        if ganhador(usuario, computador):
            return f'\nVocê escolheu {usuario} e o computador escolheu {computador}. Você venceu!!'

        return f'\nVocê escolheu {usuario} e o computador escolheu {computador}. Você perdeu!!'


    def ganhador(usuario, oponente):
        # pedra > tesoura e < papel, papel > pedra e < que tesoura, tesoura > papel e < pedra.
        if (usuario == 'pedra' and oponente == 'tesoura') or (usuario == 'tesoura' and oponente == 'papel') or \
                (usuario == 'papel' and oponente == 'pedra'):
            return True


    print(jogar())

    reiniciar = input("\nDeseja jogar novamente? 's' para Sim e 'n' para Não: ").lower()
    if reiniciar == 's':
        print('Começando novamente...\n')
        time.sleep(1)
    else:
        opcao = False
        print('Finalizando...')
        time.sleep(1)
