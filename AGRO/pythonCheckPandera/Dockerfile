FROM python:3.10.6
WORKDIR /

COPY . .

RUN pip install psycopg2
RUN pip install pandas 
RUN pip install sqlalchemy
RUN pip install pandera


CMD python3 checkDataPandera.py

EXPOSE 5432

