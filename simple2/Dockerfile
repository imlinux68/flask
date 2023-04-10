FROM python:alpine

RUN pip install flask

WORKDIR /app

COPY . .

EXPOSE 5001

CMD ["python", "app.py"]
