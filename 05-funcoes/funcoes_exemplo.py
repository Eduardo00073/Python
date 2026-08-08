def calcula():
    x = int(input('Informe um número: '))
    y = int(input('Informe outro número: '))

    print("\n1 - Adição\n2 - Subtração\n3 - Divisão\n4 - Multiplicação")
    opcao = int(input('Escolha uma operação: '))
    if opcao == 1:
        print(f'\nO resultado da adição é: {x + y}')
    elif opcao == 2:
        print(f'\nO resultado da subtração é: {x - y}')
    elif opcao == 3:
        print(f'\nO resultado da divisão é: {x / y}')
    elif opcao == 4:
        print(f'\nO resultado da multiplicação é: {x * y}')
    else:
        print('\nOpção inválida!')


calcula()
