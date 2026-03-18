estoque_produtos1 = (
    "Arroz Agulhinha 5kg", "Feijão Carioca 1kg",
    "Macarrão Espaguete", "Azeite de Oliva Extra Virgem",
    "Café Torrado e Moído", "Pão de Forma Integral",
    "Biscoito Recheado Chocolate",
    "Maçã Gala (Unidade)",
    "Banana Prata (Dúzia)",
    "Suco de Laranja Integral"
)

estoque_produtos2 = (
    "Café Torrado e Moído",
    "Pão de Forma Integral",
    "Leite Integral UHT", "Iogurte Natural", "Peito de Frango Desossado",
    "Patinho Bovino Moído", "Maçã Gala (Unidade)", "Banana Prata (Dúzia)",
    "Suco de Laranja Integral", "Queijo Mussarela Fatiado"
)

relatorio_unificado = tuple(sorted(set(estoque_produtos1 + estoque_produtos2)))

print("Relatório unificado de produtos (sem repetição):")
for produto in relatorio_unificado:
    print(produto)