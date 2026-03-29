# 8) Você recebeu um dicionário chamado estoque_papelaria
# que contém nomes de produtos como chaves e quantidades disponíveis como valores.
#
# O programa deve:
# 1) Solicitar ao usuário o nome de um produto
# 2) Se o produto existir:
#    a) Se a quantidade for menor que 5, exibir mensagem de nível crítico
#    b) Caso contrário, exibir que o estoque está em dia
# 3) Se não existir, exibir "Produto não cadastrado"

estoque_papelaria = {
    "caneta": 12,
    "lapis": 3,
    "borracha": 8,
    "caderno": 2,
    "marca-texto": 6
}

produto = input("Digite o nome do produto: ").strip().lower()

if produto in estoque_papelaria:
    quantidade = estoque_papelaria[produto]
    if quantidade < 5:
        print(f"Produto {produto} em nível crítico: apenas {quantidade} unidades!")
    else:
        print(f"Estoque em dia: {quantidade} unidades.")
else:
    print("Produto não cadastrado")