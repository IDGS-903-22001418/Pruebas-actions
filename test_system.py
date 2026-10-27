import pytest
from main import procesar_venta, main


def test_sistema_multiples_ventas():
    ventas = [
        (100, 10),
        (200, 20),
        (300, 50),
    ]
    resultados = [procesar_venta(precio, desc) for precio, desc in ventas]

    assert all(r["exito"] for r in resultados)
    assert len(resultados) == 3


def test_sistema_ventas_mixtas():
    ventas_exitosas = 0
    ventas_fallidas = 0

    resultado1 = procesar_venta(100, 10)
    if resultado1["exito"]:
        ventas_exitosas += 1
    else:
        ventas_fallidas += 1

    resultado2 = procesar_venta(200, 150)
    if resultado2["exito"]:
        ventas_exitosas += 1
    else:
        ventas_fallidas += 1

    assert ventas_exitosas == 1
    assert ventas_fallidas == 1


def test_sistema_procesamiento_completo():
    precio_base = 1000
    descuento = 20

    resultado = procesar_venta(precio_base, descuento)

    assert resultado["exito"] is True
    assert resultado["precio_final"] > 0
    assert isinstance(resultado["precio_final"], float)


def test_sistema_manejo_errores():
    casos_error = [
        (100, -10),
        (100, 100),
        (100, 150),
        (100, 200),
    ]

    for precio, descuento in casos_error:
        resultado = procesar_venta(precio, descuento)
        assert resultado["exito"] is False
        assert "error" in resultado


def test_main_ejecucion():
    try:
        main()
        assert True
    except Exception:
        pytest.fail("main() no debería lanzar excepciones")
