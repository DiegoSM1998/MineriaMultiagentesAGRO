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

def guardarData(productos, datosTropel, fecha, ccaa):
    x=6
    if not os.path.exists('data'):
        os.makedirs('data')

    nombrefichero='/data/Dataset1.1.-DatosConsumoAlimentario_'+fecha+"_"+ccaa+'.txt'
    f = open(nombrefichero, 'w')
    for producto in productos:
        f.write(fecha+"|"+ccaa+"|"+producto+"|")
        for i in range(x-6,x):
            f.write(datosTropel[i]+"|")
        x+=6
        f.write("|\n")
    f.close()

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

x=6
productos=productos[3:]
for producto in productos:
    print(producto)
    for i in range(x-6,x):
        print(datosTropel[i])
    x+=6
    print("\n")

guardarData(productos,datosTropel, fecha, ccaa)

browser.quit()