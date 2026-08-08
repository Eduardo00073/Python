from time import sleep


print("Menu:\n 0 - Sair\n 1 - Contador\n 2 - Contador Regressivo\n")
opcao = input("Informe qual opção você deseja: ")

if opcao == '1':
    tempo = int(input("Quanto tempo você deseja contar?\nR: "))
    for c in range(1, tempo + 1):
        print(c)
        sleep(1)
    print("Finalizando...")
    sleep(1)
elif opcao == '2':
    tempo = int(input("Quanto tempo você deseja contar?\nR:"))
    for c in range(tempo, -1, -1):
        print(c)
        sleep(1)
    print("Finalizando...")
    sleep(1)
elif opcao == '0':
    print("Finalizando...")
    sleep(1)
else:
    print("\nInforme uma opção válida!\nFinalizando...")
    sleep(1)
