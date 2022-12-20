## Run selenium and chrome driver to scrape data
import time
import os.path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import psycopg2
import os
import pandas as pd
from sqlalchemy import create_engine

def guardarData(productos, datosTropel, fecha, ccaa):
    x=7
    nombrefichero='Data.Ampli'+fecha+"_"+ccaa+'.raw'
    f = open(nombrefichero, 'w')
    if os.stat(nombrefichero).st_size == 0:
        f.write("Año|Mes|CCAA|Producto")
        for i in range(x-7,x):
            f.write(datosTropel[i]+"|")
        f.write("|\n")
    x+=6
    fechas=fecha.split("-")
    fecha=str(fechas[0])+"|"+str(fechas[1])
    for producto in productos[1:]:
        f.write(fecha+"|"+ccaa+"|"+producto+"|")
        for i in range(x-6,x):
            f.write(datosTropel[i]+"|")
        x+=6
        f.write("|\n")
    f.close()
    return nombrefichero

## Setup chrome options
chrome_options = Options()
chrome_options.add_argument("--headless") # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")

# Set path to chromedriver as per your configuration
homedir = os.path.expanduser("~")
webdriver_service = Service(f"{homedir}/chromedriver/stable/chromedriver")

# Choose Chrome Browser ubuntu
browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)

browser.get("https://www.mapa.gob.es/app/consumo-en-hogares/consulta11.asp")

grupoProductos= browser.find_element(By.XPATH, '''//select[@name="grupo"]''')
opcionesProductos=grupoProductos.find_elements(By.TAG_NAME,"option")
for option in opcionesProductos:
    print(str(option.get_attribute("value"))+": "+str(option.text))
productoSeleccionado = input("Escriba el número del grupo de alimentos:")
while( int(productoSeleccionado)<1 or int(productoSeleccionado)>96):
    periodoSeleccionado = input("Escriba un número del 1 al 28 por favor:")
for option in opcionesProductos:
    if(productoSeleccionado == option.get_attribute("value")):
        option.click()
        print("Grupo de productos seleccionados: "+str(option.text))

periodo= browser.find_element(By.XPATH, '''//select[@name="periodo"]''')
opcionesPeriodo=periodo.find_elements(By.TAG_NAME,"option")
for option in opcionesPeriodo:
    print(str(option.get_attribute("value"))+": "+str(option.text))
periodoSeleccionado = input("Escriba el número de periodo:")
while( int(periodoSeleccionado)<1 or int(periodoSeleccionado)>96):
    periodoSeleccionado = input("Escriba un número del 1 al 96 por favor:")
for option in opcionesPeriodo:
    if(periodoSeleccionado == option.get_attribute("value")):
        option.click()
        print("Periodo seleccionado: "+str(option.text))
        fecha=str(option.text)
                 
comunidades=browser.find_element(By.XPATH, '''//select[@name="CCAA"]''')
opcionesComunidad=comunidades.find_elements(By.TAG_NAME,"option")
for option in opcionesComunidad:
    print(str(option.get_attribute("value"))+": "+str(option.text))
comunidadesSeleccionado = input("Escriba el codigo de la comunidad:")
while( int(comunidadesSeleccionado)<1 or int(comunidadesSeleccionado)>96):
    comunidadesSeleccionado = input("Escriba el codigo exacto por favor:")
for option in opcionesComunidad:
    if(comunidadesSeleccionado == option.get_attribute("value")):
        option.click()
        print("CCAA seleccionada: "+str(option.text))
        ccaa=str(option.text)

boton=browser.find_element(By.XPATH, '//*[@id="boton1"]')
boton.send_keys(Keys.ENTER)

productoCol=browser.find_elements(By.XPATH,('''//tbody/tr/th/span'''))
datosCols=browser.find_elements(By.XPATH,('''//tbody/tr/td[2]/span[@class="tabla_texto_normal"]'''))

productos=[]
productos.append("Producto")
for producto in productoCol:
    productos.append(producto.text)
datosTropel=[]
for volumen in datosCols:
    datosTropel.append(volumen.text)

nombre=guardarData(productos,datosTropel, fecha, ccaa)

def subirData(nombre):
    df = pd.read_csv(nombre, sep="|", decimal=",")
    engine= create_engine("postgresql://docker:docker@host.docker.internal/AGROdb")
    df.to_sql(nombre,engine)

subirData(nombre)
print("Archivo "+str(nombre)+" subido a postgreSQL")

browser.quit()