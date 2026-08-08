"""
def funcao_retorno():
    return 'Olá, este é um retorno'


retorno = funcao_retorno()
print(retorno)

print(funcao_retorno())
"""


def soma_valores():
    x = 9
    y = 7

    opcao = input("Deseja somar o valor? S para sim e N para não: ").lower()
    if opcao == 's':
        return x + y
    else:
        return 'Saindo...'


print(soma_valores())
