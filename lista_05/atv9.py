# 9) O professor tem uma lista com os nomes de 6 alunos.
# Para cada nome, o programa deve solicitar duas notas (Nota A e Nota B).
#
# 1) Calcular a média aritmética simples de cada aluno
# 2) Exibir o nome do aluno, sua média e se ele está:
#    - Aprovado (média >= 7,0)
#    - Recuperação (média >= 4,5 e < 7,0)
#    - Reprovado (média < 4,5)
#
# Observação: os critérios foram organizados dessa forma
# porque o enunciado original estava inconsistente.

alunos = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda"]

for aluno in alunos:
    print(f"\nAluno: {aluno}")

    while True:
        try:
            nota_a = float(input("Digite a Nota A: "))
            nota_b = float(input("Digite a Nota B: "))

            if 0 <= nota_a <= 10 and 0 <= nota_b <= 10:
                break
            else:
                print("As notas devem estar entre 0 e 10.")
        except ValueError:
            print("Digite valores numéricos válidos.")

    media = (nota_a + nota_b) / 2

    if media >= 7.0:
        situacao = "Aprovado"
    elif media >= 4.5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    print(f"{aluno} | Média: {media:.2f} | Situação: {situacao}")