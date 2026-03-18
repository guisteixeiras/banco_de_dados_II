notas = []

while len(notas) < 10:
    entrada = input(f"Digite a nota do aluno {len(notas) + 1}: ").strip()

    if entrada == "":
        print("Entrada inválida. Digite uma nota.")
        continue

    try:
        nota = float(entrada)
        notas.append(nota)
    except ValueError:
        print("Entrada inválida. Digite apenas números.")

notas.sort(reverse=True)

print("\nNotas em ordem decrescente:")
for nota in notas:
    print(nota)