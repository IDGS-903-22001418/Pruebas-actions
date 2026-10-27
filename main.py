from tienda import calcular_precio, calcular_iva, validar_descuento


def procesar_venta(precio_base, descuento):
    try:
        validar_descuento(descuento)
        precio_con_descuento = calcular_precio(descuento, precio_base)
        precio_final = calcular_iva(precio_con_descuento)
        return {"exito": True, "precio_final": precio_final}
    except ValueError as e:
        return {"exito": False, "error": str(e)}


def main():
    print("=== Sistema de Tienda ===\n")

    resultado1 = procesar_venta(100, 10)
    if resultado1["exito"]:
        print(f"[TRY] Venta exitosa: ${resultado1['precio_final']:.2f}")
    else:
        print(f"[EXCEPTION] Error: {resultado1['error']}")

    resultado2 = procesar_venta(200, 25)
    if resultado2["exito"]:
        print(f"[TRY] Venta exitosa: ${resultado2['precio_final']:.2f}")
    else:
        print(f"[EXCEPTION] Error: {resultado2['error']}")

    resultado3 = procesar_venta(100, 150)
    if resultado3["exito"]:
        print(f"[TRY] Venta exitosa: ${resultado3['precio_final']:.2f}")
    else:
        print(f"[EXCEPTION] Error: {resultado3['error']}")


if __name__ == "__main__":
    main()
