#!/usr/bin/env python
import sys

if __name__ == "__main__":
     # Inicializar un diccionario de nombres como vacío para empezar.
     # Cada clave en este diccionario será un nombre y el valor
     # será el número de veces que aparezca ese nombre.
    names = {}
     # sys.stdin es un objeto de archivo. Todas las mismas funciones que
     # se puede aplicar a un objeto de archivo se puede aplicar a sys.stdin.
    for name in sys.stdin.readlines():
     # Cada línea tendrá una nueva línea al final.
     # que debe ser eliminado.
            name = name.strip()
            if name in names:
                    names[name] += 1
            else:
                    names[name] = 1

     # Iterando sobre el diccionario,
     # imprima el nombre seguido de un espacio seguido de
     # número de veces que apareció.
    for name, count in names.iteritems():
            sys.stdout.write("%d\t%s\n" % (count, name))
