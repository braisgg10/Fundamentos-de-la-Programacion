# Lab 04: Manipulación de Strings (Cadenas)

El objetivo de este laboratorio fue implementar una "caja de herramientas" de funciones para trabajar y manipular cadenas de texto.

---

## 1. lab04.py: Módulo de Funciones

Este archivo contiene la implementación de todas las funciones para el manejo de strings.

* **Funciones de modificación y filtrado:**
    * `cambia_primero(palabra, objetivo, nuevo)`: Reemplaza la primera aparición de un substring.
    * `filtro(palabra)`: Limpia un string (quita espacios, puntuación y convierte a minúsculas).
* **Funciones de recorte (Slicing):**
    * `primera_mitad(palabra)`: Devuelve la primera mitad de un string.
    * `sin_inicio_fin(palabra)`: Devuelve el string sin el primer ni el último carácter.
    * `sin_inicio(p1, p2)`: Concatena dos strings, quitando el primer carácter de cada uno.
* **Funciones de generación de patrones:**
    * `cuadro(car, n)`: Repite un carácter `n` veces.
    * `linea(uno, otro, m, n)`: Crea una línea con un patrón repetido.
    * `tablero(uno, otro, m, n)`: Intenta dibujar un tablero de ajedrez.
* **Mi Solución:** [Ver implementaciones](./lab04.py)

---

## 2. lab04_test.py: Script de Pruebas

* **Enunciado:** Un script proporcionado para probar la función `cambia_primero` y verificar que su salida es correcta.
* **Mi Solución:** [Ver script de prueba](./lab04_test.py)

---

[< Volver al índice principal](../../)