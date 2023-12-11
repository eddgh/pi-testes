import time
from utils import *
from utils.config_browser import *

class TestSignUp:
        
    def test_signup_buttons(self):
        open_home()
        print('01 - Entrou na página home ✔️')
        sign_up()
        print('02 - Clicou no botão Cadastrar da página home ✔️')
        btn_home()
        print('03 - Clicou na logo home da página Cadastrar ✔️')
        sign_up()
        print('04 - Clicou no botão Cadastrar da página home ✔️')
        driver.back
        print('05 - Voltou para a página de cadastro ✔️')      
        btnEntrar = driver.find_element(By.XPATH, '//*[@id="root"]/nav[1]/main/div[2]/div/button[1]')
        btnEntrar.click()
        print('06 - Clicou no botão Entrar da página Cadastrar ✔️')
        driver.back
        print('07 - Voltou para a página de cadastro ✔️')  
        btnAcessarRota = driver.find_element(By.XPATH, '//*[@id="root"]/nav[1]/main/div[2]/div/button[2]')
        btnAcessarRota.click()
        print('08 - Clicou no botão Acessar Rota ✔️')  
        sign_up()
        print('09 - Clicou no botão Cadastrar dentro da página de rota ✔️')  
        btnRegister = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/form/button')
        btnRegister.click()
        print('10 - Clicou no botão Registrar ✔️')
        btnDoYourLogin = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/p/button')
        btnDoYourLogin.click()
        print('11 - Clicou no botão Faça seu login ✔️')  
        btn_home()
        print('12 - Clicou na logo para a página home ✔️')  
        sign_up()
        print('13 - Clicou no botão Cadastrar ✔️')
        
        inputPassword = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/form/div[1]/input') 
        inputPassword.send_keys('123456')
        btnViewPassword = driver.find_element(By.CSS_SELECTOR, '#root > div.sc-bkbjWr.ccgmEz > main > form > div:nth-child(23) > svg')
        btnViewPassword.click()
        
        inputConfirmPassword = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/form/div[2]/input')
        inputConfirmPassword.send_keys('12345')
        btnViewConfirmPassword = driver.find_element(By.CSS_SELECTOR, '#root > div.sc-bkbjWr.ccgmEz > main > form > div:nth-child(26) > svg')
        btnViewConfirmPassword.click()
        
        btnRegister = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/form/button')
        btnRegister.click()
        
        driver.save_screenshot('screen_views_signup_password.png') 
        print('14 - Verifique a imagem: screen_views_signup_password.png')           
        
        time.sleep(5)
        print('18 - Fim do teste dos botões da pagina de cadastro! ✔️')  
               
    def test_signup_errors_all_blank(self):
        open_home()
        print('01 - Entrou na página home ✔️')
        sign_up()
        print('02 - Clicou no botão Cadastrar da página home ✔️')
        btnRegister = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/form/button')
        btnRegister.click()
        print('03 - Clicou no botão Registrar da página de cadastro sem preencher nada ✔️')
        time.sleep(5)
        
        blankErrorName = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/form/p[1]' )
        assert blankErrorName.text == 'Precisa ter no mínimo 3 caracteres'
        print('Nome não preenchido ou com menos de 3 caracteres')
        print('msg: ', blankErrorName.text)
        
        blankErrorSurName = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/form/p[2]')
        assert blankErrorSurName.text == 'Precisa ter no mínimo 3 caracteres'
        print('Sobrenome não preenchido ou com menos de 3 caracteres')
        print('msg: ', blankErrorSurName.text)
        
        blankErrorAge = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/form/p[3]')
        assert blankErrorAge.text == 'O campo de idade não foi preenchido.'
        print('Idade não preenchido')
        print('msg: ', blankErrorAge.text)

        blankErrorCPF = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/form/p[4]')
        assert blankErrorCPF.text == 'informe um cpf válido'
        print('CPF não preenchido')
        print('msg: ', blankErrorCPF.text)

        blankErrorPhone = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/form/p[5]')
        assert blankErrorPhone.text == 'O campo telefone não foi preenchido.'
        print('Telefone não preenchido')
        print('msg: ', blankErrorPhone.text)
        
        blankErrorEmail = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/form/p[6]')
        assert blankErrorEmail.text == 'O campo de email não foi preenchido.'
        print('Email não preenchido')
        print('msg: ', blankErrorEmail.text)
        
        blankErrorConfirmEmail = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/form/p[7]')
        assert blankErrorConfirmEmail.text == 'Você precisa confirmar o seu email'
        print('Email não confirmado')
        print('msg: ', blankErrorConfirmEmail.text)
        
        blankErrorPasword = driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/main/form/p[8]')
        assert blankErrorPasword.text == 'A senha deve conter no mínimo 6 caracteres.'
        print('Senha em branco ou com menos de 6 caracteres')
        print('msg: ', blankErrorPasword.text)
        
        blankErrorConfirmPasword = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/form/p[9]')
        assert blankErrorConfirmPasword.text == 'Você precisa confirmar a sua senha'
        print('Confirmação da senha está em branco')
        print('msg: ', blankErrorConfirmPasword.text)    
       
        time.sleep(3)