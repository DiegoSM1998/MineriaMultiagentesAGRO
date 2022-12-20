#!/usr/bin/python3
# -- coding: utf-8 --
'''Scraper Consultas'''

import os
import pandas as pd
from sqlalchemy import create_engine
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

def guardarData(productos, datosTropel, fecha, ccaa):
    '''Genera fichero con los datos scrapeados'''
    contador=6
    nombrefichero='Data.Ampli.'+fecha+"."+ccaa+'.raw'
    file = open(nombrefichero, 'w')
    for producto in productos:
        file.write(fecha+"|"+ccaa+"|"+producto+"|")
        for i in range(contador-6,contador):
            file.write(datosTropel[i]+"|")
        contador+=6
        file.write("|\n")
    file.close()
    return nombrefichero

def subirData(nombrefichero):
    '''Sube el fichero a postgresql'''
    dataframe = pd.read_csv(nombrefichero, sep="|", decimal=",")
    engine= create_engine("postgresql://docker:docker@host.docker.internal/AGROdb")
    dataframe.to_sql(nombrefichero,engine)


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
#select product
grupoProductos= browser.find_element(By.XPATH, '''//select[@name="grupo"]''')
opcionesProductos=grupoProductos.find_elements(By.TAG_NAME,"option")
for option in opcionesProductos:
    if "20" == option.get_attribute("value"):
        option.click()
        print("Grupo de productos seleccionados: "+str(option.text))
#select periodo
periodo= browser.find_element(By.XPATH, '''//select[@name="periodo"]''')
opcionesPeriodo=periodo.find_elements(By.TAG_NAME,"option")
for option in opcionesPeriodo:
    print(str(option.get_attribute("value"))+": "+str(option.text))
periodoSeleccionado = input("Escriba el número de periodo:")
while( int(periodoSeleccionado)<1 or int(periodoSeleccionado)>96):
    periodoSeleccionado = input("Escriba un número del 1 al 96 por favor:")
for option in opcionesPeriodo:
    if periodoSeleccionado == option.get_attribute("value"):
        option.click()
        print("Periodo seleccionado: "+str(option.text))
        fecha=str(option.text)
#selct ccaa
comunidades=browser.find_element(By.XPATH, '''//select[@name="CCAA"]''')
opcionesComunidad=comunidades.find_elements(By.TAG_NAME,"option")
for option in opcionesComunidad:
    print(str(option.get_attribute("value"))+": "+str(option.text))
comunidadesSeleccionado = input("Escriba el codigo de la comunidad:")
while( int(comunidadesSeleccionado)<1 or int(comunidadesSeleccionado)>50):
    comunidadesSeleccionado = input("Escriba el codigo exacto por favor:")
for option in opcionesComunidad:
    if comunidadesSeleccionado == option.get_attribute("value"):
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

productos=productos[3:]

namefichero=guardarData(productos,datosTropel, fecha, ccaa)

browser.quit()
subirData(namefichero)
print("Archivo "+str(namefichero)+" subido a postgreSQL")

