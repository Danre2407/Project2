# FROM python:3.8-slim-buster
FROM ubuntu:22.04

# Create app directory
# WORKDIR /app

# Create a directory in the container to copy the folder into
RUN mkdir /game-store
RUN mkdir /swagger

# Copy the folder from your host machine to the container
COPY /game-store /game-store
COPY /swagger /swagger
COPY app.py app.py

# Get the files
# COPY /game-store/requeriments.txt requeriments.txt

# Install dependencies
RUN apt-get update
RUN apt-get install -y python3-pip

RUN pip3 install -r /game-store/requeriments.txt

EXPOSE 5000
#Indicamos el comando que tiene que ejecutar el contenedor
CMD ["python3" ,"-m", "flask", "run", "--host=0.0.0.0"]