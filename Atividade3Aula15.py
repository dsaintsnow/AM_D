"""3. Módulo datetime
Exiba a data e a hora atuais.
Calcule quantos dias faltam para uma data futura (solicitada ao usuário)."""

from datetime import datetime

agora = datetime.now()
print(f"Data e hora atual:{agora} ")

data= input("Digite uma data futura (dd/mm/aaaa): ")
data_futura= datetime.strptime(data,"%d/%m/%Y")
dias = (data_futura - agora).days
print("Faltam",dias, "dias")