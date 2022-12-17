## Run selenium and chrome driver to scrape data
import time
import os.path
from os import remove
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

def guardarData(productos, datosTropel, fecha, ccaa, desde):
    x=6
    nombrefichero='Dataset1.1.-DatosConsumoAlimentario_'+str(desde)+'-2020.txt'
    f = open(nombrefichero, 'a')
    if os.stat(nombrefichero).st_size == 0:
        f.write("Año|Mes|CCAA|Producto|")
        for i in range(x-6,x):
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

def lanzarSelenium(periodoSeleccionado,comunidadesSeleccionado,desde):
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
        if("20" == option.get_attribute("value")):
            option.click()

    periodo= browser.find_element(By.XPATH, '''//select[@name="periodo"]''')
    opcionesPeriodo=periodo.find_elements(By.TAG_NAME,"option")
    for option in opcionesPeriodo:
        if(str(periodoSeleccionado) == option.get_attribute("value")):
            option.click()
            fecha=str(option.text)
                    
    comunidades=browser.find_element(By.XPATH, '''//select[@name="CCAA"]''')
    opcionesComunidad=comunidades.find_elements(By.TAG_NAME,"option")
    for option in opcionesComunidad:
        if(str(comunidadesSeleccionado) == option.get_attribute("value")):
            option.click()
            ccaa=str(option.text)

    boton=browser.find_element(By.XPATH, '//*[@id="boton1"]')
    boton.send_keys(Keys.ENTER)

    productoCol=browser.find_elements(By.XPATH,('''//tbody/tr/th/span'''))
    datosCols=browser.find_elements(By.XPATH,('''//tbody/tr/td[2]/span[@class="tabla_texto_normal"]'''))

    productos=[]
    productos.append("Producto")
    for producto in productoCol[3:]:
        productos.append(producto.text)
    datosTropel=[]
    for volumen in datosCols:
        datosTropel.append(volumen.text)

    # x=6
    # productos=productos[3:]
    # for producto in productos:
    #     print(producto)
    #     for i in range(x-6,x):
    #         print(datosTropel[i])
    #     x+=6
    #     print("\n")

    guardarData(productos,datosTropel, fecha, ccaa,desde)

    browser.quit()
        
def main(): 
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
    mensajeDesde='''Desde que año desea cargar la base de datos'''
    mensajeDesde+='''\n-1: 2013\n-2: 2014\n-3: 2015\n-4: 2016\n-5: 2017\n-6: 2018\n-7: 2019\n-8: 2020\nEscriba el indice:'''
    selecDesde =input(mensajeDesde)
    
    while(int(selecDesde)>8 or int(selecDesde)<1):
        selecDesde =input("Indice no valido\nEscriba un número del 1 al 8 para seleccionar el año")
        
    periodo= browser.find_element(By.XPATH, '''//select[@name="periodo"]''')
    opcionesPeriodo=periodo.find_elements(By.TAG_NAME,"option")
    
    comunidades=browser.find_element(By.XPATH, '''//select[@name="CCAA"]''')
    opcionesComunidad=comunidades.find_elements(By.TAG_NAME,"option")

    desde=int(selecDesde)+2012
    if(int(selecDesde)==1): periodoSeleccionado=1
    else: periodoSeleccionado=((int(selecDesde)-1)*12)+1
    nombrefichero='Dataset1.1.-DatosConsumoAlimentario_'+str(desde)+'-2020.txt'
    if(os.path.exists(nombrefichero)):
        remove(nombrefichero)
    while (periodoSeleccionado<97):
        for option in opcionesComunidad:
            if(option.get_attribute("value") == "XX"): pass
            else:lanzarSelenium(periodoSeleccionado, option.get_attribute("value"),desde)
        periodoSeleccionado+=1         

                 
main()
