FROM python:3.10.6
WORKDIR /

COPY . .

RUN pip install psycopg2
RUN pip install pandas 
RUN pip install sqlalchemy


CMD python3 limpiarData.py

EXPOSE 5432

