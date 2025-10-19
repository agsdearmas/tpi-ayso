# UTN - TPI-AySO API

Una API construida con Flask, Python y MongoDB, diseñada para operar en un entorno de desarrollo aislado utilizando Docker Compose.

## ⚙️ Datos del Proyecto

Trabajo Practico Integrador: Virtualización con Docker

Grupo: Agustín De Armas, Hugo Adrián Isaurralde.

Docente Titular: Martín Aristiaran.

Docente Tutor: Andrés Odiard.

Materia: Arquitectura y Sistemas Operativos

## ⚙️ Inicialización del Entorno (Desarrollo)

El entorno de la aplicación y la base de datos se inicia con un único script que automatiza el proceso de build y configuración.

### 1. Clonar el Repositorio

git clone https://github.com/agsdearmas/tpi-ayso/

cd tpi-ayso

### 2. Configurar Variables de Entorno

Creá el archivo **`.env`** en la raíz del proyecto (`tpi-ayso/`) con las credenciales y configuraciones de la DB.

```ini
# .env

# --- CONFIGURACION DE LA APLICACION ---
ENV_DEFAULT=default
APP_SECRET_KEY=TU_CLAVE_SECRETA_UNICA

# --- CONFIGURACION DE MONGODB ---
DB_DEFAULT_HOST=mongo           # Nombre del servicio en docker-compose
DB_DEFAULT_PORT=27017
DB_DEFAULT_NAME=mongo_db
DB_DEFAULT_USER=mongo_admin
DB_DEFAULT_PASSWORD=password
```

### 3. Levantar Servicios

Ejecutá el script de inicio. Este comando construirá las imágenes, creará la red de Docker e iniciará la DB y la API.

./docker/run-all.sh

El proceso finalizará mostrando los logs en tiempo real de ambos contenedores.

💡 Nota: Si la terminal muestra el mensaje Running on http://0.0.0.0:5000/, la aplicación está lista. La DB y la API están corriendo en contenedores aislados.

🩺 Endpoints Clave
| Recurso            | Método | URL de Acceso Local                     | Descripción                                              |
|--------------------|--------|-----------------------------------------|----------------------------------------------------------|
| Health Check       | GET    | http://localhost:5000/healthcheck/mongo | Verifica el estado del servidor y la conexión a MongoDB. |
| Auth Login         | POST   | http://localhost:5000/auth/login        | Autenticación de usuario.                                |


## 🛠️ Estructura y Arquitectura

La aplicación sigue una arquitectura basada en un patrón de Servicios Modulares/Singleton en Python.

## Infraestructura (Docker Compose)

Servicio app: Contenedor de la aplicación Flask. Su Dockerfile instala dependencias y ejecuta run.py.

Servicio mongo: Contenedor de la base de datos MongoDB. Los datos son persistentes gracias al volumen mongo-data definido en docker-compose.yml.

Red Interna: Ambos contenedores se comunican a través de la red de Docker, utilizando el hostname definido en el .env como DB_DEFAULT_HOST.

## Flujo de Servicios (Patrones Python)

La inicialización de las conexiones se gestiona mediante un patrón de Inyección de Dependencias y Singleton:

BaseService: Define el contrato (init_app(app)).

MongoService (Singleton de Servicio): Es el punto de entrada para la API. Dentro de init_app(app), crea la conexión física.

MongoConnector (Singleton de Conexión):

    - Gestiona la conexión física y las reconexiones.
    - Construye la URI completa y segura (mongodb://usuario:pass@host/db?authSource=admin) utilizando las variables de app.config.

## 🛑 Comandos de Mantenimiento

Comandos desde el directorio /docker para gestionar entorno:

| Comando                             | Descripción                                                                  |
|-------------------------------------|------------------------------------------------------------------------------|
| ./docker/run-all.sh                 | Construye e inicia la DB y la aplicación en modo desarrollo.                 |
| docker-compose down                 | Detiene y elimina los contenedores y la red.                                 |
| docker-compose ps                   | Muestra el estado actual de los servicios.                                   |
| docker-compose logs --follow app    | Muestra los logs en tiempo real, útil para depurar la aplicación.            |
| docker system prune -a              | Limpieza profunda del caché de Docker (usar solo si hay problemas de build). |