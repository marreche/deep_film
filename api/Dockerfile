FROM python:latest

ADD ./ /movie_api

WORKDIR /movie_api

RUN pip install -r requirements.txt

CMD ["python", "main.py"]
