# Day 3 - Sorting

Para ordenar puntos por su distancia es necesario conocer esa distancia. Por lo tanto se calcula con la fórmula de distancia entre dos puntos, es decir, se elige primero un valor al azar `random.choice(points)` y después se itera con todos los demás para obtener el menor
```python
    for i in points:
        if i != x1:
            distances.append(math.sqrt(((i[0]-x1[0])**2)+((i[1]-x1[1])**2)))
        else:
            distances.append(8000)
```
Luego se repite desde la nueva posición. Finalmente se agrega el punto faltante. En este caso solo lo hice para 4 puntos.  
Para las horas se usa la función interna de ordenamiento para Python.

`byHours = sorted(hours, reverse=True)`

El código completo lo pueden ver aqui: [Sorting Python](./ordenamiento.py)