"""5. Desafio: AwesomeAPI
Utilizando a AwesomeAPI, mostre a cotação atual de Dólar, Euro e Bitcoin em relação ao Real."""

import requests
url = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL"

resposta = requests.get(url)
dados = resposta.json()

print("Dólar:", dados["USDBRL"]["bid"])
print("Euro:",dados["EURBRL"]["bid"])
print("Bitcoin:",dados["BTCBRL"]["bid"])
