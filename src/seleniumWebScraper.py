

DIR = "https://www.mapa.gob.es/app/consumo-en-hogares/consulta11.asp"

import time
import os.path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Crear objeto de parámetro de Chrome
chrome_options = Options()
chrome_options.add_argument("--headless") # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")
    
# Establezca Chrome en modo sin interfaz, independientemente de Windows o Linux, adapte automáticamente los parámetros correspondientes
homedir = os.path.expanduser("~")
webdriver_service = Service(f"{homedir}/chromedriver/stable/chromedriver")

# Crear objeto sin interfaz de Chrome
browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# Visita Baidu
browser.get('DIR')

# Extract description from page and print
description = browser.find_element(By.NAME, "description").get_attribute("content")
print(f"{description}")

#Wait for 10 seconds
time.sleep(10)
browser.quit()