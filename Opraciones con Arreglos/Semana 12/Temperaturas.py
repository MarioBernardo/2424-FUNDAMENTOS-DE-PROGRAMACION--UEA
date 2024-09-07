# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)

# Crear una matriz 3D para almacenar datos de temperaturas
temperaturas = [
    [   # Quito
        [   # Semana 1
            {"day": "Lunes", "temp": 15},
            {"day": "Martes", "temp": 16},
            {"day": "Miércoles", "temp": 15},
            {"day": "Jueves", "temp": 14},
            {"day": "Viernes", "temp": 15},
            {"day": "Sábado", "temp": 16},
            {"day": "Domingo", "temp": 17}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 16},
            {"day": "Martes", "temp": 17},
            {"day": "Miércoles", "temp": 16},
            {"day": "Jueves", "temp": 15},
            {"day": "Viernes", "temp": 14},
            {"day": "Sábado", "temp": 15},
            {"day": "Domingo", "temp": 16}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 14},
            {"day": "Martes", "temp": 15},
            {"day": "Miércoles", "temp": 14},
            {"day": "Jueves", "temp": 15},
            {"day": "Viernes", "temp": 16},
            {"day": "Sábado", "temp": 15},
            {"day": "Domingo", "temp": 14}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 15},
            {"day": "Martes", "temp": 16},
            {"day": "Miércoles", "temp": 15},
            {"day": "Jueves", "temp": 14},
            {"day": "Viernes", "temp": 16},
            {"day": "Sábado", "temp": 17},
            {"day": "Domingo", "temp": 18}
        ]
    ],
    [   # Guayaquil
        [   # Semana 1
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 31},
            {"day": "Miércoles", "temp": 32},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 30},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 30}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 32},
            {"day": "Martes", "temp": 33},
            {"day": "Miércoles", "temp": 34},
            {"day": "Jueves", "temp": 33},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 31},
            {"day": "Domingo", "temp": 32}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 33},
            {"day": "Martes", "temp": 34},
            {"day": "Miércoles", "temp": 35},
            {"day": "Jueves", "temp": 36},
            {"day": "Viernes", "temp": 35},
            {"day": "Sábado", "temp": 34},
            {"day": "Domingo", "temp": 33}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 34},
            {"day": "Martes", "temp": 35},
            {"day": "Miércoles", "temp": 36},
            {"day": "Jueves", "temp": 37},
            {"day": "Viernes", "temp": 38},
            {"day": "Sábado", "temp": 37},
            {"day": "Domingo", "temp": 36}
        ]
    ],
    [   # Cuenca
        [   # Semana 1
            {"day": "Lunes", "temp": 12},
            {"day": "Martes", "temp": 13},
            {"day": "Miércoles", "temp": 12},
            {"day": "Jueves", "temp": 11},
            {"day": "Viernes", "temp": 12},
            {"day": "Sábado", "temp": 13},
            {"day": "Domingo", "temp": 14}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 13},
            {"day": "Martes", "temp": 14},
            {"day": "Miércoles", "temp": 15},
            {"day": "Jueves", "temp": 14},
            {"day": "Viernes", "temp": 13},
            {"day": "Sábado", "temp": 14},
            {"day": "Domingo", "temp": 13}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 12},
            {"day": "Martes", "temp": 13},
            {"day": "Miércoles", "temp": 14},
            {"day": "Jueves", "temp": 15},
            {"day": "Viernes", "temp": 14},
            {"day": "Sábado", "temp": 13},
            {"day": "Domingo", "temp": 12}
        ],
        [   # Semana 4
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

# Calcular el promedio de temperaturas para cada ciudad y semana
nombres_ciudades = ["Quito", "Guayaquil", "Cuenca"]

for i, ciudad in enumerate(temperaturas):
    print(f"Ciudad {nombres_ciudades[i]}:")
    for j, semana in enumerate(ciudad):
        suma = 0
        num_dias = len(semana)
        for dia in semana:
            suma += dia['temp']
        promedio = suma / num_dias
        print(f"  Promedio Semana {j + 1}: {promedio:.2f}°C")

while True:
    print("Selecciona una cuidad")
    print("1. Quito")
    print("2. Guayaquil")
    print("3. Cuenca")
    print("4. Salir")

    opcion= input("Ingrese la opcion deseada:")
    if opcion == "1":
        cuidad = temperaturas[0]
        print(f"Cuidad: {cuidad}")
    else:
        print("No se encuentra la opcion")
    continue