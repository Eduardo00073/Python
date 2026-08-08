"""
conjunto = set({1, 2, 2, 3, 1, 4, 5, 4, 6, 3, 7})
print(conjunto)
print(type(conjunto))

conjunto2 = {1, 'b', False, '155', 986}
print(conjunto2)

for valor in conjunto2:
    print(valor)
"""

visitantes = ['São Paulo', 'Araraquara', 'Campinas', 'São Paulo', 'Campinas', 'Araraquara', 'São Paulo', 'Campinas']
print(visitantes)
print(set(visitantes))

conjunto = {'Olá', 12, True}
print(conjunto)
conjunto.add('Hello World')
print(conjunto)

conjunto.remove(True)
print(conjunto)
