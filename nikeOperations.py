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
        
        # Validaciones para las opciones
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
#Explicacion:
"""
    Cuando intentas ejecutar solo con main() al final del código,
    no funcionará porque en Python las funciones deben ser definidas antes de ser llamadas. 
    Sin embargo, hay una razón más importante por la que esto no funciona correctamente.
    En Python, cuando escribes un archivo con código, este se ejecuta de arriba hacia abajo. El código:
"""
# if __name__ == "__main__":
#     menu()

menu()