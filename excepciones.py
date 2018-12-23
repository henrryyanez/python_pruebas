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

el_mundo_es_plano = True
if el_mundo_es_plano:
    print("¡Tené cuidado de no caerte!")
