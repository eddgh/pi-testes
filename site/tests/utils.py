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
    time.sleep(3)
    
# Entrar na página de login
def login():
    open_home()          
    sign_in()    

#certificar-se de que está na página de login
def signin_page_certificate(signinEndPoint):    
    local = driver.current_url
    print('pagina atual : ' + local)
    assert local == url + signinEndPoint
    
def form_login_certificate_hasTitle(textInPage):
    titulo = driver.find_element(By.TAG_NAME,'h1')
    print('titulo do formulário : ' + titulo.text)
    assert textInPage in titulo.text    
    
# Verificar existencia do botão Cadastre-se
def signup_button_exists(buttonText):
    btn_signup = driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/main/p/button')
    print('Botão Cadastre-se : ' + btn_signup.text)
    assert buttonText in btn_signup.text            
    
def Email(email):
    inputEmail = driver.find_element(By.XPATH,'//*[@id=\"root\"]/div[1]/main/form/input')
    inputEmail.click()
    inputEmail.send_keys(email)
    
def invalidEmail(email):
    Email(email + Keys.RETURN)
    failedEmail = driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/main/form/p[1]') # gera a mensagem de erro 'É necessário um email válido'
    print('Email invalido digitado: ' + failedEmail.text)
    assert 'É necessário um email válido' in failedEmail.text     

def blankEmail(email):
    Email(email + Keys.RETURN)
    failedEmail = driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/main/form/p[1]') # gera a mensagem de erro 'O campo de email não foi preenchido.'
    print('Campo Email em branco: ' + failedEmail.text)
    assert 'O campo de email não foi preenchido.' in failedEmail.text        

def Password(password):
    inputPassword = driver.find_element(By.XPATH,'//*[@id=\"root\"]/div[1]/main/form/div/input')
    inputPassword.click()
    inputPassword.send_keys(password)
    
def invalidPassword(password):
    Password(password + Keys.RETURN )
    driver.save_screenshot('screen_invalid_password.png')
    failedPassword = driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/main/form/p[2]') # gera a mensagem de erro 'A senha deve conter no mínimo 6 caracteres.'
    print('Password inválido: ' + failedPassword.text)
    print('Senha digitada: ' + password)
    assert 'A senha deve conter no mínimo 6 caracteres.' in failedPassword.text            
    
def viewPasswordButton():
    btn_eye_password = driver.find_element(By.CLASS_NAME,'sc-hiKeQa.laojnR')
    btn_eye_password.click()
    driver.save_screenshot('screen_view_password.png')

def login_button_submit():
    btn_submit = driver.find_element(By.XPATH,'//*[@id=\"root\"]/div[1]/main/form/button')
    btn_submit.click()            
    time.sleep(2)        