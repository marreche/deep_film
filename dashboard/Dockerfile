FROM python:latest

ADD ./ /movie_dashboard

WORKDIR /movie_dashboard

RUN pip install -r requirements.txt

CMD ["streamlit run", "main.py"]