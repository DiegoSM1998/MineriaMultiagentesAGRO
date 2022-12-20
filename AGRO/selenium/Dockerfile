FROM python:3.10.6
COPY . .
WORKDIR /


RUN apt-get update && apt-get install -y chromium
RUN pip install psycopg2
RUN pip install pandas
RUN pip install sqlalchemy
RUN pip install selenium

EXPOSE 5432
CMD ["/bin/bash", "-c", "while true; do read input; eval $input; done"]
RUN python3 ScraperBDConsumoHogaresConsultas.py