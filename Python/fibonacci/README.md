En matemáticas, la sucesión o serie de Fibonacci es la siguiente sucesión infinita de números naturales: 

1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597...

La sucesión comienza con los números 0 y 1; a partir de estos, cada término es la suma de los dos anteriores, es la relación de recurrencia que la define.

1.	Programa un bloque o función que retorne los n términos de la sucesión de Fibonacci.  
_La resolución de esta parte se aborda más adelante_  

2.	Programa un bloque o función que retorne el n-ésimo término de la sucesión de Fibonacci.  
```python
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a 
```
_En esta función se usa la definición de la sucesión de manera iterativa para el número que se busca (n-ésimo)_  

3.	Programa un bloque o función que retorne la suma de los n términos de la sucesión de Fibonacci.
```python
def fibonaccisum(n):
    a = 0
    for i in range(n):
        a += fibonacci(i)
    return a
```
_En esta función se llama a la anterior para sumar cada valor de la sucesión hasta n y almacenarlo en una variable_

Finalmente, al ser llamadas las funciones por casos en el primero (la sucesión completa hasta un n) se llama a la función `fibonacci` dentro de un loop

```python
if opcion == 1:
    n = int(input("Ingrese un numero: "))
    for i in range(n):
        print(fibonacci(i), end=" ")
```
El código completo lo pueden ver aqui: [Fibonacci Python](./fibonacci.py)