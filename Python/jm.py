jugadores = {}  

while True:
    print("\nMENU:")
    print("1. Llenar")
    print("2. Imprimir")
    print("3. Eliminar")
    print("4. Editar")
    print("5. Salir")

    opcion = input("Seleccione una opción (1/2/3/4/5): ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del jugador: ")
        equipo = input("Ingrese el equipo del jugador: ")
        posicion = input("Ingrese la posición del jugador: ")
        edad = int(input("Ingrese la edad del jugador: "))
        jugador_id = input("Ingrese un identificador único para el jugador: ")
        
        jugadores[jugador_id] = {
            "nombre": nombre,
            "equipo": equipo,
            "posicion": posicion,
            "edad": edad
        }
        print(f"¡{nombre} ha sido agregado a la lista de jugadores!")

    elif opcion == "2":
        
        print("\nLista de jugadores:")
        for jugador_id, detalles in jugadores.items():
            print(f"ID: {jugador_id}")
            print(f"Nombre: {detalles['nombre']}")
            print(f"Equipo: {detalles['equipo']}")
            print(f"Posición: {detalles['posicion']}")
            print(f"Edad: {detalles['edad']}\n")

    elif opcion == "3":
        
        jugador_id = input("Ingrese el ID del jugador que desea eliminar: ")
        if jugador_id in jugadores:
            del jugadores[jugador_id]
            print("El jugador ha sido eliminado.")
        else:
            print("ID de jugador no encontrado.")

    elif opcion == "4":
        jugador_id = input("Ingrese el ID del jugador que desea editar: ")
        if jugador_id in jugadores:
            nombre = input("Ingrese el nuevo nombre del jugador: ")
            equipo = input("Ingrese el nuevo equipo del jugador: ")
            posicion = input("Ingrese la nueva posición del jugador: ")
            edad = int(input("Ingrese la nueva edad del jugador: "))
            
            
            jugadores[jugador_id] = {
                "nombre": nombre,
                "equipo": equipo,
                "posicion": posicion,
                "edad": edad
            }
            print("La información del jugador ha sido actualizada.")
        else:
            print("ID de jugador no encontrado.")

    elif opcion == "5":
        print("Saliendo del programa.")
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción válida (1/2/3/4/5).")
