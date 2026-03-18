programacao_evento = [
    "08:30 - Credenciamento",
    "09:00 - Keynote: Economia Global e Oportunidades",
    "10:30 - Estratégias de Inovação",
    "12:00 - Almoço",
    "14:00 - Workshop: Transformação Digital",
    "16:00 - O Futuro das Startups no Brasil",
    "18:00 - Coquetel de Encerramento"
]

programacao_corrigida = programacao_evento[::-1]

print("Programação corrigida:")
for item in programacao_corrigida:
    print(item)