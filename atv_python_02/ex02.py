vendas_2023 = float(input("Digite o total de vendas em 2023: "))
vendas_2024 = float(input("Digite o total de vendas em 2024: "))

percentual = ((vendas_2024 - vendas_2023) / vendas_2023) * 100

print(f"\nO percentual de crescimento foi de: {percentual:.2f}%")

if percentual > 0:
    print("Resultado: Houve crescimento.")
elif percentual < 0:
    print("Resultado: Houve decrescimento.")
else: 
    printf("Resultado: Não houve movimento.")
