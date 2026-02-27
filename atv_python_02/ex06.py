numeros = []
for i in range(3):
    numeros.append(float(input(f"Digite o {i+1}º número: ")))

print(f"Crescente: {sorted(numeros)}")
print(f"Decrescente: {sorted(numeros, reverse=True)}")