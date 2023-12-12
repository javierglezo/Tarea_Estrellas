from Turtle_estrella_init import dibujar_estrella

"""
Módulo que permite personalizar tu estrella
"""

#Lista de opciones para los colores de tu estrella
def menu():
    """
    Función que muestra el menú de los colores
    """
    print("\nSelecciona el color de tu estrella:")
    print("1. Rojo")
    print("2. Amarillo")
    print("3. Verde")


#Asignación final de los parámetros de la estrella
def Tu_estrella():
    menu()
    elecol = int(input("Tu color:"))
    if elecol == 1:
        puntas = int(input("Elige las puntas de tu estrella(a partir de 5 e impar para estrella completa):"))
        tamaño = int(input("Elige tu tamaño de punta-punta de la estrella:"))
        dibujar_estrella(puntas, tamaño, "Red", 0, 0)
    if elecol == 2:
        puntas = int(input("Elige las puntas de tu estrella(a partir de 5 e impar para estrella completa):"))
        tamaño = int(input("Elige tu tamaño de punta-punta de la estrella:"))
        dibujar_estrella(puntas, tamaño, "Yellow", 0, 0)
    if elecol == 3:
        puntas = int(input("Elige las puntas de tu estrella(a partir de 5 e impar para estrella completa):"))
        tamaño = int(input("Elige tu tamaño de punta-punta de la estrella:"))
        dibujar_estrella(puntas, tamaño, "Green", 0, 0)



Tu_estrella()
