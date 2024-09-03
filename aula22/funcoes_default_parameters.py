"""print('Curso de Python')
print()


def multiplica_numero(numero1, numero2=2):
    return numero1 * numero2


print(multiplica_numero(5, 3))
print(multiplica_numero(7))
"""


def exemplo_melhor(nome='João', aluno=False):
    if nome == 'João' and aluno:
        return f'Bem vindo {nome}!'
    elif not aluno:
        return f'Olá {nome}, você não é um aluno.'
    return f'Olá {nome}'


print(exemplo_melhor())
print((exemplo_melhor(aluno=True)))
print(exemplo_melhor(False))
print(exemplo_melhor('Bob Sponja'))
print(exemplo_melhor(nome='Maria'))
