## ELEMENTOS DE LA TIENDA ##

elementos = [
    {"nombre": "gpu", "precio": 100},
    {"nombre": "fuente", "precio": 75},
    {"nombre": "ram", "precio": 80},
    {"nombre": "cpu", "precio": 35},
    {"nombre": "ssd", "precio": 251},
]

## MOCHILA ##

mochila = {
    "gpu": 0,
    "fuente": 0,
    "ram": 0,
    "cpu": 0,
    "ssd": 0,
}

## CREDENCIALES DEL USUARIO ##

credenciales = {
    "usuario": "Omar123",
    "password": "123",
    "saldo": 250,
    "intentos": 3,
}

## FUNCIONES ##

def buscar_producto(nombre, elementos):
    for elemento in elementos:
        if elemento["nombre"] == nombre:
            return elemento
    return None


def comprar_elemento(producto, credenciales, mochila):
    precio = producto["precio"]
    nombre = producto["nombre"]

    if credenciales["saldo"] >= precio:
        credenciales["saldo"] -= precio
        mochila[nombre] += 1

        print(f"Has comprado {nombre}.")
        print(f"Saldo restante: {credenciales['saldo']} euros.")
        print("Contenido de la mochila:")
        for nombre, cantidad in mochila.items():
            print(f"{nombre.upper()}: {cantidad}")
    else:
        print("No tienes saldo suficiente.")
        print(f"Tu saldo es de {credenciales['saldo']} euros.")


def vender_elemento(producto, credenciales, mochila):
    nombre = producto["nombre"]

    if mochila[nombre] > 0:
        mochila[nombre] -= 1
        credenciales["saldo"] += producto["precio"]

        print(f"Has vendido {nombre}.")
        print(f"Saldo actual: {credenciales['saldo']} euros.")
    else:
        print(f"No tienes {nombre} en la mochila.")


## MENÚ PRINCIPAL ##

while True:
    print("\n--- Menú principal ---")
    print("1. Iniciar sesión")
    print("2. Cerrar programa")

    eleccion = input("Elige una opción: ")

    if eleccion == "2":
        print("Cerrando el programa...")
        break

    elif eleccion == "1":
        print("\n--- Inicio de sesión ---")
        usuario = input("Ingresa el usuario: ")
        password = input("Ingresa la contraseña: ")

        if usuario == credenciales["usuario"] and password == credenciales["password"]:
            print(f"\nBienvenido a la tienda, {usuario}.")

            while True:
                print("\n--- Opciones ---")
                print("1. Comprar un elemento")
                print("2. Vender un elemento")
                print("3. Buscar un producto")
                print("4. Cerrar sesión")

                eleccion = input("Elige una opción: ")

                if eleccion == "1":
                    print("\n--- Productos ---")
                    for elemento in elementos:
                        print(
                            f"{elemento['nombre'].upper()}: "
                            f"{elemento['precio']} euros"
                        )

                    nombre = input("¿Qué producto quieres comprar? ").lower()
                    producto = buscar_producto(nombre, elementos)

                    if producto:
                        comprar_elemento(producto, credenciales, mochila)
                    else:
                        print("Ese producto no existe.")

                elif eleccion == "2":
                    nombre = input("¿Qué producto quieres vender? ").lower()
                    producto = buscar_producto(nombre, elementos)

                    if producto:
                        vender_elemento(producto, credenciales, mochila)
                    else:
                        print("Ese producto no existe.")

                elif eleccion == "3":
                    nombre = input("¿Qué producto buscas? ").lower()
                    producto = buscar_producto(nombre, elementos)

                    if producto:
                        print(
                            f"\nProducto encontrado: {producto['nombre']}, "
                            f"precio: {producto['precio']} euros."
                        )

                        print("\n¿Qué quieres hacer?")
                        print("1. Comprar este producto")
                        print("2. Vender este producto")
                        print("3. Volver al menú")

                        opcion_producto = input("Elige una opción: ")

                        if opcion_producto == "1":
                            comprar_elemento(producto, credenciales, mochila)

                        elif opcion_producto == "2":
                            vender_elemento(producto, credenciales, mochila)

                        elif opcion_producto == "3":
                            print("Volviendo al menú...")

                        else:
                            print("Opción no válida.")
                    else:
                        print("No encontramos ese producto.")

                elif eleccion == "4":
                    print("Cerrando sesión...")
                    break

                else:
                    print("Opción no válida.")

        else:
            credenciales["intentos"] -= 1
            print("Inicio de sesión incorrecto; alguna credencial está mal.")
            print(f"Intentos restantes: {credenciales['intentos']}")

            if credenciales["intentos"] == 0:
                print("Has agotado los intentos.")
                break

    else:
        print("Opción no válida.")


## ESTE HA SIDO MI PROYECTO INICIAL QUE COMBINA MIS CONOCIMIENTOS Y ESPERO QUE OS GUSTE, ES UN PROGRAMA DE UNA TIENDA QUE COMBINA: ##

# INICIO DE SESION
# COMPRA OBJETOS
# VENTA DE OBJETOS
# BUSQUEDA DE OBEJTOS
# CERRAR SESION