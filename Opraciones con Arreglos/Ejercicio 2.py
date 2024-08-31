# Ejercicio 2
# Matriz de 3 x 3
matriz = [
    [9, 2, 5],
    [4, 1, 8],
    [7, 6, 3]
]

print(matriz)

#Ordenamiento de la  fila buble_sort
def buble_sort(fila):
    #algoritmo buble_sort
    n = len(fila)
    for i in range(n):
        for j in range(n-1, i, -1):
            if fila[j] > fila[j-1]:
                fila[j], fila[j-1] = fila[j-1], fila[j]
                print(fila)
print("Matriz original")
print(matriz)
buble_sort(matriz[2])
print(matriz)
