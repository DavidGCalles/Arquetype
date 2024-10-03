# Arquetipo completo de desarrollo

Este arquetipo, basado en vue y flask, se ha desarrollado para estar interconectado y con los servicios bien desacoplados. Su facilidad de despliegue y su preconfiguración ayudan a reducir los tiempos de desarrollo increiblemente.

## Para correrlo
- Clona el repositorio
- Accede a la carpeta.

```docker compose up -d```

Con esto tendrás una instancia de toda la infraestructura funcionando. Los enlaces de interes son:

http://localhost:5000/swagger Para la documentación de swagger

http://localhost:8080/ Para el front

http://localhost:8000/ Para adminer y acceso a la base de datos de manera grafica.

## Configuraciones necesarias
    1. Proveer un archivo firebase.js correcto para la autenticación en front end
    2. Configurar variables de entorno para GOOGLE_CLIENT_ID y GOOGLE_CLIENT_SECRET que serán utilizadas en la conexión con las apis en el flujo OAUTH