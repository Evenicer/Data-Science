import numpy as np

arr = np.random.randint(1,20,10)

matriz = arr.reshape(2,5)

print(matriz)

#Obtener el numero mas grande del array
print(arr.max())
print(matriz.max(0))

#Para obtener el indice del valor mas grande en el arreglo
print(arr.argmax())