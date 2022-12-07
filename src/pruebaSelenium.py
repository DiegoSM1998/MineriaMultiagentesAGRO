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

## Setup chrome options
chrome_options = Options()
chrome_options.add_argument("--headless") # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")

# Set path to chromedriver as per your configuration
homedir = os.path.expanduser("~")
webdriver_service = Service(f"{homedir}/chromedriver/stable/chromedriver")

# Choose Chrome Browser
browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# Get page
browser.get("https://www.mapa.gob.es/app/consumo-en-hogares/consulta11.asp")

bolGrupoProductos=False
bolPeriodoConsulta=False
bolIntervalo=False
bolComunidad=False

forms = browser.find_element(By.XPATH, "//form")
fieldsets = forms.find_elements(By.XPATH,"//fieldset")

for fieldset in fieldsets:
        select= fieldset.find_element(By.XPATH,"//select")
        all_options=select.find_elements(By.TAG_NAME,"option")
        if(bolGrupoProductos==False):
            print("Selecciona el producto:")
            for option in all_options:
                print(str(option.get_attribute("value"))+": "+str(option.text))
            producto = input("Escriba el número de producto:")
            while( int(producto)<1 or int(producto)>28):
                producto = input("Escriba un número del 1 al 28 por favor:")
            for option in all_options:
                if(producto == option.get_attribute("value")):
                    option.click()
                    print("Producto seleccionado: "+str(option.text))
                    bolGrupoProductos=True

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
        bolGrupoProductos=True
            
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
        bolGrupoProductos=True

timeout=3
boton=browser.find_element(By.XPATH, '//*[@id="boton1"]')
boton.send_keys(Keys.ENTER)

tbody=browser.find_element(By.XPATH,"//tbody")
tds=tbody.find_elements(By.XPATH, "//td")
for td in tds:
    if((td.text) != ""):
        print(td.text)



tablaf=[]
tabla=browser.find_elements(By.XPATH,'''//span[@class="tabla_texto_normal_n2"]''')
for t in tabla:
    tablaf.append(t.text)
tabla1=browser.find_elements(By.XPATH,'''//span[@class="tabla_texto_normal_n2"]''')
for t1 in tabla1:
    tablaf.append(t1.text)

tabla1=browser.find_elements(By.XPATH,'''//span[@class="tabla_texto_normal"]''')
for t1 in tabla1:
    tablaf.append(t1.text)

print(tablaf)

#Wait for 10 seconds
time.sleep(1)
browser.quit()