# Ejercicio 1
# Matriz de 3 x 3

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matriz)

# Funcion buscar_valor especifico
def buscar_valor(matriz,valor_buscado):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] == valor_buscado:
                return i,j
valor_buscado = 1
print(buscar_valor(matriz,valor_buscado))

# Mostramos el resultado
if valor_buscado == valor_buscado:
    print("Valor encontrado en la posición",buscar_valor(matriz,valor_buscado))
else:
    ("Valor incorrecto")