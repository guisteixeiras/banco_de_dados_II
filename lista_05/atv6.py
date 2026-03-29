# 6) Organizar um workshop sobre tecnologia e permitir remover participantes
# que desistiram do evento.
#
# O sistema armazena os participantes em um dicionário,
# onde a chave é o nome e o valor é o número da inscrição.
#
# O programa deve ter menu com:
# - listar participantes
# - remover participantes
# Ao remover, solicitar o nome, informar se existe na lista
# e pedir confirmação da remoção.

participantes = {
    "Ana": 101,
    "Bruno": 102,
    "Carlos": 103,
    "Daniela": 104
}

while True:
    print("\n1 - Listar participantes")
    print("2 - Remover participante")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        if not participantes:
            print("Nenhum participante cadastrado.")
        else:
            print("\nLista de participantes:")
            for nome, inscricao in participantes.items():
                print(f"Nome: {nome} | Inscrição: {inscricao}")

    elif opcao == "2":
        nome = input("Digite o nome do participante que deseja remover: ").strip()

        if nome in participantes:
            confirmacao = input(f"Confirma a remoção de {nome}? (s/n): ").strip().lower()
            if confirmacao == "s":
                del participantes[nome]
                print("Participante removido com sucesso.")
            else:
                print("Remoção cancelada.")
        else:
            print("Participante não está na lista.")

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")