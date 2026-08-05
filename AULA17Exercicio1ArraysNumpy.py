"""1 – Crie um array NumPy com valores de 0 a 11, faça um reshape deste array para uma matriz 3x4. Utilizando indexação, imprima:
Toda a segunda linha.
O valor localizado na terceira linha, quarta coluna."""
import numpy as np

matriz = np.arange(12).reshape(3, 4)
segunda_linha = matriz[1, :]
print("\nToda a segunda linha:", segunda_linha)
print("="*80)
valor = matriz[2, 3]
print("Valor na 3ª linha e 4ª coluna:", valor)
