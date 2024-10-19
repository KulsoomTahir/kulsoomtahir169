FROM python:3.12-alpine

WORKDIR /code

COPY . /code/

CMD ["python", 'main.py']
