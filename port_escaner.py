import socket
from threading import Thread, Lock

# Bloqueo para sincronizar la consola
lock = Lock()

# Función para obtener la IP en el rango 192.168.x.x
def obtener_ip_red_local():
    try:
        # Usa un socket para obtener la IP activa de la red local
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("192.168.1.1", 80))  # Conexión a una IP ficticia en la red local
            return s.getsockname()[0]
    except:
        return "No se pudo obtener una dirección IP válida."

# Función para escanear un puerto
def escanear_puerto(ip, puerto, solo_abiertos, resultados):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  # Tiempo de espera reducido para mayor velocidad
        resultado = sock.connect_ex((ip, puerto))
        sock.close()

        if (resultado == 0 and solo_abiertos) or (resultado != 0 and not solo_abiertos):
            with lock:
                resultados.append(puerto)
    except:
        pass

# Escaneo con multithreading
def escanear_puertos(ip, inicio, fin, solo_abiertos=True):
    print(f"Escaneando puertos {'abiertos' if solo_abiertos else 'cerrados'} del {inicio} al {fin} en {ip}...")
    resultados = []
    threads = []

    for puerto in range(inicio, fin + 1):
        hilo = Thread(target=escanear_puerto, args=(ip, puerto, solo_abiertos, resultados))
        threads.append(hilo)
        hilo.start()

    # Esperar a que todos los hilos terminen
    for hilo in threads:
        hilo.join()

    # Mostrar resultados
    if resultados:
        print(f"Puertos encontrados: {resultados}")
    else:
        print("No se encontraron puertos.")

# Menú principal
def menu():
    # Bienvenida con IP local
    print("====================================")
    print("  Bienvenido al Escáner de Puertos")
    print("====================================")
    mi_ip = obtener_ip_red_local()
    print(f"Tu dirección IP local es: {mi_ip}")
    print("Copia esta IP si necesitas usarla en el escaneo.\n")

    # Menú
    print("Opciones disponibles:")
    print("1. Escanear todos los puertos abiertos")
    print("2. Escanear todos los puertos cerrados")
    print("3. Escanear un rango de puertos abiertos")
    print("4. Escanear un rango de puertos cerrados")

    # Selección de opción
    try:
        opcion = int(input("\nSeleccione una opción (1-4): "))
    except ValueError:
        print("Opción no válida. Por favor ingrese un número entre 1 y 4.")
        return

    if opcion in [1, 2]:
        inicio, fin = 1, 65535
    elif opcion in [3, 4]:
        try:
            # Solicitar rango de puertos
            inicio = input("Ingrese el puerto inicial (presione Enter para usar el puerto 1 por defecto): ")
            fin = input("Ingrese el puerto final (presione Enter para usar el puerto 65535 por defecto): ")
            
            # Establecer valores por defecto si no se proporcionan
            if not inicio:
                inicio = 1
            else:
                inicio = int(inicio)
            
            if not fin:
                fin = 65535
            else:
                fin = int(fin)

            # Validar que los puertos sean números válidos
            if inicio < 1 or inicio > 65535 or fin < 1 or fin > 65535 or inicio > fin:
                print("Los puertos deben estar entre 1 y 65535, y el puerto inicial no puede ser mayor que el final.")
                return
        except ValueError:
            print("Por favor ingrese valores numéricos para los puertos.")
            return
    else:
        print("Opción no válida.")
        return

    # Solicitar dirección IP
    ip = input(f"Ingrese la dirección IP a escanear (presione Enter para usar {mi_ip}): ")
    if not ip:
        ip = mi_ip

    solo_abiertos = opcion in [1, 3]  # Determina si escanear abiertos o cerrados
    escanear_puertos(ip, inicio, fin, solo_abiertos)

# Iniciar el programa
menu()
