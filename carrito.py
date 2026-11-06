# Módulo: Carrito de Compras
# Desarrollado con TDD (Desarrollo Basado en Pruebas):
# primero se escribieron las pruebas (test_carrito.py) y luego este código.
# Después de lograr que todas las pruebas pasaran (fase verde), el código
# se limpió en la fase de refactor SIN cambiar lo que hace; las pruebas
# siguieron pasando igual, lo que confirma que el refactor fue seguro.
#
# El carrito guarda productos con su precio y cantidad, calcula el subtotal,
# aplica un descuento opcional y el ITBIS de República Dominicana (18%).


class CarritoDeCompras:
    ITBIS = 0.18  # 18% de impuesto

    def __init__(self):
        self._productos = {}  # nombre -> {"precio": ..., "cantidad": ...}
        self._descuento = 0  # porcentaje de descuento, de 0 a 100

    # ---------- operaciones del carrito ----------

    def agregar(self, nombre, precio, cantidad=1):
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")
        if nombre in self._productos:
            self._productos[nombre]["cantidad"] += cantidad
        else:
            self._productos[nombre] = {"precio": precio, "cantidad": cantidad}

    def quitar(self, nombre):
        if nombre not in self._productos:
            raise ValueError("Ese producto no está en el carrito.")
        del self._productos[nombre]

    def vaciar(self):
        self._productos.clear()
        self._descuento = 0

    def aplicar_descuento(self, porcentaje):
        if porcentaje < 0 or porcentaje > 100:
            raise ValueError("El descuento debe estar entre 0 y 100.")
        self._descuento = porcentaje

    # ---------- consultas ----------

    def esta_vacio(self):
        return len(self._productos) == 0

    def numero_productos(self):
        return len(self._productos)

    def unidades_totales(self):
        return sum(datos["cantidad"] for datos in self._productos.values())

    # ---------- cálculos ----------

    def subtotal(self):
        return sum(
            datos["precio"] * datos["cantidad"]
            for datos in self._productos.values()
        )

    def _monto_con_descuento(self):
        return self.subtotal() * (1 - self._descuento / 100)

    def total(self):
        return round(self._monto_con_descuento() * (1 + self.ITBIS), 2)
