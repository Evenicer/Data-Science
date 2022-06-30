import numpy as np

#Dimensiones
# Scalar: dim = 0  Un solo dato o valor
# Vector: dim = 1 Listas
# Matriz: dim = 2 Hojas de calculo
# Tensor: dim = > 3  Series de tiempo o imagenes

scalar = np.array(42)
print(scalar)
scalar.ndim

vector = np.array([1,2,3])
print(vector)
print(vector.ndim)

matriz = np.array([[1,2,3],[4,5,6]])
print(matriz)
print(matriz.ndim)

tensor = np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]],[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]])
print(tensor)
print(tensor.ndim)

#Agregar o eliminar dimensiones

# Definir el numero de dimensiones
vector2 = np.array([1,2,3],ndmin=10)
print(vector2)
print(vector2.ndim)

# Agregar una dimension
expand = np.expand_dims(np.array([1,2,3]),axis=0)
print(expand)
print(expand.ndim)

# Eliminar dimensiones que no se estan ocupando
vector_2 = np.squeeze(vector2)
print(vector_2, vector_2.ndim)

