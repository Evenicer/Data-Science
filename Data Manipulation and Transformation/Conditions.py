import numpy as np

arr = np.linspace(1,10,10, dtype='int8')

indices_cond = arr > 5

print(indices_cond)

print(arr[(arr > 5) & (arr<9)]) 

print(arr[(arr % 2 == 0)]) #Pares
print(arr[(arr % 2 != 0)]) #Impares
print(arr[(arr % 3 == 0)]) #Multiplos de 3