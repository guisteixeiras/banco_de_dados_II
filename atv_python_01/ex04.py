#4 Crie um programa que solicite dois valores numéricos, um operador e uma potência, e realize a
# exponenciação entre esses dois valores

numerador = int(input("Digite o numerador: "))
expoente = int(input("Digite o expoente: "))

potencia = (numerador**expoente)

print(f'{numerador} elevado a {expoente} é igual a {potencia}')
