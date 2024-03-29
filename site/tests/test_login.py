
from utils import *

class TestLogin:
        
       
    def test_login_button_view_password(self):
        login() # Entrar na página de login
        Password('12345678')
        viewPasswordButton()
        print("Verifique o screenshot 'screen_view_password.png'")
        
    def test_login_success(self):                   
        login() # Entrar na página de login                 
        signin_page_certificate('signin')  # Certificar-se de que está na página de login baseado no endPoint      
        form_login_certificate_hasTitle('Inicie sua sessão') # Certificar-se de que o formulário é o de login            
        signup_button_exists('Cadastre-se') # Verificar existencia do botão Cadastre-se na página de login     
        Email('admin@admin.com') # Enviando email success
        Password('12345678') # Enviando password success            
        login_button_submit() # Enviar o formulário de login
        driver.save_screenshot('screen_login_success.png')
        avatar = driver.find_element(By.CSS_SELECTOR, '#root > nav.sc-bdnyFh.ghDIEg > main > div.sc-eCAqax.kbjCsX > p.sc-jrsKJM.dasuIU')  
        assert avatar.text is not "" 
        print('Usuario Logado: iniciais(' + avatar.text + ')')          
        logout()  
              
    def test_login_fail_invalid_email(self):
        login() # Entrar na página de login      
        invalidEmail('admin@') # Digitar um Email invalido
        time.sleep(3)
        
    def test_login_fail_blank_email(self):
        login() # Entrar na página de login      
        blankEmail('') # Campo Email deixado em branco
        time.sleep(3)
        
    def test_login_fail_invalid_password(self):
        login() # Entrar na página de login      
        invalidPassword('12345') # Password com menos de 6 digitos
        driver.save_screenshot('screen_invalid_password.png') 
        time.sleep(3)                
                

     