FROM python:latest

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

CMD [ "gunicorn", "server:app", "--workers", "4" , "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8112" ]

