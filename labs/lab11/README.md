# Lab 11: Proyectos de Programación Orientada a Objetos

Este laboratorio se centró en el diseño e implementación de Clases para resolver cuatro problemas distintos, cada uno encapsulado en su propia carpeta.

---

## 1. Proyecto: Calculadora de Fracciones (con Menú)

Este proyecto implementa una calculadora interactiva por consola para sumar, restar, etc., fracciones.

* **`fraccion.py` (La Clase):**
    * Define la clase `Fraccion`. Incluye métodos para inicializar (`__init__`), sumar (`__add__`), simplificar (`mcd`) y mostrar (`__str__`).
    * [Ver la Clase](./fraccion/fraccion.py)
* **`menu.py` (Módulo de Ayuda):**
    * Un módulo genérico que define funciones para mostrar un menú y pedir opciones al usuario.
    * [Ver el Módulo](./fraccion/menu.py)
* **`fraccion_menu.py` (El Ejecutable):**
    * El script principal. Importa las clases `Fraccion` y `menu` para crear la lógica de la calculadora.
    * [Ver el script](./fraccion/fraccion_menu.py)

---

## 2. Proyecto: Análisis de Población (Lectura de CSV)

Este proyecto introduce la lectura y procesamiento de archivos `.csv` para realizar análisis de datos.

* **`poblacion.py` (Script Principal):**
    * **Propósito:** Un script que lee el archivo `.csv`, procesa los datos de los municipios de la Comunidad de Madrid y realiza diversas operaciones de manejo
    * **Mi Solución:** [Ver implementaciones](./poblacion/poblacion.py)
* **`cam_municipios_poblacion_2022.csv` (Datos):**
    * **Propósito:** El archivo de datos `.csv` que utiliza el script `poblacion.py`.
    * **[Ver archivo CSV](./poblacion/cam_municipios_poblacion_2022.csv)**

---

## 3. Proyecto: Clases Círculo y Punto (Gráficos)

Estos dos proyectos están relacionados y modelan formas geométricas para usarlas con `stddraw`.

* **`circulo/` (Clase `Circulo`):**
    * **`circulo.py`:** Define la clase `Circulo`.
    * **`circulo_ops.py` / `circulos_pintados.py`:** Scripts que importan la clase `Circulo` para dibujarlos y realizar operaciones gráficas.
    * [Ver la Clase](./circulo/circulo.py)
    * [Ver Operaciones Gráficas](./circulo/circulo_ops.py)

* **`punto/` (Clase `Punto`):**
    * **`punto.py`:** Define la clase `Punto` (con coordenadas x, y).
    * **`punto_ops.py`:** Script con operaciones gráficas que usan la clase `Punto`.
    * [Ver la Clase](./punto/punto.py)
    * [Ver Operaciones Gráficas](./punto/punto_ops.py)

---

[< Volver al índice principal](../../)