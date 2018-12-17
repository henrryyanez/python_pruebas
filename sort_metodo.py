#Uso del metodo Sort para ordenar

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

###Orden reverso
cars.sort(reverse=True)
print(cars)

####
print('')
print("Aqui esta la lista original:")
print(cars)
print("Aqui aplicamos el metodo:")
print(sorted(cars))

#############Uso del reverse
print("Uso del reverse:")
print(cars)
cars.reverse()
print(cars)

#############Uso del len
print("Uso de len")
print(cars)
print(len(cars))
