#!/bin/bash

# Directorio base del proyecto
PROJECT_ROOT=$(dirname "$0")/..

ENV_FILE="$PROJECT_ROOT/.env"
ENV_TEMPLATE="$PROJECT_ROOT/.env-default"

# Verificar si el archivo .env existe
if [ ! -f "$ENV_FILE" ] || [ ! -s "$ENV_FILE" ]; then
    echo "Creando archivo de entorno local (.env) desde la plantilla..."
    # Copiar la plantilla al archivo de trabajo .env
    cp "$ENV_TEMPLATE" "$ENV_FILE"
    echo "Archivo (.env) creado..."
else
    echo "Archivo (.env) ya existe. Usando configuracion local..."
fi

echo "> Iniciando servicios con Docker Compose..."

# Reconstrir la imagen de la app si hay cambios en el codigo/Dockerfile
docker-compose -f docker-compose.yml --env-file "$ENV_FILE" up -d --build

echo "> Servicios iniciados. Verificando logs (Ctrl+C para salir de los logs, los contenedores seguiran activos)..."

# Mostrar logs combinados de ambos servicios, sin detiene la ejecucion del script
docker-compose -f docker-compose.yml logs -f