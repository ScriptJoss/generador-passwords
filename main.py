# Importamos libreria
import random

# Guardamos todos los caracteres
passwords_caract = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

# Pedimos los caracteres
pedir_passwords = int(input('Ingrese la longitud de la contraseña: '))

# Guardamos para agregar aca los caracteres
psw = ""

# Recorre la cantidad de caracteres que el usuario puso para luego posteriormente con random.choice elegir caracteres randoms (aumentando) y al final guardandolos en "psw"
for i in range(pedir_passwords):
    psw += random.choice(passwords_caract)

# Imprimos los caracteres finales 
print(psw)