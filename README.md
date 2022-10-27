# Challenge
---
## Descripción del proyecto
Este proyecto se realiza para caso planteado, se deben desarrollar endpoints para simplificar la [API de google drive](https://developers.google.com/drive/api/guides/about-sdk). Al desplegar la API se pueden consumir los siguientes [endpoints](https://documenter.getpostman.com/view/24015996/2s84LF4c8y):
1. GET Test_Conection, este endpoint hace el test de conectividad:

Request: 
~~~
curl --location --request GET 'http://127.0.0.1:8000/test-connection'
~~~
Respuesta 200:
~~~
{
  "message": "Conecction Status OK"
}
~~~
2. GET Searchindoc, este endpoint busca en un documento una palabra que ingrese en el request

- Request con palabra no encontrada en el archivo:

~~~
curl --location --request GET 'http://127.0.0.1:8000/search-in-doc/1kN86r2UCL53oMJLpkTIbBHrsr7ETFmuP?word=libre'
~~~
Respuesta 500:
~~~
{
  "message": "No se encontro la palabra libre en el archivo con el file_id 1kN86r2UCL53oMJLpkTIbBHrsr7ETFmuP "
}
~~~

- Request busqueda exitosa de la palabra en el documento

~~~
curl --location --request GET 'http://127.0.0.1:8000/search-in-doc/1kN86r2UCL53oMJLpkTIbBHrsr7ETFmuP?word=Mercado'
~~~
Respuesta 200:
~~~
{
  "message": "Se encontro la palabra Mercado en el 1kN86r2UCL53oMJLpkTIbBHrsr7ETFmuP "
}
~~~

- Request ID no encontrado

~~~
curl --location --request GET 'http://127.0.0.1:8000/search-in-doc/LpkTIbBHrsr7ETFmuP?word=Mercado'
~~~
Respuesta 500:
~~~
{
  "message": "No existe el archivo para el ID ingresado: LpkTIbBHrsr7ETFmuP"
}
~~~

3. POST upload file, este endpoint crea un nuevo archivo en el drive y devuelve el id del documento

- Request titulo vacio

~~~
curl --location --request POST 'http://127.0.0.1:8000/file' \
--data-raw '{
    "titulo": "",
    "descripcion": "cvjfdghdfghfg"
}'
~~~
Respuesta 404:
~~~
{
  "message": "Por favor ingresa el titulo"
}
~~~

- Request titulo con caracteres especiales

~~~
curl --location --request POST 'http://127.0.0.1:8000/file' \
--data-raw '{
    "titulo": "<<<titulo>>>",
    "descripcion": "cvjfdghdfghfg"
}'
~~~
Respuesta 404:
~~~
{
  "message": "Por favor no ingresar caracteres especiales"
}
~~~

- Request descripción vacía

~~~
curl --location --request POST 'http://127.0.0.1:8000/file' \
--data-raw '{
    "titulo": "Documento Challenge",
    "descripcion": ""
}'
~~~
Respuesta 404:
~~~
{
  "message": "Por favor ingresa la descripción"
}
~~~

- Request Creación del archivo exitosa

~~~
curl --location --request POST 'http://127.0.0.1:8000/file' \
--data-raw '{
    "titulo": "Documento Challenge",
    "descripcion": "Documento con descripcion challenge :)"
}'
~~~
Respuesta 200:
~~~
{
  "id": "1mgD87O6O8iEVzpm65HDy4flPy2oefeg1",
  "titulo": "Documento Challenge",
  "descripcion”:": "Documento con descripcion challenge :)"
}
~~~

## Instalación en computador local
---
##### Requerimientos
- python 3.10
- pip3
- git

##### Pasos de instalación
1. Descargar el repositorio en su carpeta local o ejecutar la siguiente linea 

~~~
git clone https://github.com/Buca135/Challenge
~~~

2. Dentro de la carpeta se ejecuta el siguiente comando para instalar el las librerías de python.

~~~
pip freeze > requirements.txt
~~~

3. Se ejecuta el siguiente comando para  desplegar la api

~~~
uvicorn main:app
~~~
Respuesta:
~~~
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [28720]
INFO:     Started server process [28722]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
~~~
De la respuesta se obtiene el url donde está desplegada la API y se va utilizar para los request
## Docker
---
##### Requerimientos
- docker
- git


##### Pasos de instalación
1. Descargar el repositorio en su carpeta local o ejecutar la siguiente linea 

~~~
git clone https://github.com/Buca135/Challenge
~~~
2. Ejecutar el siguiente comando para crear el contenedor en docker

~~~
docker-compose build
~~~
3. Para levantar el proyecto se utiliza el siguiente comando

~~~
docker-compose up -d
~~~
4. con el siguiente comando verificamos la URL en el cual se está ejecutando la API

~~~
docker-compose ps
~~~