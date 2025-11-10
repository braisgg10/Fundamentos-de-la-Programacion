# Lab 09: Proyecto "El Ahorcado" y Funciones Numéricas

Este laboratorio consistió en dos grandes proyectos: la implementación del juego del Ahorcado y un conjunto de funciones para explorar números con propiedades especiales (triangulares, perfectos y primos).

---

## 1. Proyecto: Juego del Ahorcado

Este es un juego del Ahorcado completamente funcional que se ejecuta en la consola. El proyecto está dividido en tres archivos:

* **`juego_ahorcado.py` (Lógica Principal):**
    * **Propósito:** Contiene la lógica principal del juego (`jugar()`). Se encarga de inicializar la partida, cargar palabras, pedir letras al usuario, gestionar los fallos y aciertos, y determinar si se ha ganado o perdido.
    * **Mi Solución:** [Ver implementaciones](./juego_ahorcado.py)

* **`ahorcado.py` (Módulo Visual):**
    * **Propósito:** Un módulo de ayuda que contiene la función `mostrar_estado(fallos)`. Esta función imprime por consola el "dibujo" del ahorcado, que progresa con cada fallo.
    * **Mi Solución:** [Ver implementación](./ahorcado.py)

* **`palabras.txt` (Datos):**
    * **Propósito:** Un archivo de texto que contiene el diccionario de palabras que el juego utiliza para seleccionar la "palabra secreta" de forma aleatoria.
    * **[Ver diccionario](./palabras.txt)**

---

## 2. lab9cuest.py: Funciones Numéricas Avanzadas

Este archivo contiene una "caja de herramientas" de funciones para identificar números con propiedades matemáticas específicas, muchas de las cuales usan bucles `while`.

* **Funciones de Números Triangulares:**
    * `es_triangular(n)`, `suma_intervalo(a, b)`, `texto_triangular(n)`: Para comprobar si un número es triangular y generar una pirámide de asteriscos.
* **Funciones de Números Perfectos:**
    * `es_perfecto(n)`, `suma_divisores(n)`, `cuantos_perfectos(n)`: Para encontrar números perfectos (aquellos que son la suma de sus divisores).
* **Funciones de Números Primos:**
    * `es_primo(n)`, `cuantos_primos(n)`, `tuplas_n_primos(n)`: Para identificar números primos y contar cuántos hay hasta una potencia de 10.

* **Mi Solución (para todas las funciones):** [Ver implementaciones](./lab9cuest.py)

---

[< Volver al índice principal](../../)