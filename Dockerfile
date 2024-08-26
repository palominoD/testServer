# Usar una imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar solo los archivos necesarios
COPY requirements.txt /app/
COPY app /app/app

# Instalar dependencias
RUN pip install -r requirements.txt

# Comando para ejecutar la aplicación Flask
CMD ["python", "app/main.py"]
