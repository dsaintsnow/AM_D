import random
import datetime
import math
import requests
from datetime import datetime

while True:

    print("\n==============================")
    print("      LISTA DE EXERCÍCIOS")
    print("==============================")
    print("1 - Módulo math")
    print("2 - Módulo random")
    print("3 - Módulo datetime")
    print("4 - ViaCEP")
    print("5 - AwesomeAPI")
    print("0 - Sair")
    print("==============================")

    opcao = input("Escolha uma opção: ")

    match opcao:

        # ==========================================
        # MÓDULO MATH
        # ==========================================
        case "1":

            numero = float(input("Digite um número: "))

            print(f"\nRaiz quadrada: {math.sqrt(numero)}")

            expoente = float(input("Digite o expoente desejado: "))
            print(f"Potência: {math.pow(numero, expoente)}")

            print(f"Arredondado para cima: {math.ceil(numero)}")
            print(f"Arredondado para baixo: {math.floor(numero)}")

        # ==========================================
        # MÓDULO RANDOM
        # ==========================================
        case "2":

            nomes = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo",  "Fernanda", "Gabriel", "Helena", "Igor", "Juliana"]
            print("\nLista original:")
            print(nomes)
            escolhido = random.choice(nomes)
            print(f"\nNome sorteado: {escolhido}")
            random.shuffle(nomes)
            print("\nLista embaralhada:")
            print(nomes)
            
        # ==========================================
        # MÓDULO DATETIME
        # ==========================================
        case "3":

            agora = datetime.now()

            print("\nData e hora atuais:")
            print(agora.strftime("%d/%m/%Y %H:%M:%S"))

            print("\nDigite uma data futura:")

            dia = int(input("Dia: "))
            mes = int(input("Mês: "))
            ano = int(input("Ano: "))

            data_futura = datetime(ano, mes, dia)

            diferenca = data_futura - agora

            if diferenca.days >= 0:
                print(f"Faltam {diferenca.days} dias.")
            else:
                print("A data informada já passou.")

        # ==========================================
        # VIA CEP
        # ==========================================
        case "4":

            cep = input("Digite o CEP (somente números): ")

            url = f"https://viacep.com.br/ws/{cep}/json/"

            resposta = requests.get(url)

            if resposta.status_code == 200:

                dados = resposta.json()

                if "erro" in dados:
                    print("CEP inválido.")
                else:
                    print("\nEndereço encontrado:")
                    print(f"Logradouro: {dados['logradouro']}")
                    print(f"Bairro: {dados['bairro']}")
                    print(f"Cidade: {dados['localidade']}")
                    print(f"Estado: {dados['uf']}")

            else:
                print("Erro ao consultar o ViaCEP.")

        # ==========================================
        # AWESOME API
        # ==========================================
        case "5":

            url = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL"

            resposta = requests.get(url)

            if resposta.status_code == 200:

                dados = resposta.json()

                print("\nCOTAÇÕES ATUAIS\n")

                print(f"Dólar: R$ {dados['USDBRL']['bid']}")
                print(f"Euro : R$ {dados['EURBRL']['bid']}")
                print(f"Bitcoin: R$ {dados['BTCBRL']['bid']}")

            else:
                print("Erro ao consultar a AwesomeAPI.")

        # ==========================================
        # SAIR
        # ==========================================
        case "0":

            print("Programa encerrado.")
            break

        # ==========================================
        # OPÇÃO INVÁLIDA
        # ==========================================
