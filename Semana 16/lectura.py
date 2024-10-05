# Abrir el archivo equipos_futbol.txt en modo lectura
file = open('equipos_futbol.txt', 'r')

# Leer y mostrar cada línea del archivo
line = file.readline()
while line:
    print(line.strip())  # Mostrar la línea eliminando el salto de línea al final
    line = file.readline()

# Cerrar el archivo
file.close()
