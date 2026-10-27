import pytest
from main import procesar_venta


def test_procesar_venta_exitosa():
    resultado = procesar_venta(100, 10)
    assert resultado["exito"] is True
    assert resultado["precio_final"] == pytest.approx(104.4)


def test_procesar_venta_sin_descuento():
    resultado = procesar_venta(500, 0)
    assert resultado["exito"] is True
    assert resultado["precio_final"] == pytest.approx(580.0)


def test_procesar_venta_descuento_maximo():
    resultado = procesar_venta(200, 99)
    assert resultado["exito"] is True
    assert resultado["precio_final"] == pytest.approx(2.32)


def test_procesar_venta_excepcion_descuento_negativo():
    resultado = procesar_venta(100, -5)
    assert resultado["exito"] is False
    assert "error" in resultado
    assert "entre 0 y 100" in resultado["error"]


def test_procesar_venta_excepcion_descuento_mayor_100():
    resultado = procesar_venta(100, 150)
    assert resultado["exito"] is False
    assert "error" in resultado
