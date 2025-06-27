from def_calculadora_ import menu 

menu()

opcion=int(input("ingrese una opcion: "))

while True:
    try:
        if opcion == 1:
            print("sumando")
            
            num1 = int(input("ingrese el primer numero: "))
            num2 = int(input("ingrese el segundo numero: "))
            
            resultado = num1 + num2
            
            print(f"el resultado de la suma es: {resultado}")
            
            menu()
            
            opcion=int(input("ingrese una opcion: "))   
        elif opcion ==2:
            print("restando")
            
            num1 = int(input("ingrese el primer numero: "))
            num2 = int(input("ingrese el segundo numero: "))
            
            resultado = num1 - num2
            
            print(f"el resultado de la resta es: {resultado}")
            
            menu()
            
            opcion=int(input("ingrese una opcion: "))     
        elif opcion ==3:
            print("multiplicando")
            
            num1 = int(input("ingrese el primer numero: "))
            num2 = int(input("ingrese el segundo numero: "))
            
            resultado = num1 * num2
            
            print(f"el resultado de la multiplicacion es: {resultado}")
            
            menu()
            
            opcion=int(input("ingrese una opcion: "))   
        elif opcion ==4:
            print("dividiendo")
            
            num1 = int(input("ingrese el primer numero: "))
            num2 = int(input("ingrese el segundo numero: "))
            
            resultado = num1 // num2
            
            print(f"el resultado de la divicion es: {resultado}")
    except ZeroDivisionError:
        while num2 == 0:
            print("no se puede dividir por cero")
            num2 = int(input("ingrese el segundo numero: "))
                    
            
            menu()
            
            opcion=int(input("ingrese una opcion: "))
        
        else:
            print("opcion no valida")
            print("saliendo...")
            break
            