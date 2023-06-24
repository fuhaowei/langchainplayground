FROM python:3.8-slim-buster


#sets working directory in container
WORKDIR /app



COPY requirements.txt /app
RUN pip install -r requirements.txt

#copies new files from docker client current directory
COPY . /app


#specifies what command to run in container
CMD ["python", "/app/main.py"]