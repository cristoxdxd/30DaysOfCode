def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a

def fibonaccisum(n):
    a = 0
    for i in range(n):
        a += fibonacci(i)
    return a

def menu():
    print("1. Sucesion de Fibonacci\n"+
          "2. n-ésimo término de la sucesión de Fibonacci\n"+
          "3. Suma de los n términos de la sucesión de Fibonacci\n"+
          "4. Salir")
    opcion = int(input("Ingrese una opcion: "))
    return opcion

def main():
    opcion = menu()
    while opcion != 4:
        if opcion == 1:
            n = int(input("Ingrese un numero: "))
            for i in range(n):
                print(fibonacci(i), end=" ")
        elif opcion == 2:
            n = int(input("Ingrese un numero: "))
            print(fibonacci(n))
        elif opcion == 3:
            n = int(input("Ingrese un numero: "))
            print(fibonaccisum(n))
        else:
            print("Ingrese una opcion valida")
        opcion = menu()

main()
    