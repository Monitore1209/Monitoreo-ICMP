Monitorear direcciones IP mediante solicitudes ICMP (ping) por medio de consultas.
Se proporciona una aplicación web mediante Flask para ver los estados de las direcciones IP y el historial de encuestas.
La encuesta se ejecuta como un servicio como parte de la aplicación web.
Se utiliza una base de datos SQLite para almacenar hosts, resultados de encuestas, cuentas de usuario, etc.

**Configuración**

Los siguientes ajustes deberán realizarse para la configuración:

```Instalar Python```

1.- Python 3.0+ debe estar instalado

```Instalar el repositorio```

2.- git clone https://github.com/Monitore1209/Monitoreo.git 

```Instalar los requisitos de Python```

3.- Desde el directorio principal de este repositorio, ejecute el siguiente comando:

pip install -r requirements.txt

 ```Configuración```

4.-Siga las instrucciones a continuación para ejecutar el servidor web y navegar hacia el servidor una vez que esté en funcionamiento. Será redirigido a una página de configuración para realizar la configuración inicial de la aplicación/web y de la base de datos.

****Nota:** Configurará una cuenta de administrador durante la configuración, esta cuenta deberá ser utilizada para una funcionalidad completa. De forma predeterminada, los visitantes no autenticados solo podrán ver los estados de IP.

**Ejecución del servidor web**
Para ejecutar el servidor web de la manera más básica (perezosa), puede ejecutar lo siguiente desde el directorio principal de este repositorio:

```flask run```
Si no se proporcionan argumentos, el servidor web se ejecutará en http://127.0.0.1:5000

Si desea especificar un host/puerto, puede usar los siguientes argumentos:

```flask run -h <host> -p <port>```
Para ver todos los argumentos:

```flask run --help```
Nota: Sería prudente mover esto a un servidor WSGI para su uso en producción, vea aquí.

**Migraciones de base de datos**
En caso de que cambie el esquema de la base de datos, será necesario realizar una migración. Estas migraciones se pueden encontrar en migrations/versions/
Para realizar una migración de la base de datos, detenga los servicios web y luego ejecute el siguiente comando desde el directorio principal de este repositorio:

```flask db upgrade```

