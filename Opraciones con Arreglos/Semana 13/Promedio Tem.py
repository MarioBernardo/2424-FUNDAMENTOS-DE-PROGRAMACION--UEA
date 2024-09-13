def calcular_promedio(semana_temperaturas):
    """
    Calcula y muestra el promedio de temperaturas para cada semana.

    Args:
    semana_temperaturas (list): Una lista de diccionarios con las temperaturas de una ciudad para 4 semanas.
    """
    for j, semana in enumerate(semana_temperaturas):
        suma = 0
        num_dias = len(semana)
        for dia in semana:
            suma += dia['temp']
        promedio = suma / num_dias
        print(f"  Promedio Semana {j + 1}: {promedio:.2f}°C")


# Datos de temperaturas
temperaturas = [
    [  # Quito
        [  # Semana 1
            {"day": "Lunes", "temp": 15},
            {"day": "Martes", "temp": 16},
            {"day": "Miércoles", "temp": 15},
            {"day": "Jueves", "temp": 14},
            {"day": "Viernes", "temp": 15},
            {"day": "Sábado", "temp": 16},
            {"day": "Domingo", "temp": 17}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 16},
            {"day": "Martes", "temp": 17},
            {"day": "Miércoles", "temp": 16},
            {"day": "Jueves", "temp": 15},
            {"day": "Viernes", "temp": 14},
            {"day": "Sábado", "temp": 15},
            {"day": "Domingo", "temp": 16}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 14},
            {"day": "Martes", "temp": 15},
            {"day": "Miércoles", "temp": 14},
            {"day": "Jueves", "temp": 15},
            {"day": "Viernes", "temp": 16},
            {"day": "Sábado", "temp": 15},
            {"day": "Domingo", "temp": 14}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 15},
            {"day": "Martes", "temp": 16},
            {"day": "Miércoles", "temp": 15},
            {"day": "Jueves", "temp": 14},
            {"day": "Viernes", "temp": 16},
            {"day": "Sábado", "temp": 17},
            {"day": "Domingo", "temp": 18}
        ]
    ],
    [  # Guayaquil
        [  # Semana 1
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 31},
            {"day": "Miércoles", "temp": 32},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 30},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 30}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 32},
            {"day": "Martes", "temp": 33},
            {"day": "Miércoles", "temp": 34},
            {"day": "Jueves", "temp": 33},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 31},
            {"day": "Domingo", "temp": 32}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 33},
            {"day": "Martes", "temp": 34},
            {"day": "Miércoles", "temp": 35},
            {"day": "Jueves", "temp": 36},
            {"day": "Viernes", "temp": 35},
            {"day": "Sábado", "temp": 34},
            {"day": "Domingo", "temp": 33}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 34},
            {"day": "Martes", "temp": 35},
            {"day": "Miércoles", "temp": 36},
            {"day": "Jueves", "temp": 37},
            {"day": "Viernes", "temp": 38},
            {"day": "Sábado", "temp": 37},
            {"day": "Domingo", "temp": 36}
        ]
    ],
    [  # Cuenca
        [  # Semana 1
            {"day": "Lunes", "temp": 12},
            {"day": "Martes", "temp": 13},
            {"day": "Miércoles", "temp": 12},
            {"day": "Jueves", "temp": 11},
            {"day": "Viernes", "temp": 12},
            {"day": "Sábado", "temp": 13},
            {"day": "Domingo", "temp": 14}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 13},
            {"day": "Martes", "temp": 14},
            {"day": "Miércoles", "temp": 15},
            {"day": "Jueves", "temp": 14},
            {"day": "Viernes", "temp": 13},
            {"day": "Sábado", "temp": 14},
            {"day": "Domingo", "temp": 13}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 12},
            {"day": "Martes", "temp": 13},
            {"day": "Miércoles", "temp": 14},
            {"day": "Jueves", "temp": 15},
            {"day": "Viernes", "temp": 14},
            {"day": "Sábado", "temp": 13},
            {"day": "Domingo", "temp": 12}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 13},
            {"day": "Martes", "temp": 14},
            {"day": "Miércoles", "temp": 15},
            {"day": "Jueves", "temp": 16},
            {"day": "Viernes", "temp": 15},
            {"day": "Sábado", "temp": 14},
            {"day": "Domingo", "temp": 13}
        ]
    ]
]


def mostrar_promedios():
    """
    Muestra el promedio de temperaturas para cada ciudad y semana.
    """
    nombres_ciudades = ["Quito", "Guayaquil", "Cuenca"]
    for i, ciudad in enumerate(temperaturas):
        print(f"Ciudad {nombres_ciudades[i]}:")
        calcular_promedio(ciudad)


def menu():
    """
    Muestra un menú para seleccionar la ciudad y muestra los promedios correspondientes.
    """
    while True:
        print("\nSelecciona una ciudad:")
        print("1. Quito")
        print("2. Guayaquil")
        print("3. Cuenca")
        print("4. Salir")

        opcion = input("Ingrese la opción deseada: ")
        if opcion == "1":
            print("\nTemperaturas de Quito:")
            calcular_promedio(temperaturas[0])
        elif opcion == "2":
            print("\nTemperaturas de Guayaquil:")
            calcular_promedio(temperaturas[1])
        elif opcion == "3":
            print("\nTemperaturas de Cuenca:")
            calcular_promedio(temperaturas[2])
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intente nuevamente.")


# Mostrar promedios para todas las ciudades
mostrar_promedios()

# Iniciar el menú interactivo
menu()

