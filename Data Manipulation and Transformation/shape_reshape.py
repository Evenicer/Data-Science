import numpy as np

arr = np.random.randint(1,10,(3,2))

print(arr)

#Para conocer el tama;o del arreglo
print(arr.shape)

#Para cambiar la estructura del array
arr = arr.reshape(1,6)
print(arr)

#Reto

array = np.random.randint(1,100,(10,10))
print("Original:")
print(array)

array2 = array.reshape(20,5)
print("New:")
print(array2)