import random

nPlayers = 2

def menu():
    print("\n\tBingo 75")
    print('1. Numero de jugadores (default 2)\n' +
          '2. Reglas\n' +
          '3. Jugar\n' +
          '4. Salir')
    return input('Ingrese su opción: ')

def rules():
    print('''
    El juego consiste en que cada jugador tiene un cartón y se sacan números al azar.
    Los jugador van tachando el número que sale si lo tienen en su cartón.
    El jugador gana si completa una línea o una diagonal en su cartón.
    Otra forma de ganar es que consiga las cuatro esquinas de su cartón.
    El jugador también gana si completa todo el cartón.
    ''')

def nplayers():
    global nPlayers
    nPlayers = int(input('Ingrese el número de jugadores: '))

def crearTablero():
    matriz = []
    filas = 5
    columnas = 5
    for i in range(filas):
        matriz.append(random.sample(range(1, 76), columnas))
    dim = (filas,columnas)
    return matriz, dim

def mostrarTablero(matriz, dim):
    filas, columnas = dim
    bingo = ['B', 'I', 'N', 'G', 'O']
    for letter in bingo: print(letter, end='\t')
    print()
    for i in range(filas):
        for j in range(columnas):
            print(matriz[i][j], end='\t')
        print('')
    print()

def checkBingo(matriz, numero):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == numero:
                matriz[i][j] = 'X'
    return matriz

def playBingo():
    currentB = random.choice(range(1,76))
    return currentB

def Play():
    end = False
    cartones = []
    for i in range(nPlayers):
        cartones.append(crearTablero())
        mostrarTablero(cartones[i][0], cartones[i][1])
        
    while not end:
        numero = playBingo()
        print(f"\tEl número es '{numero}'")
        for i in range(nPlayers):
            print ('Cartón del jugador', i+1)
            matriz = checkBingo(cartones[i][0], numero)
            mostrarTablero(matriz, (5,5))
            if matriz[0][0] == 'X' and matriz[0][4] == 'X' and matriz[4][0] == 'X' and matriz[4][4] == 'X':
                print(f'Jugador {i+1} Ganaste por las esquinas')
                end = True
                break
            elif matriz[0][0] == 'X' and matriz[1][1] == 'X' and matriz[2][2] == 'X' and matriz[3][3] == 'X' and matriz[4][4] == 'X':
                print(f'Jugador {i+1} Ganaste por la diagonal')
                end = True
                break
            elif matriz[0][0] == 'X' and matriz[0][1] == 'X' and matriz[0][2] == 'X' and matriz[0][3] == 'X' and matriz[0][4] == 'X':
                print(f'Jugador {i+1} Ganaste por la primera fila')
                end = True
                break
            elif matriz[1][0] == 'X' and matriz[1][1] == 'X' and matriz[1][2] == 'X' and matriz[1][3] == 'X' and matriz[1][4] == 'X':
                print(f'Jugador {i+1} Ganaste por la segunda fila')
                end = True
                break
            elif matriz[2][0] == 'X' and matriz[2][1] == 'X' and matriz[2][2] == 'X' and matriz[2][3] == 'X' and matriz[2][4] == 'X':
                print(f'Jugador {i+1} Ganaste por la tercera fila')
                end = True
                break
            elif matriz[3][0] == 'X' and matriz[3][1] == 'X' and matriz[3][2] == 'X' and matriz[3][3] == 'X' and matriz[3][4] == 'X':
                print(f'Jugador {i+1} Ganaste por la cuarta fila')
                end = True
                break
            elif matriz[4][0] == 'X' and matriz[4][1] == 'X' and matriz[4][2] == 'X' and matriz[4][3] == 'X' and matriz[4][4] == 'X':
                print(f'Jugador {i+1} Ganaste por la quinta fila')
                end = True
                break

def main():
    option = menu()
    while option != '4':
        if option == '1':
            nplayers()
        elif option == '2':
            rules()
        elif option == '3':
            Play()
        option = menu()

if __name__ == '__main__':
    main()