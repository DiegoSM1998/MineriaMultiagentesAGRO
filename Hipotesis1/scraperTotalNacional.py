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

from itertools import cycle
from shutil import get_terminal_size
from threading import Thread
from time import sleep
class Loader:
    def __init__(self, desc="Loading...", end="Done!", timeout=0.1):
        """
        A loader-like context manager

        Args:
            desc (str, optional): The loader's description. Defaults to "Loading...".
            end (str, optional): Final print. Defaults to "Done!".
            timeout (float, optional): Sleep time between prints. Defaults to 0.1.
        """
        self.desc = desc
        self.end = end
        self.timeout = timeout

        self._thread = Thread(target=self._animate, daemon=True)
        self.steps = [ ".  ", ".. ", "...","..:",".::",":::"]
        self.done = False

    def start(self):
        self._thread.start()
        return self

    def _animate(self):
        for c in cycle(self.steps):
            if self.done:
                break
            print(f"\r{self.desc} {c}", flush=True, end="")
            sleep(self.timeout)

    def __enter__(self):
        self.start()

    def stop(self):
        self.done = True
        cols = get_terminal_size((80, 20)).columns
        print("\r" + " " * cols, end="", flush=True)
        print(f"\r{self.end}", flush=True)

    def __exit__(self, exc_type, exc_value, tb):
        # handle exceptions with those variables ^
        self.stop()


if __name__ == "__main__":
    with Loader("Loading with context manager..."):
        for i in range(10):
            sleep(0.25)

def guardarData(productos, datosTropel, fecha, ccaa, desde):
    x=7
    nombrefichero='Dataset1.1.-DCA_PatatasYHortalizas_'+str(desde)+'-2020.txt'
    f = open(nombrefichero, 'a')
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
    else:
        x+=5
        fechas=fecha.split("-")
        fecha=str(fechas[0])+"|"+str(fechas[1])
        for producto in productos[1:]:
            f.write(fecha+"|"+ccaa+"|"+producto+"|")
            for i in range(x-6,x):
                f.write(datosTropel[i]+"|")
                print(datosTropel[i])
                
            x+=6
            f.write("|\n")
    f.close()

def lanzarSelenium(periodoSeleccionado,desde):
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
        if("16" == option.get_attribute("value")):
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
        if("1" == option.get_attribute("value")):
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
    loader = Loader("Cargando datos", "That was fast!", 1).start()
    while (periodoSeleccionado<97):
        lanzarSelenium(periodoSeleccionado,desde)
        periodoSeleccionado+=1         
    loader.stop()
                 
main()
