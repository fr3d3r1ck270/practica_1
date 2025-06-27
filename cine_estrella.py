
from C_E import menu
voletos_en_total = 50
compra_total= 0

print("---cine estrella--- ")
print("bienvenido al cine estrella")
print("elija una opcion")
print("1.ver el total de los voletos\n")
print("2.comprar voletos\n")
print("3.salir\n")

opt=int(input("ingrese una opcion: "))


while True:
    try:
        if opt == 1: 
            print(f"los voletos disponibles son: {voletos_en_total}\n")
            print("si desea comprar voletos ingrese la opcion 2\n")
            menu()
            opt=int(input("ingrese una opcion: "))
        elif opt == 2:
            compra_v=int(input("cuantos voletos quiere comprar: "))
            
            compra_total = voletos_en_total - compra_v
            
            print(f"compra exitosa a comprado {compra_total} voletos\n")

            menu()
            opt=int(input("ingrese una opcion: "))
        elif opt == 3: 
            print("saliendo...")
            break
    except ValueError:
        print("opcion no valida")
        print("por favor ingrese una opcion valida (1,2,3)")