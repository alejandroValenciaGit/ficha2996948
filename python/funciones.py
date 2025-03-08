def mostrar ():
    print("Hola mundo funciones");
mostrar();

def suma(a, b):
    return a+b;

def resta(a,b):
    return a-b;

def multiplicacion(a,b):
    return a*b;

def division(a,b):
    if b == 0:
        return "Error; No se puede dividir por cero."
    return a/b;

def exponente(a,b):
    return a**b;

def calculadora():
    while True:
        print("\n--- Calculadora en python ----")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Division")
        print("5. Exponente")
        print("6. Salir")

        opcion = input("Seleccione una opcion (1-6): ")

        if opcion == "6":
            print("Saliendo de la calculadora...")
            break

        if opcion not in ["1","2","3","4","5"]:
            print("Opcion no valida. Intente de nuevo.")
            continue

        try:
            num1 = float(input("Ingrese el primer numero: "))
            num2 = float(input("Ingrese el segundo numero: "))

            operaciones = {
                "1": suma,
                "2": resta,
                "3": multiplicacion,
                "4": division,
                "5": exponente
            }

            resultado = operaciones[opcion](num1, num2)
            print(f"Resultado: {resultado}")
        
        except ValueError:
            print("Error: Ingrese solo numeros validos.")

calculadora()

