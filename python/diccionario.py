# Diccionario inicial con varios datos
# Se define un diccionario donde la clave es el ID y el valor es otro diccionario con nombre y edad
registros = {
    1: {"nombre": "Ana", "edad": 25},
    2: {"nombre": "Luis", "edad": 30},
    3: {"nombre": "Carlos", "edad": 22}
}

# Funcion para consultar por nombre
def consultar(nombre):
    """
    Busca registros en el diccionario cuyo nombre coincida con el parametro dado (sin distinguir mayusculas/minusculas).
    :param nombre: Nombre a buscar
    :return: Diccionario con los registros que coinciden.
    """
    return {id_: datos for id_,datos in registros.items() if datos["nombre"].lover() == nombre.lover()}

# Funcion para ordenar el diccionario por clave
def ordenar_por_clave(clave):
    """
    Ordena el diccionario de registros segun la clave especifica (por ejemplo, "edad" o "nombre").
    :param clave: Clave por la cual ordenar.
    :return: Lista de tuplas ordenadas.
    """
    return sorted(registros.items(), key=lambda x: x[1][clave])

# Funcion para anexar un nuevo registro
def anexar_registro():
    """
    Permite al usuario ingresar un nuevo registro mediante la entrada de datos por teclado.
    """
    id_nuevo = int(input("Ingrese el ID: "))
    nombre_nuevo = input("Ingrese el nombre: ")
    edad_nueva = int(input("Ingrese la edad: "))
    registros[id_nuevo] = {"nombre": nombre_nuevo, "edad": edad_nueva}
    print("Registro agregado exitosamente.")

# Funcion para almacenar en otro diccionario los registros mayores a una edad 
def filtrar_por_edad(edad_minima):
    """
    Filtra los registros cuya edad sea mayor o igual a la edad minima especificada.
    :param edad_minima: Edad minima para filtrar.
    :return: Diccionario de registros filtrados.
    """
    return {id_: datos for id_,datos in registros.items() if datos["edad"] >= edad_minima}

# Menu interactivo para el usuario
def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Consultar por nombre")
        print("2. Ordenar registros")
        print("3. Agregar nuevo registro")
        print("4. Filtrar por edad")
        print("5. Mostrar registros")
        print("6. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre a consultar: ")
            print("Resultados:", consultar(nombre))
        elif opcion == "2":
            clave = input("Ingrese la clave de ordenamiento (nombre, edad): ")
            print("Registros ordenadods:", ordenar_por_clave(clave))
        elif opcion == "3":
            anexar_registro()
        elif opcion == "4":
            edad = int(input("Ingrese la edad minima para filtrar : "))
            print("Registros filtrados:", filtrar_por_edad(edad))
        elif opcion == "5":
            print("Lista completa de registros:", registros)
        elif opcion == "6":
            print("Saliendo del programa.")
            break
        else:
            print("Opcion no valida. Intente de nuevo.")

# Ejecutar el menu interactivo
menu()

