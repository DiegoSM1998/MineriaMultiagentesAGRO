
"""
# Filename: run_selenium.py
"""

## Run selenium and chrome driver to scrape data from cloudbytes.dev
import time
import os.path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

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


forms = browser.find_element(By.XPATH, "//form")
fieldsets = forms.find_elements(By.XPATH,"//fieldset")
for fieldset in fieldsets:
    select= fieldset.find_element(By.XPATH,"//select")
    all_options=select.find_elements(By.TAG_NAME,"option")
    for option in all_options:
        print(str(option.get_attribute("value"))+": "+str(option.text))
        option.click()





#Wait for 10 seconds
time.sleep(10)
browser.quit()