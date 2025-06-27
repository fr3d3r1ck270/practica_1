import re


pokemones = []


def ingresar_pokemon():
    print("\nIngrese el Id de pokemon: ")
    id_pokemon = len(pokemones) + 1  
    nombre = input("Ingrese nombre de pokemon: ").lower()
    
    
    for pokemon in pokemones:
        if pokemon["nombre"] == nombre:
            print("El nombre de pokemon ya existe, ingrese otro nombre.")
            return

   
    codigo = input("Ingrese código: ")
    while not validar_codigo(codigo):
        print("El código no es válido. Debe tener al menos 8 caracteres, al menos 1 número, al menos 1 letra y no puede tener espacios.")
        codigo = input("Ingrese código: ")

    
    tipo = input("Ingrese tipo (fuego, agua, hierba, veneno, psíquico, luchador, eléctrico): ").lower()
    tipos_validos = ["fuego", "agua", "hierba", "veneno", "psiquico", "luchador", "electrico"]
    while tipo not in tipos_validos:
        print(f"El tipo debe ser uno de los siguientes: {', '.join(tipos_validos)}.")
        tipo = input("Ingrese tipo: ").lower()

    
    pokemon = {"id": id_pokemon, "nombre": nombre, "codigo": codigo, "tipo": tipo}
    pokemones.append(pokemon)
    print(f"Pokemon {nombre} ingresado con éxito!")


def validar_codigo(codigo):
    if len(codigo) < 8:
        return False
    if not re.search(r"\d", codigo):  
        return False
    if not re.search(r"[a-zA-Z]", codigo):
        return False
    if " " in codigo:  
        return False
    return True


def buscar_pokemon():
    nombre_buscar = input("\nIngrese pokemon a buscar: ").lower()
    for pokemon in pokemones:
        if pokemon["nombre"] == nombre_buscar:
            print(f"El tipo de pokemon es: {pokemon['tipo']} y su código es: {pokemon['codigo']}")
            return
    print("Pokemon no encontrado!")


def eliminar_pokemon():
    nombre_eliminar = input("\nIngrese pokemon a eliminar: ").lower()
    for pokemon in pokemones:
        if pokemon["nombre"] == nombre_eliminar:
            pokemones.remove(pokemon)
            print(f"Pokemon {nombre_eliminar} eliminado con éxito!")
            return
    print("No se pudo eliminar pokemon!")


def listar_pokemones():
    if not pokemones:
        print("\nNo hay pokemones en la lista.")
    else:
        print("\nLista de Pokemones:")
        for pokemon in pokemones:
            print(f"ID: {pokemon['id']} - Nombre: {pokemon['nombre']} - Tipo: {pokemon['tipo']}")


def menu():
    while True:
        print("\nMENU PRINCIPAL")
        print("1.- Ingresar pokemon.")
        print("2.- Buscar pokemon.")
        print("3.- Eliminar pokemon")
        print("4.- Listar pokemones")
        print("5.- Salir.")

        try:
            opcion = int(input("\nIngrese opción: "))
            if opcion == 1:
                ingresar_pokemon()
            elif opcion == 2:
                buscar_pokemon()
            elif opcion == 3:
                eliminar_pokemon()
            elif opcion == 4:
                listar_pokemones()
            elif opcion == 5:
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida, por favor ingrese una opción válida.")
        except ValueError:
            print("Debe ingresar un número válido.")

# Ejecutar el programa
if __name__ == "__main__":
    menu()