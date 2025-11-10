# Lab 10: Programación Orientada a Objetos (OO)

Este laboratorio representa un gran salto conceptual, pasando de la programación procedural a la **Programación Orientada a Objetos**. El trabajo se centró en diseñar e implementar `Clases` para modelar conceptos del mundo real.

El laboratorio está dividido en tres proyectos principales y un archivo de ejercicios.

---

## 1. Proyecto: Ahorcado (Versión Orientada a Objetos)

Una refactorización del juego del Ahorcado del `lab09`, esta vez usando Clases para gestionar el estado del juego.

* **`palabra_secreta.py` (La Clase Principal):**
    * **Propósito:** Define la clase `PalabraSecreta`. Este objeto es ahora el "cerebro" del juego: guarda la palabra secreta y la visible, carga palabras del fichero y contiene los métodos para comprobar aciertos (`hay_aciertos`), actualizar la palabra (`cambiar`) y verificar si se ha ganado (`esta_acertada`).
    * **Mi Solución:** [Ver la Clase](./ahorcado/palabra_secreta.py)
* **`juego_ahorcado.py` (El Ejecutable):**
    * **Propósito:** Contiene la lógica de la partida (`jugar()`). Ahora este script es mucho más limpio: crea una *instancia* del objeto `PalabraSecreta` y simplemente llama a sus métodos.
    * **Mi Solución:** [Ver el script](./ahorcado/juego_ahorcado.py)
* **`ahorcado.py` (Módulo Visual):**
    * **Propósito:** Módulo de ayuda que dibuja el estado del ahorcado en la consola (`mostrar_estado`).
    * **Mi Solución:** [Ver el script](./ahorcado/ahorcado.py)
* **`palabras.txt` (Datos):**
    * **Propósito:** El diccionario de palabras del juego.
    * **[Ver diccionario](./ahorcado/palabras.txt)**

---

## 2. Proyecto: Clases de Hora y Fecha

Este proyecto consistió en crear clases para modelar el tiempo y luego usarlas para construir aplicaciones gráficas.

* **`hora.py` (Clase `Hora`):**
    * **Propósito:** Define la clase `Hora` (hh:mm:ss). Incluye métodos para sumar (`__add__`), restar (`__sub__`), comparar (`__lt__`, `__eq__`), y convertir a/desde segundos.
    * **Mi Solución:** [Ver la Clase](./hora_fecha/hora.py)
* **`fecha.py` (Clase `Fecha`):**
    * **Propósito:** Define la clase `Fecha` (dd/mm/aa). Incluye métodos para obtener el día siguiente (`siguiente`), comparar fechas y gestionar años bisiestos.
    * **Mi Solución:** [Ver la Clase](./hora_fecha/fecha.py)
* **`reloj_digital.py` (Aplicaciones):**
    * **Propósito:** Un script que *importa* las clases `Hora` y `Fecha` y las usa con `stddraw` para crear varias aplicaciones: un reloj en tiempo real, un cronómetro, un temporizador, una alarma y un calendario.
    * **Mi Solución:** [Ver las apps](./hora_fecha/reloj_digital.py)

---

## 3. Proyecto: Clase Punto

Un proyecto para modelar un `Punto` en un plano 2D.

* **`punto.py` (Clase `Punto`):**
    * **Propósito:** Define la clase `Punto` (x, y). Incluye métodos para calcular la distancia (`distancia`) y comparar (`__eq__`).
    * **Mi Solución:** [Ver la Clase](./punto/punto.py)
* **`punto_ops.py` (Operaciones):**
    * **Propósito:** Un script que *importa* la clase `Punto` y la usa con `stddraw` para realizar operaciones gráficas: pintar puntos, dibujar rejillas, encontrar puntos medios y generar "nubes" de puntos aleatorios.
    * **Mi Solución:** [Ver las operaciones](./punto/punto_ops.py)

---

## 4. `lab10cuest.py`: Ejercicios de Clases

* **Propósito:** Un archivo con más ejercicios de diseño de clases, incluyendo:
    * `Automovil`: Una clase para modelar un coche (consumo, depósito, etc.).
    * `Tiempo`: Una clase simple (mm:ss) para practicar la sobrecarga de operadores.
    * `Fraccion`: Una clase para representar fracciones y sumarlas.
* **Mi Solución:** [Ver implementaciones](./lab10cuest.py)

---

[< Volver al índice principal](../../)