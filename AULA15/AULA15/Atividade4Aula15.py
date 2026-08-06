"""4. Consumindo ViaCEP
Solicite um CEP ao usuário.
Utilize o ViaCEP para consultar.
Exiba: Logradouro, Bairro, Cidade e Estado.
Caso o CEP seja inválido, informe o usuário."""

import requests

cep = input("Digite o CEP: ")
url = f"https://viacep.com.br/ws/{cep}/json/"
resposta = requests.get(url)
dados = resposta.json()

if "erro" in dados:
    print("CEP inválido.")
else:
    print("Logradouro:",dados["logradouro"])
    print("Bairro:", dados["bairro"])
    print("Cidade:",dados["localidade"])
    print("Estado:", dados["uf"])
    