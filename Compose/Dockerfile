FROM python:3.10

COPY . .

RUN pip install -r requeriments.txt

RUN pip install selenium
RUN apt-get update && apt-get install -y chromium

CMD ["python", "/src/ScrapperBDSuperAlimentos.py"]