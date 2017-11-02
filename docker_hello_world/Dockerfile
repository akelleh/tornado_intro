
FROM python:3.6.2

WORKDIR /app

ADD . /app

EXPOSE 7777

RUN pip install -r /app/requirements.txt

CMD ["python", "/app/hello_world.py"]
