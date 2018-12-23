class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")

print("Segunda prueba")

import sys

try:
    f = open('miarchivo.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("Error OS: {0}".format(err))
except ValueError:
    print("No pude convertir el dato a un entero.")
except:
    print("Error inesperado:", sys.exc_info()[0])
    raise
