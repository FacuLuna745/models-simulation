# Informe sobre los algoritmos del sistema 📋

<hr>

El siguiente programa plantea la simulación del método Montecarlo a un serie de datos que se proporcionan por medio de
un archivo .txt

### Consigna 📌
La consigna de este proyecto, es que una compañia de productos alimenticios necesita tomar estrategias de ventas
y uno de los datos que requiere es la estimación de visitas a su sitio web para los próximos 100 días.

El sysadmin de la empresa nos informa que el servidor web que aloja el sitio es propio, y que además cuenta con una 
consola de monitoreo, desde hace 250 días, que puede brindarnos información histórica de las visitas al sitio.

Se le solicita que desarrolle un software que, tomando los 250 datos 
históricos de visitas diarias al sitio web, y sabiendo que los mismos se distribuyen normalmente, permita estimar los
datos futuros para los próximos 100 días.

### Metodo Montecarlo 📦
Este metodo nos permite calcular las medidas estadisticas de los datos historicos en base a las visitas al sitio, 
y en base a esos datos historicos, se aplicara el método de Montecarlo para generar los datos estimados de futuras 
visitas a la pagina web.
Los calculos de las medidas estadisticas se encuentran separados en distintas funciones para la facilidad de 
reutilización de estos metodos.

En este caso queremos realizar la prediccion de las visitas que tendra el sitio web en los proximos ***100 dias***

### Pasos para realizar el método 📋
Lo primero que realizamos fue una lectura de los datos que se encuentran en el archivo _**datosPracticaMontecarlo.txt**_,
en base a estos datos obtenidos los ordenamos de mayor a menor y calculamos el total con la suma de cada uno de ellos.

Luego de eso calculamos la media, varianza, desvio estandar, minimos, maximos, distribución acumulada y distribución 
acumulada normalizada, para una mayor efectividad y agilización utilizamos las funciones que incorpora **python** como 
tambien **pandas**

Una vez teniendo los valores anteriores generamos un 100 numeros entre random entre 1 y 0, para luego fijarnos cual es
el primer que este random en la lista de acumulado normalizado. Y ahi me dice que valor de x corresponde ese random.

Para cada uno de estos valores recorremos la lista de acumulados normalizados hasta encontrar el primer nº que supera 
al random. Este nº nos va a indicar que nº de x corresponde para ese nº random.

Con esto obtendremos la estimación y en base a esto calculamos nuevamente media, varianza, desvio estandar, minimos y 
maximos