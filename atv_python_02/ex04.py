valor_2023 = 30000.00
valor_2024 = 65000.00
valor_2022 = 87000.00

menor = valor_2022
maior = valor_2022

if (valor_2023 < menor):
    menor = valor_2023
if (valor_2023 > maior):
    maior = valor_2023

if (valor_2024 < menor):
    menor = valor_2024
if (valor_2024 > maior):
    maior = valor_2024

print("Valor mais baixo: ", menor)
print("Valor mais alto: ", maior)