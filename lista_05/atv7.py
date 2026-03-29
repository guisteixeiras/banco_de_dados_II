# 7) Uma loja de eletrônicos deseja premiar os vendedores.
# Armazenar os nomes de 5 vendedores em uma lista
# e seus respectivos totais de vendas em outra lista.
#
# 1) Identificar quem vendeu mais de R$ 5.000,00
# 2) Para esses vendedores, exibir o nome e calcular bônus de 10%
# 3) Para os demais, exibir apenas o nome e a mensagem "Meta não atingida"

vendedores = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo"]
vendas = [6500.00, 4200.00, 8300.00, 5000.00, 2700.00]

for i in range(len(vendedores)):
    nome = vendedores[i]
    total_vendas = vendas[i]

    if total_vendas > 5000:
        bonus = total_vendas * 0.10
        print(f"{nome} vendeu R$ {total_vendas:.2f} e receberá bônus de R$ {bonus:.2f}")
    else:
        print(f"{nome} - Meta não atingida")