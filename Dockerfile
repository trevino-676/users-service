FROM python:3.9-slim-buster
WORKDIR /usr/src/app
ENV TZ=America/Mexico_City
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]