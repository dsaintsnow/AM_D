"""4 – Crie um array de dimensões (3x1) com valores [10, 20, 30] e então crie outro array unidimensional com valores [1, 2, 3]. Utilize broadcasting para multiplicar esses arrays gerando uma matriz (3x3)por fim imprima claramente os arrays originais e a matriz final."""
import numpy as np

a = np.array([10,20,30])
a_uni = np.array([1,2,3])
matriz_final = a+a_uni

print(f"Array 3x1: {a}")
print("="*80)
print(f"Array Unidimensional: {a_uni}")
print("="*80)
print(matriz_final)
print("="*80)
m_f=np.append(matriz_final,(a,a_uni))
mf=m_f.reshape(3,3)
print(m_f)
print("="*80)
print(mf)
print("="*80)
