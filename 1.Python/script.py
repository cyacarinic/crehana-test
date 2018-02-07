# -*- coding: utf-8 -*-
"""
Para el desarrollo del problema se hizo uso del algoritmo "Winding numbers"
* Ref: https://www.youtube.com/watch?v=f-DIsdvwJ7E
Se valida si el punto a evaluar (persona) intersecta alguno de los lados del
polígono, de no ser así, se toman segmentos de puntos consecutivos (vértices)
para verificar si el punto se encuentra a la derecha o izquierda del segmento
teniendo en cuenta la orientanción del mismo. Finalmente, se contabilizan los
segmentos de subida (+1) y bajada (-1) al rededor del punto, si se obtiene 0
pertenece, el punto está dentro del polígono.
"""
import sys


# Los pares ordenados se trataran como objetos
class Punto(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "{} {}".format(self.x, self.y)


def is_inside(jail_coords, position):
    # Winding number iniciado en 0
    wn = 0

    # Se tomarán los vertices de la prisión de dos en dos
    for i in range(len(jail_coords) - 1):
        v0, v1 = jail_coords[i], jail_coords[i+1]

        # Verificar si la persona está al borde de la prisión
        def on_line_x():
            if v0.x <= v1.x:
                return v0.x <= position.x and position.x <= v1.x
            return v0.x >= position.x and position.x >= v1.x

        # Verificar si la persona está a la derecha o izquierda del segmento
        # v0->v1 (Relatividad vertical)
        def left_or_right():
            fact1 = ((v1.x - v0.x) * (position.y - v0.y))
            fact2 = ((v1.y - v0.y) * (position.x - v0.x))
            return fact1 - fact2

        # Segmento de subida
        if v1.y >= position.y and position.y > v0.y:
            lor = left_or_right()
            if lor > 0:
                wn += 1
            # 0 si el punto está en el segmento
            elif lor == 0:
                return True
        # Segmento de bajada
        elif v0.y >= position.y and position.y > v1.y:
            lor = left_or_right()
            if lor < 0:
                wn -= 1
            # 0 si el punto está en el segmento
            elif lor == 0:
                return True
        # Segmento lineal
        elif v0.y == position.y and on_line_x():
            return True
    return wn != 0


if __name__ == '__main__':
    test_file = open(sys.argv[1], 'r')

    # Iteramos sobre los casos de prueba
    for test_case in test_file:
        # Separamos coordenadas de la prisión y la persona
        prision, point = test_case.split('|')
        # Capturamos las coordenadas de la prisión en un arreglo
        jail_coords = []
        for prision_point in prision.split(','):
            x, y = prision_point.split()
            jail_coords.append(Punto(int(x), int(y)))
        jail_coords.append(jail_coords[0])
        # Evaluamos la posición de la persona
        x, y = point.split()
        pt = Punto(int(x), int(y))
        print("Prisionero" if is_inside(jail_coords, pt) else "Ciudadano")

    test_file.close()
