# Informe sobre las decisiones de dise帽o 馃搵
<hr>

## Arquitectura del sistema 鈿欙笍
El sistema al ser sencillo elegimos crear dos archivos uno donde se encuentra toda la logica
del mismo y otro archivo txt que es donde se carga el patron inicial.

#### Archivo _life.py_ 馃搫
Este es el archivo principal donde se encuentra los m茅todos aplicados en el sistema:

- `read_matrix()`: m茅todo que lee la matriz y devuelve un arrays de int.


- `check_life_dead(matrix)`: nos permite corroborar las celdas vivas y muertas.


- `check_gen(counter_gen)`: controla las generaciones que lleva el sistema
  

- `check_running_gen(matrix)`: m茅todo que nos permite que al tener las celdas muertes se cancele
la ejecuci贸n
<hr>

### Reglas del juego 馃摙
En el siguiente apartado se explicara los m茅todos que utilizamos para comprobar los vecinos y la 
supervivencia de las celdas:
- `check_neighbor(matrix, x, y)`: en este m茅todo lo que hacemos es recibir por parametro
una matriz, un valor de x y un valor de y, que nos va a permitir recorrer los 8 vecinos que va a tener
  el valor de la posici贸n (x e y) y luego devuelve el n煤mero de vecinos.
  
    Ademas se implemento la logica para que la matriz sea toroidal osea que
    no tengo final cuando se llegara a algunos de sus bordes, esta consta de sacar el m贸dulo de la division de la posici贸n
    con la cantidad de elementos _(dos veces el len de la matriz)_
  

- `survival(matrix)`: lo planteado en este es lo siguiente, se recibe la matriz por parametro se copia esta matriz a una auxiliar, luego
  de esto se recorre la matrix que se paso por parametro y en cada iteraci贸n del for se llama al m茅todo `check_neighbor(matrix, x, y)`
  obteniendo el n煤mero de vecinos, asi podemos comparar si en la **_posici贸n[x][y]_** tenemos un 1 y el n煤mero de vecinos es menor que 2 o
  mayor que 3, esa posici贸n pasa tener el valor 0, y si en la **_posici贸n[x][y]_** tenemos un valor 0 y su n煤mero de vecinos es exactamente
  3, en esa posici贸n la celda pasa a tener el valor 1, **todos estos cambios se lo hacemos a la matriz auxiliar**
  Una vez que se termina de comprobar la posici贸n devolvemos una copia de la matriz auxiliar
  
  
<hr>

Luego en la parte de ejecuci贸n se llaman a los dem谩s m茅todos, donde aplicamos un tiempo para ir mostrando la matriz y limpiando
la consola.
