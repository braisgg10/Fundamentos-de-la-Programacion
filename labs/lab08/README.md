# Lab 08: Listas, Bucles `while` y Proyectos

Este laboratorio consistió en varios proyectos y archivos de ejercicios independientes, enfocados en el manejo avanzado de listas, la implementación de bucles `while`, y la creación de programas más complejos.

---

## 1. Proyecto: Juego de Adivinar Frases ("Guesser")

Este es un juego interactivo que pide al usuario adivinar palabras faltantes en una frase célebre.

* **`guesser.py` (Lógica Principal):**
    * **Propósito:** Contiene la lógica principal del juego. Implementa funciones para crear huecos (`frase_huecos`), gestionar la partida (`acertar`, `acertar_random`), generar huecos aleatorios (`lista_cambios_random`) y comprobar aciertos (`aciertos`).
    * **Mi Solución:** [Ver implementaciones](./guesser.py)

* **`quotes.py` (Módulo de Datos):**
    * **Propósito:** Un archivo simple que contiene las listas de `frases` y `autores` que el juego `guesser.py` utiliza como fuente de datos.
    * **Mi Solución:** [Ver datos](./quotes.py)

---

## 2. Ejs.py: Caja de Herramientas de Funciones

Un módulo con una gran variedad de funciones que resuelven problemas numéricos y de listas, muchas usando bucles `while`.

* **Funciones de Listas:**
    * `borrado_una(lista, a)` y `borrado_varias(lista, a_borrar)`: Para eliminar elementos de una lista.
    * `frecuencia(n, l)`: Cuenta la aparición de un elemento.
    * `hay_repetidos(lista)` y `esta_ordenada(lista)`: Funciones de comprobación de estado de listas.
* **Funciones Numéricas (Primos y Triangulares):**
    * `es_primo(a)` y `primos(a)`: Para encontrar números primos.
    * `es_triangular(n)`, `cuantos_triangulares(n)`, `triangulares(n)`: Funciones para trabajar con números triangulares.
* **Mi Solución:** [Ver implementaciones](./Ejs.py)

---

## 3. Gráficos: Dibujo de Baldosas (`lab08.py`)

* **Propósito:** Contiene las funciones `dibujar_baldosa`, `dibujar_fila` y `dibujar_suelo` para generar un suelo de N x N baldosas con un diseño gráfico alterno, usando la librería `stddraw`.
* **Mi Solución:** [Ver implementaciones](./lab08.py)

---

## 4. lab08cuest.py: Ejercicios de Cuestionario

Un archivo con más ejercicios de manipulación de listas y strings.

* **Funciones de Listas:** `sustitucion(lista, una, otra)` y `sustituir(lista, una, otra)`.
* **Funciones de Strings:** `es_vocal(c)`, `cambio_vocales(palabra, car)` y `paletot(frase, car)` (que aplica el cambio de vocales a una frase entera).
* **Mi Solución:** [Ver implementaciones](./lab08cuest.py)

---

[< Volver al índice principal](../../)