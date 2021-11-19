FROM python:3.8.5

ADD ./ /movie_dashboard

WORKDIR /movie_dashboard

RUN pip install --upgrade pip
   
# RUN pip install numpy && \
#     pip install pandas && \
#     pip install requests && \
#     pip install scikit_surprise && \
#     pip install streamlit && \
#     pip install pymongo && \
#     pip install python-dotenv && \
#     pip install dnspython && \
#     pip install cython
RUN pip install -r requirements.txt

CMD streamlit run --server.port $PORT main.py