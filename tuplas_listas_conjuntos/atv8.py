produtos = ["Hambúrguer", "Batata Frita", "Refrigerante", "Sorvete"]

print("Lista original:", produtos)

if len(produtos) > 0:
    removido = produtos.pop()
    print("Último produto removido:", removido)
else:
    print("A lista está vazia.")

print("Lista final:", produtos)