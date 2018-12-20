#Usando el IF


cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

print("\nAhora pruebo con validadores:\n")

hy = 'Audi'
hy == 'audi'
print(hy)

print("\nContinuando con IF inequality:\n")

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
 print("Hold the anchovies!")
