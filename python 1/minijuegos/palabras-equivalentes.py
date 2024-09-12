"""
Dada la siguiente lista con pares de palabras, debes evaluar si estas palabras 
son magicamente equivalentes, las palabras magicamente equivalentes son:
Las que utilizan exactamente las mismas vocales, sin importar cuántas veces se repitan

Finalmente debes imprimir por pantalla cuales son las palabras magicamente equivalentes
"""

palabras_pares = [
    ["camino", "limón"],  # Mismas vocales: a, i, o
    ["murciélago", "esquilador"],  # Mismas vocales: a, e, i, o, u
    ["tigre", "grieta"],  # Mismas vocales: e, i
    ["bucle", "lucha"],  # No son mágicamente equivalentes: u, e / u, a
    ["ratón", "noche"],  # Mismas vocales: o, e
    ["perro", "gorra"],  # Mismas vocales: o, e
    ["mesa", "serpiente"],  # Mismas vocales: e, a
    ["llave", "valle"],  # Mismas vocales: a, e
    ["astro", "costra"],  # Mismas vocales: a, o
    ["libro", "robot"],  # No son mágicamente equivalentes: i, o / o
]
