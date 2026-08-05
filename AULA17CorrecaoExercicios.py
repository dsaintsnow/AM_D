#CORREÇÃO DOS EXERCÍCIOS - AULA 17 - 1 AO 4

import numpy as np

opcoes = input("Digite a opção desejada: ")

match opcoes:
    case "1":
        n_array=np.array([0,1,2,3,4,5,6,7,8,9,10,11])
        n_array=np.reshape(n_array,(3,4))
        print(n_array[1])
        print(n_array[2,3])

    case "2":
        a1=np.array([1,2,3])
        a2=np.array([4,5,6])
        a1=np.concatenate((a1,a2))
        print(a1[1:5])

    case "3":
        original=np.array([10,20,30,40,50])
        copia=np.copy(original)
        copia=np.delete(copia,[2])
        print(original)
        print(copia)

    case "4":
        new=np.array([100,200,300,400,500,600])
        a,b=np.split(new,2)
        print(new)
        print(a)
        print(b)
        b=np.append(b,[700])
        print(b)
