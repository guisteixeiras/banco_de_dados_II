voluntarios = []

while True:
    nome = input("Digite o nome do voluntário (ou [0] para encerrar): ").strip()

    if nome.lower() == "0":
        break

    if nome == "":
        print("Entrada inválida. O nome não pode estar vazio.")
        continue

    if not all(parte.isalpha() for parte in nome.split()):
        print("Entrada inválida. Digite apenas letras e espaços.")
        continue

    voluntarios.append(nome.title())
    print("Voluntário cadastrado com sucesso!")

if len(voluntarios) == 0:
    print("Nenhum voluntário foi cadastrado.")
else:
    voluntarios.sort()
    print("\nVoluntários cadastrados em ordem alfabética:")
    for v in voluntarios:
        print(v)