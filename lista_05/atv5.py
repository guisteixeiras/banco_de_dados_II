# 5) Existem duas listas de participantes de uma corrida.
# A primeira já é um dicionário com nome e idade.
# A segunda é uma lista apenas com nomes.
#
# É preciso adicionar uma idade aleatória entre 18 e 60 anos
# para cada nome da Participantes_lista_2 usando random.randint(18, 60),
# depois adicionar esses dados à Participantes_lista_1.
#
# Ao final, mostrar:
# 1) Os nomes de todos os participantes
# 2) As idades de todos os participantes
# 3) Média das idades

import random

Participantes_lista_1 = {
    "Mariana": 25,
    "Carlos": 32,
    "Beatriz": 28,
    "Rafael": 35
}

Participantes_lista_2 = [
    "Ana", "Bruno", "Caio", "Daniela", "Eduardo", "Fernanda",
    "Gabriel", "Helena", "Igor", "Julia", "Kevin", "Larissa",
    "Miguel", "Natália", "Otávio", "Paula", "Ricardo", "Sabrina",
    "Tiago", "Ursula", "Vitor", "Wanessa", "Xavier", "Yara",
    "Zeca", "Arthur"
]

for nome in Participantes_lista_2:
    Participantes_lista_1[nome] = random.randint(18, 60)

print("Nomes dos participantes:")
for nome in Participantes_lista_1.keys():
    print(nome)

print("\nIdades dos participantes:")
for idade in Participantes_lista_1.values():
    print(idade)

media = sum(Participantes_lista_1.values()) / len(Participantes_lista_1)
print(f"\nMédia das idades: {media:.2f}")