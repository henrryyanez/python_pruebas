#Pruebas con operadores Logicos
a = 10
b = 12
c = 13
d = 10

resultado = ((a>b) or (a<c) and ((a==c) or (a>=b)))

resultado2= ((a<b) and (b<c))

resultado3= not((a<b) and (b<c))

print(resultado)

print(resultado2)

print(resultado3)
