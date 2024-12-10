import string
import random

# Función para generar la contraseña
def generar_contrasena(longitud, eleccion):
    caracteres = ""
    if "1" in eleccion:  # Letras
        caracteres += string.ascii_letters
    if "2" in eleccion:  # Números
        caracteres += string.digits
    if "3" in eleccion:  # Caracteres especiales
        caracteres += string.punctuation

    if not caracteres:  # Si no se seleccionó ninguna opción
        print("No seleccionaste ninguna opción válida. Se usarán todos los caracteres por defecto.")
        caracteres = string.ascii_letters + string.digits + string.punctuation

    return "".join(random.choice(caracteres) for _ in range(longitud))

# Solicitar la longitud de la contraseña
longitud = int(input("Ingrese el tamaño de la contraseña: "))

# Solicitar la combinación de caracteres
print("Selecciona los tipos de caracteres (escribe los números sin importar el orden):")
print("1. Letras (mayúsculas y minúsculas)")
print("2. Números")
print("3. Caracteres especiales")
eleccion = input("Ingrese su elección (por ejemplo, '123', '12', '1', etc.): ")

# Generar y mostrar la contraseña
contrasena = generar_contrasena(longitud, eleccion)
print("La contraseña generada es: " + contrasena)
