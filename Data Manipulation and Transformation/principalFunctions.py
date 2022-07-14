import numpy as np

arr = np.random.randint(1,20,10)

matriz = arr.reshape(2,5)

print(matriz)

#Obtener el numero mas grande del array
print(arr.max())
print(matriz.max(0))

#Para obtener el indice del valor mas grande en el arreglo
print(arr.argmax())

#Obtener el minimo
print(arr.min(0))

#Indices
print(matriz.argmin(1))

#Para conocer la diferencia del pico mas bajo al pico mas alto
print(arr)
print(arr.ptp())

#Para especificar el percentil (Valor que esta en la mitad, Mediana)
np.percentile(arr,50)

#Ordenar los numeros de menor a mayor
arr.sort()

#Mediana
print(np.median(arr))

#Desviacion estandar
np.std(arr)

#Varianza
np.var(arr)

#Media
np.mean(arr)

#Concatenar
a = np.array([[1,2],[3,4]])
b = np.array([5,6])

#Se tienen que aumentar la dimension de b para poder concatenarlo

b = np.expand_dims(b,axis=0)

c = np.concatenate((a,b),axis=0)
print(c)

#Transpuesta de una matriz
matriz.T