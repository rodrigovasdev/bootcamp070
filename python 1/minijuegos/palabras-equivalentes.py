"""
Dada la siguiente lista con pares de palabras, debes evaluar si estas palabras 
son magicamente equivalentes, las palabras magicamente equivalentes son:
Las que utilizan exactamente las mismas vocales, sin importar cuántas veces se repitan

Finalmente debes imprimir por pantalla cuales son las palabras magicamente equivalentes
"""

palabras_pares = [
    ["camino", "limón"],  # No son mágicamente equivalentes: a, i, o / i, o
    ["murciélago", "esquilador"],  # Mismas vocales: a, e, i, o, u
    ["tigre", "grieta"],  # No son mágicamente equivalentes: i, e / i, e, a
    ["bucle", "lucha"],  # No son mágicamente equivalentes: u, e / u, a
    ["ratón", "noche"],  # No son mágicamente equivalentes: a, o / o, e
    ["perro", "gorra"],  # No son mágicamente equivalentes: e, o / o, a
    ["mesa", "serpiente"],  # No son mágicamente equivalentes: e, a / e, i
    ["llave", "valle"],  # Mismas vocales: a, e
    ["astro", "costra"],  # Mismas vocales: a, o
    ["libro", "robot"],  # No son mágicamente equivalentes: i, o / o
]
