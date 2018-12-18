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
