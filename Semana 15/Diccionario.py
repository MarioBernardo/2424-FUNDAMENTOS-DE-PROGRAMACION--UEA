# Crear el diccionario con información ficticia
informacion_personal = {
    "nombre": "David Bernardo",
    "edad": 30,
    "ciudad": "Quito",
    "profesion": "Ingeniero"
}

# Acceder al valor asociado con la clave "ciudad" y modificarlo
informacion_personal["ciudad"] = "Guayaquil"

# Agregar una nueva clave-valor que represente la "profesion"
informacion_personal["profesion"] = "Desarrollador de Software"

# Verificar si la clave "telefono" existe en el diccionario
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0998765432"  # Agregar número ficticio

# Eliminar la clave "edad" del diccionario
informacion_personal.pop("edad")

# Imprimir el diccionario resultante
print("Diccionario final:", informacion_personal)
