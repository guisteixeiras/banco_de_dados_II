projetos = ['Python', 'Java', 'PHP', ' ', 'C', None, 'Jscript', 'HTML', 'SQL', ' ']

encontrados = 0
sem_nome = 0
ausentes = 0

for curso in projetos:

    if curso is None:
        ausentes += 1

    elif curso == ' ':
        sem_nome += 1

    else:
        encontrados += 1

print("Cursos encontrados:", encontrados)
print("Cursos sem nome:", sem_nome)
print("Cursos ausentes:", ausentes)