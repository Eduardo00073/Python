"""
lista1 = [1, 2, 11, 66, 71, 24, 72, 1, 4]
lista2 = ['P', 'y', 't', 'h', 'o', 'n']
lista3 = [1, 2, 'a', 'b']
lista4 = []
lista5 = list(range(10, -1, -1,))
lista6 = list("Curso de Python")

# ordenar uma lista
lista2.sort(reverse=True)
print(lista2)

# contagem de ocorrências dentro de uma lista
print(lista6.count('o'))
print(lista1.count(1))

# adicionar elementos dentro de uma lista
print(lista4)
lista4.append([1, 77, 12, 53, 78, 91, 83, 64])
lista4.extend([152, 144, 5, 56])
lista4.extend("Python")
print(lista4)

# adicionar elementos dentro de uma lista em uma posição específica
lista3.insert(2, 15)
print(lista3)

# utilizando o reverse e o copy em listas
lista1.reverse()
print(lista1)
lista4 = lista5.copy()
print(lista4)
"""

lista1 = [1, 2, 11, 66, 71, 24, 72, 1, 4]
lista2 = ['P', 'y', 't', 'h', 'o', 'n']
lista3 = [1, 2, 'a', 'b']
lista4 = []
lista5 = list(range(10, -1, -1,))
lista6 = list("Curso de Python")

# removendo elementos de uma lista
print(lista1)
lista1.pop()
print(lista1)

print(lista6)
lista6.pop(3)
print(lista6)

lista6.clear()
print(lista6)