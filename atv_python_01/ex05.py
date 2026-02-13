# Crie um programa que solicite dois valores numéricos, um numerador e um denominador e realize a
# divisão inteira entre os dois valores. (o denominador não pode ser 0).

denominador = int(input("Digite o denominador: "))
numerador = int(input("Digite um numerador: "))

if (denominador==0):
    print("O denominador não pode ser igual a 0!")
else:
    resultado = (denominador//numerador)

print(f'O resultado da divisão inteira é igual a {resultado}')


