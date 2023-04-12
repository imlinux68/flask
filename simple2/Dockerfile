FROM python:alpine

RUN pip install flask

WORKDIR /app

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
