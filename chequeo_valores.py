#Probando valores

banned_users = ['andrew', 'carolina', 'david']
user = input('')

if user not in banned_users:
    print(user.title() + ", puedes postear una respuesta si quieres.")
