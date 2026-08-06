from bs4 import BeautifulSoup
import requests
import csv
import numpy as np


pagina = requests.get("https://quotes.toscrape.com")
soup = BeautifulSoup(pagina.text,"html.parser")

frases = soup.find_all("span", class_= "text")
author = soup.find_all("small", class_= "author")
quote = soup.find_all("div", class_= "quote")

titulos = []
autores = []
tags = []

for f in frases:
    titulos.append(f.text)
for a in author:
    autores.append(a.text)
for t in quote:
    tags_html = t.find_all("a",class_="tag")
    lista_tags = []
    for tg in tags_html:
        lista_tags.append(tg.text)
    tags.append(lista_tags)

"""for i in range(len(frases)):

    print("CITAÇÃO: ")
    print(f'{titulos[i]}')
    print("="*75)

    print("AUTOR: ")
    print(f'{autores[i]}')
    print("="*75)

    print("TAGS: ")
    print(f'{tags[i]}')
    print("="*75)"""


arquivo = open("citacoes.csv","w", newline = "",encoding = "UTF-8")

escritor = csv.writer(arquivo)

escritor.writerow(
    ["Citação","Autor","Tags"]
)

for i in range(len(frases)):
    escritor.writerow(
        [titulos[i],
        autores[i],
        ", ".join(tags[i])]
    )

arquivo.close()

"""print("="*75)
print("Arquivo citacoes.csv criado com sucesso.")
print("="*75)"""

tamanho_frases = []
quantidade_tags = []

for frases in titulos:
    tamanho_frases.append(len(frases))
for quote in tags:
    quantidade_tags.append(len(quote))

"""for j in tamanho_frases:
    print(j)"""

array_frases = np.array(tamanho_frases)
"""print(array_frases)"""

array_tags = np.array(quantidade_tags)

print(f"Tamanho das Frases: {array_frases}")
print(f"Contagem das Tags: {array_tags}")
print(np.mean(array_frases))
print(np.max(array_frases))
print(np.min(array_frases))

indice = np.argmax(array_frases)
print(titulos[indice])
print(tamanho_frases[9])

""" Média de caracteres das frases
Média de Tags por frase
Frase mais longa e mais curta
Frase com maior quantidade de Tags
Autor da maior e da menor frase"""
print("A Média de Caracteres é:")
print(np.mean(array_frases))
print("="*80)
print("A Média das Tags é:")
print(np.mean(array_tags))
print("="*80)
print("A Frase mais curta é:")
print(np.min(tamanho_frases))
print("="*80)
print("A Frase mais longa é:")
print(np.max(tamanho_frases))
print("="*80)
