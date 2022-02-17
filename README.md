# mutant-py

## Acerca del entorno de desarrollo

Este proyecto se ha realizado bajo las siguientes condiciones:

* Sistema operativo: Arch Linux
* Versión de Python: 3.10.2
* Gestor para entornos virtuales y paquetes: `Pipenv`

## Ejecución entorno local

### Entorno virtual

Para generar o ingresar al entorno virtual que `Pipenv` provee, ejecutamos:

`pipenv shell`

A partir de este punto, todo lo haremos dentro de este entorno
virtual.

Cuando se requiera salir de este, lo haremos con:

`exit`

### Instalación de dependencias

Se ha adjuntado un fichero `requirements.txt` para aquellos que usen
`Virtualenv` o `pip` de forma nativa. En este caso se ha usado para
la gestión de entorno y paquetes `Pipenv`.

Para instalar las dependencias con `Pipenv`, usamos:

`pipenv install`

### Configuración `.env`

Para el correcto funcionamiento de este proyecto se necesita de
un fichero `.env`, en donde se contiene la configuración de la
base de datos y algunos otros detalles. En este caso por usabilidad
se ha expuesto un archivo `.env-example`, el cual es una copia
exacta de como debe quedar la configuración del `.env`.

Es decir, solo es copiar y renombrar.

Para este caso, no necesitamos configurar una base de datos local,
ya que se ha configurado una conexión hacia RDS de AWS. Pero en caso
que se requiera probar en una base de datos local, simplemente
se modifica el siguiente valor `SQLALCHEMY_DATABASE_URI` en el `.env`.

### Ejecución

Después de estar dentro del entorno virtual, ejecutamos:

`flask run`

### Endpoints

Mensaje de bienvenida -> GET: `http://localhost:5000/`

Agregar registros DNA -> POST: `http://localhost:5000/api/mutant`

Ver estadisticas -> GET: `http://localhost:5000/api/stats`

***Nota:*** _La especificación más detallada de cada endpoint,
se encontrará mas adelante._

### Unit Testing

Para correr los test unitarios, realizamos lo siguiente:

`python -m unittest`

### Code Coverage

Ejecutar en el siguiente orden:

1. Analisis de cobertura de código a través de pruebas unitarias:

`coverage run -m unittest discover`

2. Reporte de cobertura de código:

`coverage report`

## Ejecución entorno AWS

### API

La API está expuesta en el siguiente dominio:

http://mutant-balancer-402315165.us-west-2.elb.amazonaws.com

con la siguiente configuración de endpoints
___
**Bienvenida**

**Endpoint** -> `{dominio}/`

**Verbo** -> `GET`
____

**Agregar DNA**

**Endpoint** -> `{dominio}/api/mutant`

**Verbo** -> `GET`

**Headers** -> `{ Content-Type = application/json }`

**Body** ->
```
{
	"dna": ["ATGCGA", "CAGTGC", "TTATGT", "AGAATG", "CCTCTA", "ATTTTG"]
}
```
___
**Estadísticas**

**Endpoint** -> `{dominio}/api/stats`

**Verbo** -> `GET`

## Consideraciones finales
* Se hace uso de dos bases de datos en RDS, una para pruebas y
la otra para el proyecto local y en producción.
* Las configuraciones hechas en base de datos no siguen lineamientos
de seguridad básicos, como el no publicar el acceso dentro del repositorio
o usar la misma base de datos para entorno local y producción.
Pero se entiende que para efectos prácticos, es la configuración
que se requería.



_Andrés Alvarez - Ingeniero de Software - andresalvarezs10@gmail.com_
