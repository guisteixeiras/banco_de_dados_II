nomes_sujos = ["ana", "pedro", "ANA", "marcos", "pedro", "beatriz"]

print("Lista original:")
print(nomes_sujos)

nomes_limpos = []
nomes_vistos = set()

for nome in nomes_sujos:
    nome_formatado = nome.strip().title()
    
    if nome_formatado not in nomes_vistos:
        nomes_vistos.add(nome_formatado)
        nomes_limpos.append(nome_formatado)

print("\nLista final:")
print(nomes_limpos)