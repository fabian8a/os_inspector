# os_inspector
Este proyecto contiene un agente(python) que permite la recoleción de información del sistema operativo en donde se ejecute el agente. Dicha información es enviada a un API que se encarga de almacenarla en bucket de S3 para su posterior uso.

## Estructura del repositorio
Este repositorio ha sido divido en  las siguientes carpetas:

•**agent**: Esta carpeta contiene el archivo agent.py que se ejecuta en cada servidor y recopila información sobre el estado del sistema, por ejemplo la información del procesador, el usuario actual, nombre y versión del sistema operativo.

•**api**: Esta carpeta contiene el archivo api.py que corre un API usando flask la cual expone dos endpoints uno para recopilar información enviada por el agente y el otro endpoint que permite obtener la información recopilada.

## Cómo ejecutar el agente
Los pasos escritos a continuacion deben realizarce en la carpeta agent.

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
### Ejecución del agente

Una vez se ha finalizado la ejecución de los requisitos ya se puede correr el agent.py 
```python
python agent.py
```
Si el proceso se ejecuto correctamente se obtiene un mensaje de **success** de lo contrario generará mensaje **error**.

### Funcionamiento interno del agent

Cuando el agente es ejecutado el codigo de python utiliza las diferentes librerarias para recopilar la información del sistema, esta información la guarda en un diccionario de python el cual es convertido a JSON posteriormente. La estructura del archivo es la siguiente.
```json
{
    "cpu": "CPU",
    "os_username": "USER",
    "os_name": "OS",
    "server_ip": "IP",
    "timestamp": "2024-06-01 12:26:24",
    "os_version": "VERSION"
}
```
Una vez recolectada esta información el agente la envia al API que se especifica las variables de entorno configuradas, si no se establece la comunicación con el API va generar error.

### Cómo ejecutar el API
El API puede ser ejcutada de dos formas: 
#### Opcion 1 Docker
Se ha hecho el build de una imagen utilizando dockerfile que se encuentra en la carpeta API, dicha imagen ha sido subida a docker hub en el siguiente repositorio **fabian8a/api_inspector:v2**, este repositorio es publico por lo cual se puede hacer pull de la imagen libremente.
Para ejecutar este container se debe tener instalado docker y la ejecucion se puede realizar utilizando el siguiente comando.
```bash
docker run -itd -p 5000:5000 fabian8a/api_inspector:v2
```

#### Opcion 2 servidor con python instalado

Esta opcion requiere que se ejecuten lo siguientes pasos en la carpeta API:
1.	Para ejecutar el agente se debe tener Python instalado, para mas detalle verifica este [link](https://www.python.org/downloads/).

2.	Instalar las dependencias que el agente requiere, para ello se puede ejecutar:
```python
pip install -r requirements.txt
```
3.  Ejecutar el api.py
```python
python api.py
```

### API Endpoints

#### /report
Este endpoint acepta dos metodos POST y GET.
##### POST
Este metodo es usado para cargar la información generada por el agente.
##### GET
Este metodo es usado para obtener la información del S3, las requests deben hacerce especificando la IP a consultar en el query.
```bash
curl http://IP_API:5000/report?ip='10.10.10.1'
```

#### /health
Este endpoint solo acepta el metodo GET.

##### GET
Este metodo se usa para validar que el API este corriendo.
```bash
curl http://IP_API:5000/health
```








