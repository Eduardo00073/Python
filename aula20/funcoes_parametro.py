"""
def soma_valores(numero1, numero2):
    return numero1 + numero2


n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

print(soma_valores(n1, n2))
"""


def nome_sobrenome(nome, sobrenome):
    return nome + sobrenome


nome1 = 'João'
sobrenome1 = ' Silva'

print(nome_sobrenome(sobrenome=sobrenome1, nome=nome1))
print(nome_sobrenome(nome=nome1, sobrenome=sobrenome1))
print(nome_sobrenome(nome1, sobrenome1))
