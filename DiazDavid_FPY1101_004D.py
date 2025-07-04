productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']
}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
    'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
    'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]
}

def stock_marca(marca):
    total = 0

    for modelo, datos in productos.items():
        if datos[0].lower() == marca.lower():
            total = total + stock.get(modelo, [0, 0])[1]
    
    print(f"El stock es: {total}")

def busqueda_precio(p_min, p_max):
    disponibles = []

    for modelo, datos in stock.items():
        if p_min <= datos[0] <= p_max and datos[1] > 0:
            marca = productos[modelo][0]
            disponibles.append(f"{marca}--{modelo}")
    
    if disponibles:
        disponibles.sort()
        print(f"Los notebooks entre los precios consultas son: {disponibles}")
    
    else:
        print("No hay notebooks en ese rango de precios.")

def actualizar_precio(modelo, p):
    if modelo in stock:
        stock[modelo][0] = p
        return True
    
    else:
        return False

while True:
    print(" ___________________________")
    print("|                           |")
    print("|  *** MENU PRINCIPAL ***   |")
    print("| 1.- Stock marca.          |")
    print("| 2.- Búsqueda por precio   |")
    print("| 3.- Actualizar precio.    |")
    print("| 4.- Salir                 |")
    print("|___________________________|")
    opcion = input("Ingrese opción: ")

    if opcion == "1":
        marca = input("Ingrese la marca del notebook: ")
        stock_marca(marca)
    
    elif opcion == "2":
        while True:
            try:
                p_min = int(input("Ingrese el precio menor del rango: "))
                p_max = int(input("Ingrese el precio mayor del rango: "))

                if p_min > p_max:
                    print("El precio mínimo no puede ser mayor que el máximo.")
                
                else:
                    break

            except ValueError:
                print("Debe ingresar valores enteros!!")

        busqueda_precio(p_min, p_max)

    elif opcion == "3":
        while True:
            modelo = input("Ingrese el modelo a actualizar: ").upper()
            try:
                p = int(input("Ingrese el nuevo precio: "))

                if actualizar_precio(modelo, p):
                    print("Precio actualizado!!")
                
                else:
                    print("El modelo no existe!")
            
            except ValueError:
                print("Ingrese un precio válido!")

            nuevo = input("Desea actualizar otro precio? (s/n): ").lower()
            
            if nuevo == "n":
                break
    
    elif opcion == "4":
        print("\n*** PROGRAMA FINALIZADO ***\n")
        break