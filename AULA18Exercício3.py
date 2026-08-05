"""3 – Crie uma matriz NumPy (2x3): [[1, 2, 3], [4, 5, 6]] e então adicione o vetor [10, 20, 30] a cada linha da matriz usando broadcasting, multiplique a matriz resultante pelo escalar 2 e Imprima a matriz inicial, após soma e após
multiplicação."""

import numpy as np

matriz = np.array([[1, 2, 3], [4, 5, 6]])
print("Matriz inicial:")
print(matriz)
print("="*80)
soma = matriz + np.array([10, 20, 30])
print("\nApós a soma:")
print(soma)
print("="*80)
multiplicacao = soma * 2
print("\nApós a multiplicação:")
print(multiplicacao)
print("="*80)
