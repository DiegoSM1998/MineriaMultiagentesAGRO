FROM python:3.10.6
COPY . .
WORKDIR /

RUN apt-get install -y chromium
RUN pip install psycopg2
RUN pip install pandas
RUN pip install sqlalchemy
RUN pip install selenium

EXPOSE 5432

CMD python3 ScraperBDConsumoHogaresConsultas.py