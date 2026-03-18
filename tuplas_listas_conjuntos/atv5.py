mesas = [None] * 15

while True:
    print("\n===== MENU =====")
    print("1 - Confirmar reserva")
    print("2 - Cancelar reserva")
    print("3 - Exibir situação das mesas")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        try:
            numero = int(input("Digite o número da mesa (1 a 15): "))
            if numero < 1 or numero > 15:
                print("Mesa inválida. Digite um número entre 1 e 15.")
                continue

            if mesas[numero - 1] is not None:
                print("Essa mesa já está reservada para:", mesas[numero - 1])
            else:
                nome = input("Digite o nome do cliente: ").strip()
                if nome == "":
                    print("Nome inválido.")
                elif not all(parte.isalpha() for parte in nome.split()):
                    print("Digite apenas letras e espaços.")
                else:
                    mesas[numero - 1] = nome.title()
                    print("Reserva confirmada com sucesso!")

        except ValueError:
            print("Digite um número válido.")

    elif opcao == "2":
        try:
            numero = int(input("Digite o número da mesa (1 a 15): "))
            if numero < 1 or numero > 15:
                print("Mesa inválida. Digite um número entre 1 e 15.")
                continue

            if mesas[numero - 1] is None:
                print("Essa mesa já está livre.")
            else:
                print("Reserva cancelada da mesa", numero, "- Cliente:", mesas[numero - 1])
                mesas[numero - 1] = None

        except ValueError:
            print("Digite um número válido.")

    elif opcao == "3":
        livres = mesas.count(None)
        reservadas = 15 - livres

        print(f"\nMesas livres: {livres}")
        print(f"Mesas reservadas: {reservadas}")

        for i in range(15):
            if mesas[i] is None:
                print(f"Mesa {i+1}: Livre")
            else:
                print(f"Mesa {i+1}: Reservada para {mesas[i]}")

    elif opcao == "4":
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida.")