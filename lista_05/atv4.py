# 4) Ana é responsável pelo controle de estoque de uma loja de papelaria.
# O programa deve permitir cadastrar produtos em um dicionário,
# onde a chave é o nome do produto e o valor é a quantidade.
#
# Menu:
# 1 - Cadastrar
# 2 - Exibir
# 3 - Atualizar
# 0 - Sair
#
# Validar entradas para não aceitar caracteres inválidos e dados inconsistentes
# e informar se o produto não existir.

estoque = {}

def nome_valido(nome):
    return nome.replace(" ", "").isalpha()

while True:
    print("\n1 - Cadastrar")
    print("2 - Exibir")
    print("3 - Atualizar")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        produto = input("Digite o nome do produto: ").strip()
        if not nome_valido(produto):
            print("Nome inválido.")
            continue

        try:
            quantidade = int(input("Digite a quantidade: "))
            if quantidade < 0:
                print("Quantidade inválida.")
                continue
        except ValueError:
            print("Digite um número inteiro válido.")
            continue

        estoque[produto] = quantidade
        print("Produto cadastrado com sucesso.")

    elif opcao == "2":
        if not estoque:
            print("Nenhum produto cadastrado.")
        else:
            print("\nProdutos cadastrados:")
            for produto, quantidade in estoque.items():
                print(f"{produto}: {quantidade}")

    elif opcao == "3":
        produto = input("Digite o nome do produto para atualizar: ").strip()

        if produto in estoque:
            try:
                nova_quantidade = int(input("Digite a nova quantidade: "))
                if nova_quantidade < 0:
                    print("Quantidade inválida.")
                    continue
            except ValueError:
                print("Digite um número inteiro válido.")
                continue

            estoque[produto] = nova_quantidade
            print("Quantidade atualizada com sucesso.")
        else:
            print("Produto não existe no estoque.")

    elif opcao == "0":
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida.")