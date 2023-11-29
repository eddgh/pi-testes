import time
from utils import open_home
from utils.config_browser import *

class TestNavBar:
        
    def test_NavBar_Logo(self):
        open_home()
        navBarLogo = driver.find_element(By.CSS_SELECTOR, '#root > nav.sc-bdnyFh.jVcacZ > main > div.sc-dlniIP.cnAMdn > img')
        src = navBarLogo.get_property('src')
        object_type = navBarLogo.aria_role
        print('Tipo de objeto: ' + object_type) 
        print('Caminho da imagem: ', src)
        assert object_type == 'image' 

    def test_NavBar_Btn_signup(self):
        open_home()
        navBarBtnSignup = driver.find_element(By.XPATH, '//*[@id="root"]/nav[1]/main/div[2]/div/div/button[2]')
        Destino_esperado = driver.current_url + 'signup'
        navBarBtnSignup.click()
        time.sleep(3)
        print('Destino esperado: ' + Destino_esperado)
        Destino_encontrado = driver.current_url
        print ('Destino encontrado: ' + Destino_encontrado)
        assert Destino_esperado == Destino_encontrado
        
    def test_NavBar_Btn_signin(self):
        open_home()
        navBarBtnSignin = driver.find_element(By.XPATH, '//*[@id="root"]/nav[1]/main/div[2]/div/div/button[1]')
        Destino_esperado = driver.current_url + 'signin'
        navBarBtnSignin.click()
        time.sleep(3)
        print('Destino esperado: ' + Destino_esperado)
        Destino_encontrado = driver.current_url
        print ('Destino encontrado: ' + Destino_encontrado)
        assert Destino_esperado == Destino_encontrado 


    def test_NavBarBtnAcessRoute(self):
        open_home()
        navBarBtnAcessRoute = driver.find_element(By.CSS_SELECTOR, '#root > nav.sc-bdnyFh.jVcacZ > main > div.sc-eCAqax.kbjCsX > div > div > button:nth-child(3)')
        Destino_esperado = driver.current_url + 'produto/123123'
        navBarBtnAcessRoute.click()
        time.sleep(3)
        print('Nome do botão: ' + navBarBtnAcessRoute.text)
        print('Destino esperado: ' + Destino_esperado)
        Destino_encontrado = driver.current_url
        print ('Destino encontrado: ' + Destino_encontrado)
        assert Destino_esperado == Destino_encontrado 

    def teardown_class(self):
        driver.close()                               