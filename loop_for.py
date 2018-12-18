#Uso de FOR

for vuelta in range(1,10):
     print("Vuelta "+str(vuelta))
     
#Usando for, practicas
print("\nOtro ejemplo.\n")

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
 print(magician.title() + ", that was a great trick!")
 print("I can't wait to see your next trick, " + magician.title() + ".\n")

 print("Thank you, everyone. That was a great magic show!")

#Usando for, practicas 2, devolviendo modo lista
numbers = list(range(1,6))
print(numbers)

#Usando for, practicas 3
print("\nOtro ejemplo 3:\n")
even_numbers = list(range(2,11,2))  #Aumenta de 2 en 2 sin pasarse de 11 en el loop
print(even_numbers)

print("\nOtro ejemplo 4:\n")

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

print("\nAplicando metodos al resutado 5:\n")

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))
