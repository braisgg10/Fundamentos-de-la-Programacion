# Lab 12: Proyecto "Rompemuros" (Juego con Matrices y OOP)

Este laboratorio es un proyecto completo que implementa el juego "Rompemuros". El objetivo fue diseñar una arquitectura de software robusta, combinando la Programación Orientada a Objetos con el manejo de matrices para la lógica del juego y la librería `stddraw` para la visualización.

El proyecto está organizado en módulos y paquetes, separando la lógica del tablero, las figuras y el motor del juego.

---

## 1. Módulos de Utilidad

* **`matrices.py` (Módulo de Matrices):**
    * **Propósito:** Una "caja de herramientas" esencial que proporciona funciones para trabajar con listas de listas (matrices), como `crear_matriz`, `n_filas`, `n_columnas` y `copia_matriz`.
    * **Mi Solución:** [Ver implementaciones](./matrices.py)

---

## 2. Paquete `parrilla` (El Tablero Visual)

* **`parrilla/parrilla.py` (Clase `Parrilla`):**
    * **Propósito:** Define la clase `Parrilla`. Este objeto es el "tablero" visual del juego. Se encarga de inicializar la ventana de `stddraw` y tiene métodos para dibujar la cuadrícula y gestionar las coordenadas (convertir de píxeles a celdas y viceversa).
    * **Mi Solución:** [Ver la Clase](./parrilla/parrilla.py)

---

## 3. Paquete `figuras` (Los Objetos del Juego)

* **`figuras/figuras.py` (Clase Base `Figura`):**
    * **Propósito:** Define la clase "madre" `Figura`. Es una clase abstracta que establece el comportamiento común de todos los objetos que pueden existir en el juego (como tener una posición y un método para dibujarse).
    * **Mi Solución:** [Ver la Clase Base](./figuras/figuras.py)

---

## 4. `rompemuros.py` (El Motor del Juego)

Este es el archivo principal que une todo.

* **Definición de Clases del Juego:**
    * Define las clases específicas del juego (`Muro`, `Diamante`, `Rompemuros`) que **heredan** de la clase `Figura`. Cada una sabe cómo dibujarse y cuál es su comportamiento.
* **Clase `Juego`:**
    * **Propósito:** Es el "director" de la orquesta. Este objeto contiene la `Parrilla`, la `matriz` lógica, la lista de todas las `figuras` y al jugador (`_rompemuros`).
    * **Lógica:** Contiene el bucle principal del juego (`jugar`), el método para procesar las teclas (`_procesar_tecla`) y el método que actualiza el estado del juego (`_actualizar`).
* **Mi Solución:** [Ver implementaciones](./rompemuros.py)

---

## 5. `rompemuros_test.py` (El Ejecutable)

* **Propósito:** Este es el script que se ejecuta para iniciar la partida. Se encarga de crear el objeto `Juego` y llamar a su método `jugar()`.
* **Mi Solución:** [Ver script](./rompemuros_test.py)

---

[< Volver al índice principal](../../)