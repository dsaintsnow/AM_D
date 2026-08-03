"""1. Módulo math
Calcule a raiz quadrada de um número.
Determine a potência de um número.
Arredonde um número para cima (ceil).
Arredonde um número para baixo (floor)."""

import math
numero = float(input("Digite um número: "))
potencia  = float(input("Digite a potência: "))

resultado = math.pow(numero,potencia)
print(f"A potência é:{resultado}")
