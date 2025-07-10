# usaremos una imagen base oficial de python
FROM python:3.12.2

# establecer el directorio de trabajo del contenedor 
WORKDIR /app

# copiar archivo de la aplicacion al contenedor
COPY app.py .

# Comando a ejecutar a inciar el contenedor 
CMD ["python", "app.py"] 