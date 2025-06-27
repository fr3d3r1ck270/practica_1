
from funcion import devuelve_bono,menu 

menu()

subsidio = 0
edad = 0
bono = 0
subsidio_total = 0


while True:
  try:
    opcion = int(input("Ingrese una opcion: "))
    edad = int(input("Ingrese su edad: "))
    if opcion == 1:#800.000
      subsidio = 500_000
      bono = devuelve_bono(edad)#Uso de funcion
      subsidio_total = subsidio + bono
      print(f"Recibe un subsidio de {subsidio_total}")

    elif opcion == 2:#750.000
      subsidio = 600_000
      bono = devuelve_bono(edad)#Uso de funcion
      subsidio_total = subsidio + bono
      print(f"Recibe un subsidio de {subsidio}")

    elif opcion == 3:#700.000
      subsidio = 700_000
      if edad >= 65:
        bono = 80_000
      elif edad < 65 and edad <=60:
        bono = 70_000
      elif edad < 60 and edad <= 55:
        bono = 60_000
      else:
        bono = 50_000
      print(f"Recibe un subsidio de {subsidio}")

    elif opcion == 4:#600.000:
      subsidio = 750_000
      if edad >= 65:
        bono = 80_000
      elif edad < 65 and edad <=60:
        bono = 70_000
      elif edad < 60 and edad <= 55:
        bono = 60_000
      else:
        bono = 50_000
      print(f"Recibe un subsidio de {subsidio}")

    elif opcion == 5:#500.000:
      subsidio = 800_000
      if edad >= 65:
        bono = 80_000
      elif edad < 65 and edad <=60:
        bono = 70_000
      elif edad < 60 and edad <= 55:
        bono = 60_000
      else:
        bono = 50_000
      print(f"Recibe un subsidio de {subsidio}")


    elif opcion == 6:
      print("Saliendo...")
      break
    else:
      print("Opcion no válida, intentelo nuevamente")
  except ValueError:

    print("Ingrese correctamente sus datos")
    print("Para opción solo numeros")
    print("Para edad solo numeros")