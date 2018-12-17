#Uso de agregador "append"

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

#########Agregamos datos a "moto" con append###############
moto = []
moto.append('motohonda')
moto.append('motoyamaha')
moto.append('motosuzuki')
print(moto)

#########Insertando con Append en una posicion elegida######
autos = ['ford', 'chevrolet', 'fiat']
autos.insert(0, 'bronco')
print(autos)

#########Eliminando de una Lista############################
motos2 = ['honda', 'yamaha', 'suzuki']
print(motos2)
del motos2[0]
print(motos2)
#########Usando el metodo pop####################
popped_motorcycle = motorcycles.pop() 
#######Uso de Remove#########
motorcycles.remove('yamaha')
print(motorcycles)
#############################
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")
