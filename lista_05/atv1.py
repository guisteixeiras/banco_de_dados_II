# 1) Uma editora deseja comparar dois artigos para identificar quais palavras
# aparecem em ambos. Criar um programa que receba os dois textos e exiba
# um conjunto com as palavras comuns entre eles.
#
# Depois, Laura e Ana criaram listas diferentes de compras. O programa deve mostrar:
# a) Quais itens apareceram nas duas listas
# b) Quais foram exclusivos de Laura
# c) Quais foram exclusivos da Ana

import re

texto1 = """
O desenvolvimento de software moderno exige domínio absoluto sobre algoritmos
e estruturas de dados complexas. Python se destaca como uma ferramenta poderosa,
permitindo que desenvolvedores criem soluções eficientes para problemas reais
com código limpo.
"""

texto2 = """
Grandes desenvolvedores utilizam Python para resolver problemas complexos com
eficiência e elegância. O domínio sobre a linguagem permite a criação de
software de alto nível, transformando algoritmos em soluções reais que
impactam o mundo moderno.
"""

def limpar_texto(texto):
    texto = texto.lower()
    palavras = re.findall(r'\b\w+\b', texto)
    return set(palavras)

palavras_texto1 = limpar_texto(texto1)
palavras_texto2 = limpar_texto(texto2)

palavras_comuns = palavras_texto1.intersection(palavras_texto2)

print("Palavras comuns entre os textos:")
print(palavras_comuns)

print("\n" + "=" * 50 + "\n")

lista_laura = {
    "Picanha", "Carvão", "Cerveja", "Refrigerante", "Pão de alho",
    "Queijo coalho", "Linguiça", "Asinha de frango", "Farofa", "Gelo",
    "Cebola", "Tomate", "Vinagre", "Sal", "Papel toalha"
}

lista_ana = {
    "Arroz", "Feijão", "Azeite", "Alface", "Banana", "Maçã", "Batata",
    "Ovos", "Leite", "Detergente", "Cebola", "Tomate", "Vinagre",
    "Sal", "Papel toalha"
}

comuns = lista_laura.intersection(lista_ana)
exclusivos_laura = lista_laura.difference(lista_ana)
exclusivos_ana = lista_ana.difference(lista_laura)

print("Itens em comum:")
print(comuns)

print("\nItens exclusivos de Laura:")
print(exclusivos_laura)

print("\nItens exclusivos de Ana:")
print(exclusivos_ana)