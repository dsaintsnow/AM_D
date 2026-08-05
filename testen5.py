import numpy as np

a = np.array(["Débora","Maria","Polllyana","Mara","Yasmin"])
print(a.ndim)
print("="*80)

b = np.array([[[2,3,4],[5,6,7]],[[2,3,4],[5,6,7]]])
print(b.size)
print("="*80)

c = np.array([[7,8,9],[12,33,44]])
print(f"TAMANHO: {c.size}")
print(f"NÚMERO DE DIMENSÕES: {c.ndim}")
print(f"FORMATO: {c.shape}")
print(f"TIPOS DE DADOS: {c.dtype}")
print("="*80)

d = np.array([1,2,3,4,5,6,7,8,9])
new_d = d.reshape(3,3)
print(d)
print(new_d)
print("="*80)

e = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
new_e = e.reshape(3,2,2)
print(e)
print(new_e)
print("="*80)

#copia 2x a mesma lista, alterando somente o valor informado
f = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
g = f
g[0]=19
print(f)
print(g)
print("="*80)

#cópia que faz modificação do valor informado
h = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
i = np.copy(h)
h[0]=19
print(i)
print("="*80)

a1=np.array([1,2,3])
a2=np.array([4,5,6])
r1=np.concatenate((a1,a2))
r2=np.concatenate((a1,a2))
r3=np.concatenate((a1,a1,a2,a2))
print(r1)
print(r2)
print(r3)
print("="*80)

b1 = np.array([1,2,3,4,5,6])
result1=np.split(b1,3)
print(result1)
print("="*80)

b2 = np.array([1,2,3,4,5,6])
b3 = np.append(b2,[7,8,9,10,11,12])
b3[0]=20
print(b2)
print(b3)
print("="*80)

arr=np.array([44,33,22,11,88])
element = arr[1]
print(element)
print(arr[0])
