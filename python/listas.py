# Definimos una lista con 10 elementos
mi_lista = [34, 12, 465, 67, 23, 89, 5, 90, 56, 78]

# Funcion que realiza varias operaciones sobre la lista
def operar_listas(lista):
    # Ordenamos la lista en orden ascendente
    lista_ordenada = sorted(lista)
    print("Lista ordenada: ", lista_ordenada)

    # Extraemos un rango de la lista (del indice 2 a 6)
    sub_lista = lista_ordenada[2:7]
    print("Sublista (indices 2 al 6): ", sub_lista)

    # Creamos una nueva lista con los elementos de la sublista elevados al cuadrado
    nueva_lista = [x**2 for x in sub_lista]
    print("Nueva lista con elementos elevados al cuadrado: ", nueva_lista)

    # Modificamos las lista original reemplazando el tercer elemento por 100
    lista_modificada = lista.copy() # Creamos una copia para no afectar la original
    lista_modificada[2] = 100
    print("Lista modificada: ", lista_modificada)

    return lista_ordenada, sub_lista, nueva_lista, lista_modificada

# Llamamos a la funcion y almacenamos los resultados
ordenada, sub, nueva, modificada = operar_listas(mi_lista)

animales = ["perro", "gato", "foca", "leon", "tiburon", "colibri"]
animales1 = animales
print(animales1)

a = "Abeja"
b = "Mosca"
c = "Libelula"

miLista = [a, b, c]
print(miLista)