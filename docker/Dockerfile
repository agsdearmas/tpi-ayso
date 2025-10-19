FROM python:3.10-slim

# Establecer variables de entorno que la aplicacion puede usar
ENV PYTHONUNBUFFERED=1
ENV APP_HOME=/usr/src/app

# Crear y establecer el directorio de trabajo dentro del contenedor
WORKDIR ${APP_HOME}

# Copiar solo el archivo de requisitos e instalar las dependencias.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el codigo completo de la aplicacion al contenedor
COPY . .

# Exponer el puerto por defecto de Flask
EXPOSE 5000

# Comando para ejecutar la aplicacion:
CMD [ "python", "run.py" ]