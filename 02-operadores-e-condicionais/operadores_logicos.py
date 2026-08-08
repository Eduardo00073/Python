usuario_ativo = True
usuario_cadastrado = True

if usuario_cadastrado and usuario_ativo:
    print("Usuário cadastrado!")
else:
    print("Usuário não cadastrado.")

print("\n")

produto_exibicao = True
produto_estoque = True

if produto_exibicao or produto_estoque:
    print("Produto disponível para venda!")
else:
    print("Produto indisponível no momento.")
