FROM python:3.11.4

RUN mkdir /1

WORKDIR /1

COPY req.txt .

RUN pip install -r req.txt

COPY . .

CMD gunicorn main:app --workers 2 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000