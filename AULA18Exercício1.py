# – Crie dois arrays NumPy: A = [10, 20, 30, 40, 50] e B = [1, 2, 3, 4, 5].  Realize as seguintes operações entre eles:     
"""Soma Adição: numpy.add(x1, x2)
Subtração: numpy.subtract(x1, x2)
Multiplicação: numpy.multiply(x1, x2)
Divisão: numpy.divide(x1, x2)

Imprima claramente cada resultado."""

import numpy as np

A = np.array([10,20,30,40,50])
B = np.array([1,2,3,4,5])

C = np.add(A,B)
print(f"A Soma é de: {C}")
print("="*80)

D = np.subtract(A,B)
print(f"A Subtração é de: {D}")
print("="*80)

E = np.multiply(A,B)
print(f"A Multiplicação é de: {E}")
print("="*80)
F = np.divide(A,B)
print(f"A Divisão é de: {F}")
