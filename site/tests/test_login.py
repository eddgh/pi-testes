from utils import navegador, time, By, Keys, url
import pytest

class TestLogin:  
   
    def setup_class(self):        
        global driver
        driver = navegador
        driver.maximize_window()
        
    def test_login_success(self):
        #abrindo a pagina home
        driver.get(url)             
        
        #botão Entrar (signin da pagina home)            
        btn_link_sign_in = driver.find_element(By.XPATH,'//*[@id="root"]/nav[1]/main/div[2]/div/div/button[1]')
        btn_link_sign_in.click()
        
        #certificar-se de que está na página de login    
        local = driver.current_url
        print('pagina atual : ' + local)
        assert local == url + 'signin'  
        
        #certificar-se de que o formulário é o de login
        titulo = driver.find_element(By.TAG_NAME,'h1')
        print('titulo do formulário : ' + titulo.text)
        assert 'Inicie sua sessão' in titulo.text
        
        #verificar existencia do botão Cadastre-se na página de login
        btn_signup = driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/main/p/button')
        print('Botão Cadastre-se : ' + btn_signup.text)
        assert 'Cadastre-se' in btn_signup.text        
                
        inputEmail = driver.find_element(By.XPATH,'//*[@id=\"root\"]/div[1]/main/form/input')
        inputEmail.click()
        inputEmail.send_keys('admin@admin.com')
            
        inputPassword = driver.find_element(By.XPATH,'//*[@id=\"root\"]/div[1]/main/form/div/input')
        inputPassword.click()
        inputPassword.send_keys('12345678')
        # inputPassword.send_keys(Keys.RETURN)
        time.sleep(2)
                                    
        btn_eye_password = driver.find_element(By.CLASS_NAME,'sc-hiKeQa.laojnR')
        btn_eye_password.click()
        driver.save_screenshot('screen_00.png')
            
        btn_submit = driver.find_element(By.XPATH,'//*[@id=\"root\"]/div[1]/main/form/button')
        btn_submit.click()
            
        time.sleep(2)               
        
    def teardown_class(self):
        driver.close()
        
        
    def test_login_fail(self):
        #abrindo a pagina home
        driver.get(url)             
        
        #botão Entrar (signin da pagina home)
        btn_link_sign_in = driver.find_element(By.XPATH,'//*[@id="root"]/nav[1]/main/div[2]/div/div/button[1]')            
        btn_link_sign_in.click()       
                   
        #Email invalido digitado
        inputEmail = driver.find_element(By.XPATH,'//*[@id=\"root\"]/div[1]/main/form/input')
        inputEmail.click()
        inputEmail.send_keys('admin')
        inputEmail.send_keys(Keys.RETURN)
        time.sleep(3)  
        failedEmail = driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/main/form/p[1]')
        print('Email invalido digitado: ' + failedEmail.text)
        assert 'É necessário um email válido' in failedEmail.text   
      
    def teardown_class(self):
        driver.close()        
     