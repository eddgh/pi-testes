from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = 'http://localhost:5173/'

import time