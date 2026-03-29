# 2) Você está desenvolvendo um sistema de acesso que possui três níveis de CRUD:
# n1 - somente leitura
# n2 - leitura e atualização
# n3 - criação, leitura, atualização e exclusão
#
# Fazer um programa que realize o processo de login de três usuários e mostre
# as funcionalidades de acordo com o nível de acesso.
# O login deverá ser composto por CPF e senha.
# Faça a validação se o usuário pode entrar ou não entrar no sistema e,
# se entrar, qual é o nível de acesso.

usuarios = {
    "11111111111": {"senha": "senha123", "nivel": "n1"},
    "22222222222": {"senha": "abc456", "nivel": "n2"},
    "33333333333": {"senha": "xyz789", "nivel": "n3"}
}

funcionalidades = {
    "n1": ["Somente leitura"],
    "n2": ["Leitura", "Atualização"],
    "n3": ["Criação", "Leitura", "Atualização", "Exclusão"]
}

cpf = input("Digite o CPF: ").strip()
senha = input("Digite a senha: ").strip()

if cpf in usuarios:
    if usuarios[cpf]["senha"] == senha:
        nivel = usuarios[cpf]["nivel"]
        print("\nLogin realizado com sucesso!")
        print(f"Nível de acesso: {nivel}")
        print("Funcionalidades permitidas:")
        for funcao in funcionalidades[nivel]:
            print("-", funcao)
    else:
        print("\nAcesso negado: senha incorreta.")
else:
    print("\nAcesso negado: CPF não cadastrado.")