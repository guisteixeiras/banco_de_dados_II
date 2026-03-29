# 10) Criar um programa que peça ao usuário 10 números inteiros, um por um.
# À medida que os números forem digitados:
# - armazenar os pares em uma lista chamada pares
# - armazenar os ímpares em uma lista chamada impares
#
# Ao final, exibir:
# 1) A lista completa de números pares
# 2) A lista completa de números ímpares
# 3) A soma dos números pares e a soma dos números ímpares

pares = []
impares = []

for i in range(10):
    while True:
        try:
            numero = int(input(f"Digite o {i+1}º número inteiro: "))
            break
        except ValueError:
            print("Digite um número inteiro válido.")

    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("\nLista de números pares:")
print(pares)

print("\nLista de números ímpares:")
print(impares)

print(f"\nSoma dos pares: {sum(pares)}")
print(f"Soma dos ímpares: {sum(impares)}")