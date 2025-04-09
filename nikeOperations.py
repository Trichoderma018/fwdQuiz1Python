

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
    else:
        print("La clave no existe")

encontrarCalve()