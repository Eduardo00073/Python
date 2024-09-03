def funcao(x, y):
    return x * y


print(funcao(4, 7))

lambda x, y: 4 * 7
nomes = ['Isaac Bradbury', 'Robert Asimov', 'Arthur Herbert', 'Frank Heinlein', 'Leigh Adams', 'Clark H. Brackett',
         'Orson Scott']
print(nomes)

nomes.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(nomes)
