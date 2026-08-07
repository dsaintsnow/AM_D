"""2 – Crie um array NumPy com os seguintes valores: [12, 15, 20, 25, 30, 35, 40].Utilize funções NumPy para calcular:
Soma total
Média
Desvio padrão
Máximo e mínimo     
Imprima cada resultado com clareza."""

import numpy as np

a = np.array([12, 15, 20, 25, 30, 35, 40])

soma_total = np.sum(a)
print(f"A soma total é: {soma_total}")
print("="*80)
media = np.mean(a)
print(f"A média dos valores é: {media:.2f}")
print("="*80)
desvio = np.std(a)
print(f"O desvio padrão é: {desvio:.2f}")
print("="*80)
maximo = np.max(a)
minimo = np.min(a)
print(f"O Valor Máximo é de: {maximo} e o Valor Mínimo é de: {minimo}")
print("="*80)