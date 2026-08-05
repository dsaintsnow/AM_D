###3 – Crie um array original com valores [10, 20, 30, 40, 50].  Faça uma cópia deste array.  Remova o elemento 30 da cópia sem alterar o original.  Imprima os dois arrays para mostrar que o original permanece inalterado.

import numpy as np

a = np.array([10,20,30,40,50])
b = np.copy(a)
b = np.delete(b,[2])
print(a)
print(b)