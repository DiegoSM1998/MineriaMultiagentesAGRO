## Run selenium and chrome driver to scrape data
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
browser.get("https://www.huercasa.com/es/blog/listado-de-superalimentos-27-productos-que-no-pueden-faltar-en-tu-casa")

# Extract description from page and print
forms = browser.find_elements(By.XPATH, "//h3")
superalimentos=""
f = open('superalimentos.txt', 'w')
for form in forms:
    superalimento=(str(form.text).split(".")[1])
    f.write(str(superalimento))
    f.write("\n")

browser.quit()