from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico)

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url ='http://localhost:5173/'

import time

# ******************************** Pattern Funcitions ********************************

btn_link_sign_in = '//*[@id="root"]/nav[1]/main/div[2]/div/div/button[1]'

# Abrir a pagina home
def open_home():
    driver.get(url)
    driver.maximize_window()
    
# Clicar no botão Entrar (signin da pagina home) 
def sign_in():
    driver.find_element(By.XPATH, btn_link_sign_in).click()
    time.sleep(5)

#certificar-se de que está na página de login
def signin_certificate():    
    local = driver.current_url
    print('pagina atual : ' + local)
    assert local == url + 'signin'
    
def Email(email):
    inputEmail = driver.find_element(By.XPATH,'//*[@id=\"root\"]/div[1]/main/form/input')
    inputEmail.click()
    inputEmail.send_keys(email)
        