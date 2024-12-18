import random

passwords_caract = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

pedir_passwords = int(input('Ingrese la longitud de la contraseña: '))

psw = ""

for i in range(pedir_passwords):
    psw += random.choice(passwords_caract)

print(psw)