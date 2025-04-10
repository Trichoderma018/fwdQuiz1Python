

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

actualizarValor()
#eliminarValor()
#print(datos)