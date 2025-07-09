albums = {
    "ALB001": ["Back in Black", "AC/DC", "Rock", 1980],
    "ALB002": ["Thriller", "Michael Jackson", "Pop", 1982],
    "ALB003": ["The Wall", "Pink Floyd", "Rock", 1979],
    "ALB004": ["A Night at the Opera", "Queen", "Rock", 1975],
    "ALB005": ["Kind of Blue", "Miles Davis", "Jazz", 1959]
}

inventario = {
    "ALB001": [12990, 5],
    "ALB002": [14990, 8],
    "ALB003": [13990, 0],
    "ALB004": [15990, 10],
    "ALB005": [9900, 0]
}


def stock_genero(genero):
    total = 0
    genero = genero.lower()
    for album_id , detalles in albums.items():
        if detalles[2].lower() == genero:
            total += inventario[album_id][1]
    print(f"el stock total para {genero} es: {total}")
    
    
def busqueda_año(año_min, año_max):
    encontrados=[]
    for album_id,detalles in albums.items():
        año = detalles[3]
        if año_min <= año <= año_max and inventario[album_id][1]> 0:
            encontrados.append(f"{detalles[1]}---{detalles[0]}")
    if encontrados:
        encontrados.sort()
        print("los albumes entre los años consultados son:", encontrados)
    else:
        print("no hay albumes en ese rango de años")
        
        
def actualizar_stock(album_id, nueva_cantidad):
    if album_id in inventario:
        inventario[album_id][1] = nueva_cantidad
        return True
    else:
        return False
    
    
def menu():
    while True:
        print("\n*** MENÚ PRINCIPAL ***")
        print("1. Stock por Género.")
        print("2. Búsqueda por Año de Lanzamiento.")
        print("3. Actualizar Cantidad de Stock.")
        print("4. Salir.")
        
        opcion = input("ingrese una opcion: ")
        
        
        if opcion == "1":
            genero=input("ingrese el genero a consultar: ")
            stock_genero(genero)
        
        elif opcion == "2":
            while True:
                try:
                    año_min=int(input("ingrese año minimo: "))
                    año_max=int(input("ingrese año maximo: "))
                    break
                except ValueError:
                    print("debe imgresar valores enteros")
                busqueda_año(año_min,año_max)
            
        elif opcion == "3":
            while True:
                album_id = input("ingrese el ID del album a actualizar: ")
                try:
                    nueva_cantidad =int(input("ingrese nueva cantidad: "))
                except ValueError:
                    print("debe ingresar un numero entero")
                    continue
                
                actualizado = actualizar_stock(album_id, nueva_cantidad)
                if actualizado :
                    print("stock actualizado")
                else:
                    print("el album no existe")
                    
                seguir = input("desea actualizar otro stock(s/n): ").lower()
                if seguir != "si":
                    break
        elif opcion == "4":
            print("saliendo...")
            break
       
menu()        
