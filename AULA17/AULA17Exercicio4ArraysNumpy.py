 # 4 - Crie um array com valores [100, 200, 300, 400, 500, 600], divida-o (split) esse array em dois arrays separados, cada um com três elementos.  No segundo array resultante, adicione o valor 700 ao final.  Imprima ambos arrays finais.
import numpy as np 

new = np.array([100,200,300,400,500,600])
a,b=np.split(new,2)
print(new)
print(a)
print(b)
b=np.append(b,[700])
print(b)