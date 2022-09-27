def contar_letras(cadena):
    counter = 0
    for character in cadena:
        if character.isalpha():
            counter += 1
    return counter

def contar_digitos(cadena):
    counter = 0
    for character in cadena:
        if character.isdigit():
            counter += 1
    return counter

def contar_caracter(cadena, caracter):
    return cadena.count(caracter)

def main():
    #cadena = "4$$E&95KPfjT$%TJ7#6T2%tcnS#3$^"
    cadena = input("Ingrese una cadena: ")
    print("La cantidad de letras es: ", contar_letras(cadena))
    print("La cantidad de digitos es: ", contar_digitos(cadena))
    caracter = input("Ingrese el caracter a contar: ")
    print("La cantidad de caracteres es: ", contar_caracter(cadena, caracter))

main()