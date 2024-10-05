# Abrir el archivo equipos_futbol.txt en modo escritura
file = open('equipos_futbol.txt', 'w')

# Escribir tres equipos de fútbol ecuatoriano en el archivo
file.write("1. Barcelona SC\n")
file.write("2. Emelec\n")
file.write("3. Liga de Quito\n")

# Cerrar el archivo
file.close()
