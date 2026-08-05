######### 2 – Crie dois arrays 1D NumPy com valores [1, 2, 3] e [4, 5, 6] e concatene-os formando um único array. Após isso, faça slicing para obter apenas os elementos [2, 3, 4, 5].

import numpy as np

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

array_completo = np.concatenate((array1, array2))
resultado = array_completo[1:5]

print("Array Completo:", array_completo)
print("="*80)
print(resultado)