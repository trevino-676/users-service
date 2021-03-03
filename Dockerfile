FROM python:3.9-alpine
LABEL maintainer="Luis Manuel Torres Trevino"
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]