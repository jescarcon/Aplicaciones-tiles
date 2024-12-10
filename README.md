# Aplicaciones-utiles
Conjunto de aplicaciones creadas por ciertas necesidades que me fueron surgiendo, las comparto con el mundo. 

1. ------------- GENERADOR DE CONTRASEÑAS SEGURAS ------------- 
Creada para generar contraseñas seguras con ciertos parametros para que sirva para cualquier web. Vista abajo

      Ingrese el tamaño de la contraseña: 10
      Selecciona los tipos de caracteres (escribe los números sin importar el orden):
      1. Letras (mayúsculas y minúsculas)
      2. Números
      3. Caracteres especiales
      Ingrese su elección (por ejemplo, '123', '12', '1', etc.): 123
      La contraseña generada es: ^&7|fWd|N_

2. -------------  ESCANER DE PUERTOS ------------- 
Creada para escanear ciertos puertos abiertos/cerrados de una forma local y eficiente ya que usa multihilos. Vista abajo


     Bienvenido al Escáner de Puertos
    ====================================
    Tu dirección IP local es: 192.168.X.X (Ocultada por seguridad)
    Copia esta IP si necesitas usarla en el escaneo.
    
    Opciones disponibles:
    1. Escanear todos los puertos abiertos
    2. Escanear todos los puertos cerrados
    3. Escanear un rango de puertos abiertos
    4. Escanear un rango de puertos cerrados
    
    Ejemplo de la opcion 1
    
    Seleccione una opción (1-4): 1
    Ingrese la dirección IP a escanear (presione Enter para usar  192.168.X.X):  (Ocultada por seguridad)
    Escaneando puertos abiertos del 1 al 65535 en 192.168.X.X...
    Puertos encontrados: [135, 139, 445, 5040, 5432, 7680, 27036, 49664, 49665, 49666, 49667, 49668, 49669]

    Ejemplo de la opcion 3
    
    Seleccione una opción (1-4): 3
    Ingrese el puerto inicial (presione Enter para usar el puerto 1 por defecto): 136
    Ingrese el puerto final (presione Enter para usar el puerto 65535 por defecto): 
    Ingrese la dirección IP a escanear (presione Enter para usar 192.168.1.136): 
    Escaneando puertos abiertos del 136 al 65535 en 192.168.X.X... (Ocultada por seguridad)
    Puertos encontrados: [139, 445, 5040, 5432, 7680, 27036, 49665, 49667, 49666, 49668, 49669, 49664]
