# Pruebas unitarias del Carrito de Compras
# Metodología TDD: estas pruebas se escribieron ANTES que el código del módulo.
# Ciclo: Rojo (las pruebas fallan) -> Verde (el código las pasa) -> Refactor.
#
# Para ejecutarlas:  pytest -v

import pytest

from carrito import CarritoDeCompras


def test_carrito_nuevo_esta_vacio():
    carrito = CarritoDeCompras()
    assert carrito.esta_vacio() is True
    assert carrito.subtotal() == 0


def test_agregar_producto_suma_al_subtotal():
    carrito = CarritoDeCompras()
    carrito.agregar("Yaroa pequeña", 200)
    assert carrito.subtotal() == 200
    assert carrito.esta_vacio() is False


def test_agregar_con_cantidad_multiplica_el_precio():
    carrito = CarritoDeCompras()
    carrito.agregar("Taco", 75, cantidad=3)
    assert carrito.subtotal() == 225


def test_agregar_el_mismo_producto_aumenta_la_cantidad():
    carrito = CarritoDeCompras()
    carrito.agregar("Hamburguesa", 200)
    carrito.agregar("Hamburguesa", 200)
    assert carrito.numero_productos() == 1
    assert carrito.unidades_totales() == 2
    assert carrito.subtotal() == 400


def test_quitar_producto_lo_saca_del_subtotal():
    carrito = CarritoDeCompras()
    carrito.agregar("Hot dog", 150)
    carrito.agregar("Refresco", 50)
    carrito.quitar("Hot dog")
    assert carrito.subtotal() == 50


def test_vaciar_deja_el_carrito_en_cero():
    carrito = CarritoDeCompras()
    carrito.agregar("Picadera familiar", 700)
    carrito.vaciar()
    assert carrito.esta_vacio() is True
    assert carrito.total() == 0


def test_total_aplica_el_itbis_del_18_porciento():
    carrito = CarritoDeCompras()
    carrito.agregar("Sándwich", 100)
    # 100 + 18% de ITBIS = 118
    assert carrito.total() == pytest.approx(118.00)


def test_descuento_se_aplica_antes_del_impuesto():
    carrito = CarritoDeCompras()
    carrito.agregar("Picadera familiar", 700)
    carrito.agregar("Yaroa grande", 400)
    carrito.aplicar_descuento(10)  # subtotal 1100 -> 990 con descuento
    # 990 * 1.18 = 1168.20
    assert carrito.total() == pytest.approx(1168.20)


def test_sin_descuento_el_total_es_subtotal_mas_itbis():
    carrito = CarritoDeCompras()
    carrito.agregar("Quesadilla", 200, cantidad=2)
    # 400 * 1.18 = 472
    assert carrito.total() == pytest.approx(472.00)


def test_precio_negativo_da_error():
    carrito = CarritoDeCompras()
    with pytest.raises(ValueError):
        carrito.agregar("Taco", -75)


def test_cantidad_cero_da_error():
    carrito = CarritoDeCompras()
    with pytest.raises(ValueError):
        carrito.agregar("Taco", 75, cantidad=0)


def test_quitar_un_producto_que_no_existe_da_error():
    carrito = CarritoDeCompras()
    with pytest.raises(ValueError):
        carrito.quitar("Pizza")


def test_descuento_fuera_de_rango_da_error():
    carrito = CarritoDeCompras()
    with pytest.raises(ValueError):
        carrito.aplicar_descuento(101)
