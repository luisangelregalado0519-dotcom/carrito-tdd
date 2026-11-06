# Carrito de Compras con TDD e Integración Continua

Proyecto de la **Unidad 5** de Desarrollo Basado en Pruebas (TDD), IRS-023-01.
Facilitador: Ing. Carlos Rafael Luna Vargas, MGI, MGC.

Un módulo pequeño de software (un carrito de compras) desarrollado siguiendo
**estrictamente** el ciclo de TDD **Rojo → Verde → Refactor**, con un pipeline
de **Integración Continua (GitHub Actions)** que ejecuta las pruebas de forma
automática en cada `push` y cada `pull request`.

## El módulo

`carrito.py` — clase `CarritoDeCompras`:

- Agregar productos con precio y cantidad (si se repite, suma la cantidad).
- Quitar productos y vaciar el carrito.
- Calcular el subtotal.
- Aplicar un descuento en porcentaje (de 0 a 100).
- Calcular el total con el **ITBIS de República Dominicana (18%)**.
- Validaciones: precio y cantidad deben ser mayores que cero; quitar un
  producto que no existe da error; el descuento fuera de rango da error.

## Las pruebas (se escribieron PRIMERO)

`test_carrito.py` — **13 pruebas unitarias** con pytest que cubren el
comportamiento normal y los casos de error.

Para ejecutarlas en tu computadora:

```bash
pip install -r requirements.txt
pytest -v
```

## El ciclo TDD seguido

1. **Rojo:** se escribieron las 13 pruebas antes del código. Al correrlas,
   fallaron porque el módulo todavía no existía
   (ver `evidencia_fase_roja.txt`).
2. **Verde:** se escribió el código mínimo para que pasaran.
   Resultado: **13 passed** (ver `evidencia_fase_verde.txt`).
3. **Refactor:** se limpió el código sin cambiar su comportamiento y las
   13 pruebas siguieron pasando (ver `evidencia_refactor.txt`).

## Integración Continua (GitHub Actions)

El archivo `.github/workflows/pruebas.yml` hace que, ante cada `push` o
`pull request`:

1. GitHub prepara una máquina limpia con Python 3.12.
2. Instala pytest.
3. Ejecuta **todas** las pruebas unitarias.

- Si **todas pasan**, el trabajo queda en verde ✅ y el cambio se puede integrar.
- Si **una falla**, el trabajo queda en rojo ❌, GitHub **avisa al equipo**
  (campana y correo) y, con la protección de rama activada en
  *Settings → Branches* (exigir que la revisión «Ejecutar pruebas unitarias»
  pase antes de integrar), el cambio **queda bloqueado** hasta corregirlo.

En `evidencia_prueba_fallida.txt` se ve un ejemplo real: se quitó el impuesto
del cálculo a propósito y 3 pruebas fallaron — así se ve un bloqueo.
