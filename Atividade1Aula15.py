"""1. Módulo math
Calcule a raiz quadrada de um número.
Determine a potência de um número.
Arredonde um número para cima (ceil).
Arredonde um número para baixo (floor)."""

import math

numero = float(input("Digite um número: "))

raiz = math.sqrt(numero)
print("="*75)
print("Raiz quadrada:", raiz)
print("="*75)
print("Arredondando para cima:", math.ceil(raiz))
print("="*75)
print("Arredondando para baixo:", math.floor(raiz))

expoente = float(input("Digite o expoente: "))
print("="*75)
print("Potência:", math.pow(numero, expoente))
print("="*75)
