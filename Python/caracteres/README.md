# Day 2 - String Counter

Las dos primeras funciones son bastante similares y lo único que cambia es el tipo de dato que se está evaluando  

```python
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
```
Como podemos ver la función interna que se llama es `.isalpha` (para letras) y `.isdigit` (para dígitos) respectivamente.

Para la última función se pide al usuario un caracter para contar cuantas veces se encuentra en la cadena  
```python
def contar_caracter(cadena, caracter):
    return cadena.count(caracter)
```

El código completo lo pueden ver aqui: [String Counter Python](./cadena.py)