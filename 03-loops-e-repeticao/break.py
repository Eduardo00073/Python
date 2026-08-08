for c in range(0, 11):
    if c == 5:
        print(f"Número {c} atingido, saindo...")
        break
    else:
        print(c)

while True:
    parada = int(input("\nDigite 0 para finalizar as iterações do bloco while: "))
    if parada == 0:
        print("Finalizando...")
        break
    else:
        print("O número digitado não foi 0, retornando...")
