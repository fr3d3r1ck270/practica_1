def devuelve_bono(edad):
  if edad >= 65:
    return 80_000
  elif edad < 65 and edad <=60:
    return 70_000
  elif edad < 60 and edad <= 55:
    return 60_000
  else:
    return 50_000


def menu():
   print("Programa para subsidios")
   print("Ingrese su nivel social")
   print("1. Sueldo $800.000")
   print("2. Sueldo $750.000")
   print("3. Sueldo $700.000")
   print("4. Sueldo $600.000")
   print("5. Sueldo $500.000")
   print("6. Salir")
