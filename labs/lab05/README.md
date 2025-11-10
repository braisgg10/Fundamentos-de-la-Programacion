# Lab 05: Lógica Condicional y Objetos

Este laboratorio se dividió en dos grandes bloques: la práctica de sentencias condicionales (`if/else`) y la manipulación de objetos de una clase (`Tiempo`).

---

## 1. lab05_ejer.py: Práctica de Condicionales

Este archivo contiene un conjunto de funciones que resuelven problemas usando lógica condicional.

* **Funciones implementadas:**
    * `es_bisiesto(a)` y `dias_febrero(a)`: Cálculo de días en febrero.
    * `coste_lapiz(lapices)` y `coste_total(lapices)`: Cálculo de precios por volumen.
    * `calculo(op1, oper, op2)`: Una calculadora simple para 4 operaciones.
    * `precio_menu(asistentes)` y `coste_totalm(asistentes)`: Cálculo de precios de menús escalado por número de asistentes.
* **Mi Solución:** [Ver implementaciones](./lab05_ejer.py)

---

## 2. Operaciones con la Clase `Tiempo`

Esta parte consistió en implementar lógica para operar con una clase `Tiempo` proporcionada.

* **`lab05.py` (Función principal):**
    * **Enunciado:** Implementar la función `suma_tiempos(t1, t2)` para sumar correctamente dos objetos `Tiempo`, manejando el desbordamiento de minutos a horas.
    * **Mi Solución:** [Ver implementación](./lab05.py)
* **`lab05_test.py` (Script de prueba):**
    * **Propósito:** Un script de *testing* para verificar que `suma_tiempos` funciona correctamente con diferentes casos.
    * **[Ver script de prueba](./lab05_test.py)**
* **`tiempo.py` (Clase base):**
    * **Propósito:** Archivo proporcionado por la cátedra que define la clase `Tiempo`.
    * **[Ver la clase](./tiempo.py)**

---

## 3. tiempo_script.py: Prueba de Asignación de Objetos

* **Propósito:** Un script para demostrar cómo funciona la asignación de objetos en Python (aliasing) en comparación con la creación de un nuevo objeto (copia).
* **[Ver script](./tiempo_script.py)**

---

[< Volver al índice principal](../../)