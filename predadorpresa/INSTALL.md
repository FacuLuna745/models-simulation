## Instrucciones de instalación y de lanzamiento 📖

<hr>

### Instalación 🔩

Los pasos para la instalación son:

```
git clone https://github.com/FacuLuna745/models-simulation.git
```

```
cd models-simulation
```

En caso de utilizar el paquete venv ejecutar:

```
python -m venv venv
```

```
source venv/bin/activate
```

Luego instalaremos

```
pip3 install -r requirements.txt
```

<hr>

### Lanzamiento 🚀

1. Para el lanzamiento debemos estar en la ruta **models-simulation/predadorpresa**
    ```
    cd predadorpresa
    ```
2. Una vez adentro de este directorio, encontraremos un archivo llamado **_predadorpresa.py_** , el cual ejecutaremos
   para dar inicio a la simulación
   ```
   python3 predadorpresa.py
   ```
3. Mientras se está ejecutando la simulación le va a preguntar si quiere cambiar los parametros o si desea mantener los
   que vienen por defecto. Si eligio cambiar le va a pedir los nuevos parametros y si no ya les mostrara el gráfico de
   fase y el de población.


4. En caso de que salga el siguiente error:
   `main.py:11: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.plt.show().`

   ejecutar el siguiente comando:
   ```
   sudo apt-get install python3-tk
   ```