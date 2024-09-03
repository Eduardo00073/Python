"""
# Acessando dados em um dicionário
dicionario = {'sp': 'São Paulo', 'rj': 'Rio de Janeiro', 'bh': 'Bahia', 'to': 'Tocantins'}
print(dicionario['sp'])
print(dicionario['to'])

print(dicionario.get('bh'))
print(dicionario.get('pe', 'Não existe'))

# Verificando chaves em um dicionário
dicionario = {'sp': 'São Paulo', 'rj': 'Rio de Janeiro', 'bh': 'Bahia', 'to': 'Tocantins'}
print('sp' in dicionario)
print('pe' in dicionario)
print('São Paulo' in dicionario)

# Tipos de dados em dicionários
localidade = {
    (14.5512, 56.7890): 'Brasil',
    (145.1810, 77.6840): 'Dubai',
    (99.7819, 92.6910): 'África'
}
print(localidade)
print(type(localidade))

# Adicionado elementos em um dicionário
jogos = {1: 'God of War', 2: 'Valorant', 3: 'GTA V'}

jogos[4] = 'Batman'
print(jogos)

novoJogo = {5: 'Mario'}
jogos.update(novoJogo)
print(jogos)

# Atualizando elementos em um dicionário
jogos = {1: 'God of War', 2: 'Valorant', 3: 'GTA V'}
print(jogos)

jogos[1] = 'Counter Strike: GO'
print(jogos)

jogos.update({2: 'The Last of Us'})
print(jogos)
"""

# Removedo elementos em um dicionário
jogos = {1: 'God of War', 2: 'Valorant', 3: 'GTA V'}
print(jogos)

jogos.pop(1)
print(jogos)

del jogos[2]
print(jogos)
