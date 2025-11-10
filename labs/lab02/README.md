# Lab 02: Creación de Módulos (Librerías)

El objetivo de este laboratorio fue aprender a crear un módulo (la "librería" `saludos.py`) y a importar y utilizar sus funciones desde otros scripts.

---

## 1. El Módulo `saludos.py` (La Tarea Principal)

El trabajo consistió en implementar las siguientes funciones dentro del archivo `saludos.py`:

* **`hola_multi(nombre, num)`:**
    * **Enunciado:** Crear una función que devuelva un string "hola " repetido `num` veces, seguido del `nombre` y "!".
    * **Mi Solución:** [Ver implementación](./saludos.py)
* **`hola_random(nombre)`:**
    * **Enunciado:** Crear una función que llame a `hola_multi` con el `nombre` y un número aleatorio de repeticiones (entre 1 y 6).
    * **Mi Solución:** [Ver implementación](./saludos.py)

---

## 2. Scripts de Prueba y Ejecución

Los siguientes archivos se usaron para ejecutar y probar las funciones creadas en `saludos.py`:

* **`hacer_hola_multi.py`:**
    * **Propósito:** Llama a `hola_multi()` con varios argumentos para probar su salida.
    * **[Ver script](./hacer_hola_multi.py)`**
* **`test_hola_random.py`:**
    * **Propósito:** Prueba la implementación de `hola_random()`.
    * **[Ver script](./test_hola_random.py)`**
* **`ultima_tarea.py`:**
    * **Propósito:** Script final del laboratorio que pide un nombre al usuario y comprueba una salida.
    * **[Ver script](./ultima_tarea.py)**

---

[< Volver al índice principal](../../)