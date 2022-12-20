FROM python:3.10.6
WORKDIR /

COPY . .

RUN pip install psycopg2
RUN pip install pandas 
RUN pip install sqlalchemy
RUN pip install seaborn
RUN pip install numpy
RUN pip install seaborn
RUN pip install scikit-learn
RUN pip install sqlalchemy
RUN pip install matplotlib

CMD python3 linear_regression.py

EXPOSE 5432

