# os_inspector
Este proyecto contiene un agente(python) que permite la recoleción de información del sistema operativo en donde se ejecute el agente. Dicha información es enviada a un API que se encarga de almacenarla en bucket de S3 para su posterior uso.

## Estructura del repositorio
Este repositorio ha sido divido en  las siguientes carpetas:

•**agent**: Esta carpeta contiene el archivo agent.py que se ejecuta en cada servidor y recopila información sobre el estado del sistema, por ejemplo la información del procesador, el usuario actual, nombre y versión del sistema operativo.

•**api**: Esta carpeta contiene el archivo api.py que corre un API usando flask la cual expone dos endpoints uno para recopilar información enviada por el agente y el otro endpoint que permite obtener la información recopilada.

## Como ejecutar el agente

### Requisitos

1.	Para ejecutar el agente se debe tener Python instalado, para mas detalle verifica este [link](https://www.python.org/downloads/).

2.	Instalar las dependencias que el agente requiere, para ello se puede ejecutar:
```python
pip install -r requirements.txt
```
3.  Crear las siguientes variables de entorno API_IP y API_PORT, estas variables corresponden a donde se esta ejecutando el servidor.
```bash
export API_IP= api server
export API_PORT='5000'
```








