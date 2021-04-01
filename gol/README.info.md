#Informe sobre las decisiones de diseño
<hr>

##Arquitectura del sistema
El sistema al ser sencillo elegimos crear dos archivos uno donde se encuentra toda la logica
del mismo y otro archivo txt que es donde se carga el patron inicial.

#### Archivo _life.py_
Este es el archivo principal donde se encuentra los métodos aplicados en el sistema:

- `read_matrix()`: método que lee la matriz y devuelve un arrays de int.


- `check_life_dead(matrix)`: nos permite corroborar las celdas vivas y muertas.


- `check_gen(counter_gen)`: controla las generaciones que lleva el sistema
  

- `check_running_gen(matrix)`: método que nos permite que al tener las celdas muertes se cancele
la ejecución
<hr>

###Reglas del juego
En el siguiente apartado se explicara los métodos que utilizamos para comprobar los vecinos y la 
supervivencia de las celdas:
- `check_neighbor(matrix, x, y)`: en este método lo que hacemos es recibir por parametro
una matriz, un valor de x y un valor de y, que nos va a permitir recorrer los 8 vecinos que va a tener
  el valor de la posición (x e y) y luego devuelve el número de vecinos.
  
    Ademas se implemento la logica para que la matriz sea toroidal osea que
    no tengo final cuando se llegara a algunos de sus bordes, esta consta de sacar el módulo de la division de la posición
    con la cantidad de elementos _(dos veces el len de la matriz)_
  

- `survival(matrix)`: lo planteado en este es lo siguiente, se recibe la matriz por parametro se copia esta matriz a una auxiliar, luego
  de esto se recorre la matrix que se paso por parametro y en cada iteración del for se llama al método `check_neighbor(matrix, x, y)`
  obteniendo el número de vecinos, asi podemos comparar si en la **_posición[x][y]_** tenemos un 1 y el número de vecinos es menor que 2 o
  mayor que 3, esa posición pasa tener el valor 0, y si en la **_posición[x][y]_** tenemos un valor 0 y su número de vecinos es exactamente
  3, en esa posición la celda pasa a tener el valor 1, **todos estos cambios se lo hacemos a la matriz auxiliar**
  Una vez que se termina de comprobar la posición devolvemos una copia de la matriz auxiliar
  <hr>

Luego en la parte de ejecución se llaman a los demás métodos, donde aplicamos un tiempo para ir mostrando la matriz y limpiando
la consola.
