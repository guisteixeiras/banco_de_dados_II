convidados = []

while True:
    nome = input("Digite o nome do convidado (ou [0] para encerrar): ").strip()

    if nome.lower() == "0":
        break

    if nome == "":
        print("Entrada inválida. O nome não pode estar vazio.")
        continue

    if not all(parte.isalpha() for parte in nome.split()):
        print("Entrada inválida. Digite apenas letras e espaços.")
        continue

    nome = nome.title()

    if nome in convidados:
        print("Esse convidado já foi cadastrado.")
    else:
        convidados.append(nome)
        print("Convidado cadastrado com sucesso!")

if len(convidados) == 0:
    print("Nenhum convidado foi cadastrado.")
else:
    convidados.sort()
    print("\nLista final de convidados:")
    for convidado in convidados:
        print(convidado)