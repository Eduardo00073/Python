"""
# exemplo de iteração com for
for elemento in lista1:
    print(elemento)
"""
lista1 = [1, 2, 11, 66, 71, 24, 72, 1, 4]
lista2 = ['P', 'y', 't', 'h', 'o', 'n']
lista3 = [1, 2, 'a', 'b']
lista4 = []
lista5 = list(range(10, -1, -1,))
lista6 = list("Curso de Python")

# exemplo de iteração com while
listaJogos = []
produtos = ''

while produtos != '0':
    produtos = input("Informe o nome de um jogo para adicioná-lo à lista de jogos ou digite 0 para sair:\n")
    if produtos != '0':
        listaJogos.append(produtos)
    else:
        print("Finalizando...\n")

opcao = input("Deseja exibir a lista de jogos? Digite 's' para aceitar ou 'n' para negar: ").lower()
if opcao == 's':
    contagem = 1
    for jogos in listaJogos:
        print(f"Jogo número {contagem}:", jogos)
        contagem += 1
else:
    exit()
