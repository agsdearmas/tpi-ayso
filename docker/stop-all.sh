#!/bin/bash

echo "> Deteniendo y eliminando contenedores y la red de Docker..."

# Detener y eliminar los contenedores y la red
# No elimina el volumen de datos (mongo-data) por defecto, por lo que los datos persisten
docker-compose -f docker-compose.yml --env-file ../.env down

echo "> Recursos liberados."