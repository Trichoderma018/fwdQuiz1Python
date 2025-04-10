#Ejercicio 1

#Diccionario

datos = {
    "producto": "Zapatillas Air Max",
    "talla": 42,
    "color": "Rojo",
    "stock": 20
}

#Funcion para encontrar la clave
def encontrarCalve():
    clave = input("Ingrese la clave: ")
    if clave in datos:
        print("Clave encontrada")
        return clave
    else:
        print("La clave no existe")
        print(datos)
        return False



def actualizarValor():
    claveEncontrada = encontrarCalve()
    if claveEncontrada != False:
        print("Actualizar productos")
        print("________________")
        datos[claveEncontrada] = input("Ingrese el nuevo valor de la clave: ")
        print("")
        print(">>>Diccionario actualizado")
        print(datos)
        print("")

def eliminarValor():
    claveEncontrada = encontrarCalve()
    if claveEncontrada != False:
        print("Para eliminar la clave")
        si = input("Presione 'y' para eliminar : ")
        if si == 'y':
            datos.pop(claveEncontrada)
            print("")
            print(">>>Diccionario actualizado")
            print(datos)
            print("")
        else:
            print("Saliendo del programa")

#actualizarValor()
#eliminarValor()

#Ejercicio 2

def mostrarMensaje():
    print("\n¡Nunca te rindas! Cada día es una nueva oportunidad.\n")

def mostrarNombres():
    nombres = ["Ana", "Juan", "María", "Carlos", "Patricia"]
    print("\nLista de nombres:")
    for nombre in nombres:
        print("- " + nombre)
    print()

def menu():
    ejecutando = True  # Bandera de salida del while

    while ejecutando:
        print("===== MENÚ PRINCIPAL =====")  # Mostrar menú
        print("1. Mostrar un mensaje")
        print("2. Mostrar una lista de nombres")
        print("3. Salir del programa")
        print("==========================")
        
        opcion = input("Seleccione una opción (1-3): ")  # Capturar la opción del usuario
        
        # Estructura if-elif en lugar de match-case
        if opcion == "1":
            mostrarMensaje()
        elif opcion == "2":
            mostrarNombres()
        elif opcion == "3":
            print("\n¡Gracias por usar el programa!\n")
            ejecutando = False
        else:  # Caso por defecto
            print("\nERROR: Invalida. Por favor, ingrese 1, 2 o 3.\n")

# Este bloque debe estar FUERA de la función menu
if __name__ == "__main__":
    menu()