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
1. Para el lanzamiento debemos estar en la ruta **models-simulation/gol**
```
cd gol
```
2. Una vez adentro de este directorio se encuentra con un archivo llamado **seed.txt**, en el
cual se cargara la matrix cuadrada inicial o patron inicial está constituido por 10 celdas de largo y 
   10 celdas de alto, aunque el sistema está pensado para que reciba cualquier tamaño de matriz cuadrada. 
   Patrones conocidos:
   
   - **Nave Espacial**
      ```
      0 0 0 0 0 0 0 0 0 0 
      0 0 0 0 0 0 0 0 0 0
      0 0 0 0 0 1 0 0 0 0
      0 0 0 0 0 0 1 0 0 0
      0 0 0 0 1 1 1 0 0 0 
      0 0 0 0 0 0 0 0 0 0
      0 0 0 0 0 0 0 0 0 0
      0 0 0 0 0 0 0 0 0 0
      0 0 0 0 0 0 0 0 0 0
      0 0 0 0 0 0 0 0 0 0 
      ```
   - **Osciladores**
      ```
      0 0 0 0 1 1 0 0 0 0 
      0 0 0 1 0 0 1 0 0 0
      0 0 0 1 0 1 0 0 0 0
      0 0 1 1 0 1 0 0 0 0
      0 0 0 0 0 0 1 1 0 1 
      0 0 0 0 0 0 0 0 0 1
      0 0 0 0 0 0 1 1 1 0
      0 0 0 0 0 0 1 0 0 0
      0 0 0 0 0 0 0 0 0 0
      0 0 0 0 0 0 0 0 0 0 
      ```

3. Una vez modificado este archivo, se ejecutara el life.py mostrando las
generaciones del patron por medio de la consola
   ```
   python3 life.py
   ```

4. Si el patron elegido se genera infinitamente, debe presionar **_Ctrl + C_** para parar la
ejecución