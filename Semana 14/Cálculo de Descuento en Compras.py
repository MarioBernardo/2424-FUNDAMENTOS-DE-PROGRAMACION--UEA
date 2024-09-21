def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento


def main():
    # Compra 1
    articulo1 = "Laptop"
    precio1 = 1200
    cantidad1 = 1
    monto_total1 = precio1 * cantidad1
    descuento1 = calcular_descuento(monto_total1)
    monto_final1 = monto_total1 - descuento1

    print(f"Artículo: {articulo1}")
    print(f"Precio por unidad: ${precio1}")
    print(f"Cantidad: {cantidad1}")
    print(f"Monto Total: ${monto_total1}")
    print(f"Descuento: ${descuento1}")
    print(f"Monto Final a Pagar: ${monto_final1}")

    # Compra 2
    articulo2 = "Teléfono"
    precio2 = 800
    cantidad2 = 2
    monto_total2 = precio2 * cantidad2
    porcentaje2 = 15
    descuento2 = calcular_descuento(monto_total2, porcentaje2)
    monto_final2 = monto_total2 - descuento2

    print(f"\nArtículo: {articulo2}")
    print(f"Precio por unidad: ${precio2}")
    print(f"Cantidad: {cantidad2}")
    print(f"Monto Total: ${monto_total2}")
    print(f"Descuento: ${descuento2}")
    print(f"Monto Final a Pagar: ${monto_final2}")


if __name__ == "__main__":
    main()
