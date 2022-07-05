import numpy as np

list(range(0,10))

#Creando arrays

print(np.arange(0,10))

#Se le agrega un step para que vaya de 2 en 2
print(np.arange(0,10,2))

#Zeros para generar arrays de una dimension definida con puros 0 para definir un esquema previo
print(np.zeros(3))

#Por ejemplo una imagen con 10 x 10:
print(np.zeros((10,10)))

#Igual con 1
print(np.ones(10))

#Para generar una distribucion ordenada
print(np.linspace(0,10,10))

#Para generar una matriz con la diagonal principal en 1 y el resto en 0
print(np.eye(4))

#Generar valor aleaotorio
print(np.random.rand())

#Generar un array con valores aleatorios
print(np.random.rand(4))

#Generar estructura matricial con valores aleatorios
print(np.random.rand(4,4))

#Generar una estructura con numeros enteros aleatorios
print(np.random.randint(1,100,(10,10)))