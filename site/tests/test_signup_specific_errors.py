import time
from utils import *
from utils.config_browser import *

class TestSignUpSpecificErrors:

    def test_signup_fail_invalid_email(self):
       open_home()
       sign_up()       
       inputEmail = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/form/input[3]')
       inputEmail.send_keys('admim@' + Keys.ENTER)  
       time.sleep(5)            
       errors = driver.find_elements(By.TAG_NAME, 'p')
       msg = errors[2].text
       if msg:
           print('Email inválido digitado: ', inputEmail.get_attribute('value') )
           print('msg: ' + msg)
       else:
           print('Email válido digitado: ', inputEmail.get_attribute('value') )
           print('Email digitado corretamente')