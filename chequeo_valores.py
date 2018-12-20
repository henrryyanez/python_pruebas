#Probando valores

banned_users = ['andrew', 'carolina', 'david']
user = input('Ingresa tu nombre: ')

if user not in banned_users:
    print(user.title() + ", puedes postear una respuesta si quieres.")


age = input('Ingresa tu edad: ')
if age >= '18':
    print("Si tienes edad para votar!")
