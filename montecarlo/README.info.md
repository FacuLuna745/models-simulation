# Informe sobre los algoritmos del sistema 馃搵

<hr>

El siguiente programa plantea la simulaci贸n del m茅todo Montecarlo a un serie de datos que se proporcionan por medio de
un archivo .txt

### Consigna 馃搶
La consigna de este proyecto, es que una compa帽ia de productos alimenticios necesita tomar estrategias de ventas
y uno de los datos que requiere es la estimaci贸n de visitas a su sitio web para los pr贸ximos 100 d铆as.

El sysadmin de la empresa nos informa que el servidor web que aloja el sitio es propio, y que adem谩s cuenta con una 
consola de monitoreo, desde hace 250 d铆as, que puede brindarnos informaci贸n hist贸rica de las visitas al sitio.

Se le solicita que desarrolle un software que, tomando los 250 datos 
hist贸ricos de visitas diarias al sitio web, y sabiendo que los mismos se distribuyen normalmente, permita estimar los
datos futuros para los pr贸ximos 100 d铆as.

### Metodo Montecarlo 馃摝
Este metodo nos permite calcular las medidas estadisticas de los datos historicos en base a las visitas al sitio, 
y en base a esos datos historicos, se aplicara el m茅todo de Montecarlo para generar los datos estimados de futuras 
visitas a la pagina web.
Los calculos de las medidas estadisticas se encuentran separados en distintas funciones para la facilidad de 
reutilizaci贸n de estos metodos.

En este caso queremos realizar la prediccion de las visitas que tendra el sitio web en los proximos ***100 dias***

### Pasos para realizar el m茅todo 馃搵
Lo primero que realizamos fue una lectura de los datos que se encuentran en el archivo _**datosPracticaMontecarlo.txt**_,
en base a estos datos obtenidos los ordenamos de mayor a menor y calculamos el total con la suma de cada uno de ellos.

Luego de eso calculamos la media, varianza, desvio estandar, minimos, maximos, distribuci贸n acumulada y distribuci贸n 
acumulada normalizada, para una mayor efectividad y agilizaci贸n utilizamos las funciones que incorpora **python** como 
tambien **pandas**

Una vez teniendo los valores anteriores generamos un 100 numeros entre random entre 1 y 0, para luego fijarnos cual es
el primer que este random en la lista de acumulado normalizado. Y ahi me dice que valor de x corresponde ese random.

Para cada uno de estos valores recorremos la lista de acumulados normalizados hasta encontrar el primer n潞 que supera 
al random. Este n潞 nos va a indicar que n潞 de x corresponde para ese n潞 random.

Con esto obtendremos la estimaci贸n y en base a esto calculamos nuevamente media, varianza, desvio estandar, minimos y 
maximos