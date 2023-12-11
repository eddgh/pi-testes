import time
from utils import open_home
from utils.config_browser import *

class TestFooter_Copyright:
        
    def test_footerCopyRightText(self):
        open_home()
        footerCopyRights = driver.find_element(By.XPATH, '//*[@id="root"]/nav[2]/main/p')
        esperado = '\u00A92023 Direitos reservados dhrentcar.com.br' # \u00A9 = ©️
        print('Esperado: ' + esperado)
        print('Encontrado: ' + footerCopyRights.text)
        assert esperado in footerCopyRights.text
    
class TestFooterSocialMedia:
    
    def test_footerSocialMedia_Facebook(self):
        open_home()
        Facebook = driver.find_element(By.CSS_SELECTOR,'#root > nav.sc-dItHI.fhchdd > main > div > button:nth-child(1) > svg')
        Facebook.screenshot
        Facebook.click()
        time.sleep(2)
        driver.save_screenshot('screen_Facebook_Btn_Click.png')
        print("Verifique o screenshot 'screen_Facebook_Btn_Click.png'")       

    def test_footerSocialMedia_Linkedin(self):
        open_home()
        Linkedin = driver.find_element(By.CSS_SELECTOR,'#root > nav.sc-dItHI.fhchdd > main > div > button:nth-child(2) > svg')
        Linkedin.screenshot
        Linkedin.click()
        time.sleep(2)
        driver.save_screenshot('screen_Linkedin_Btn_Click.png')
        print("Verifique o screenshot 'screen_Linkedin_Btn_Click.png'")

    def test_footerSocialMedia_Instagram(self):
        open_home()
        Instagram = driver.find_element(By.CSS_SELECTOR,'#root > nav.sc-dItHI.fhchdd > main > div > button:nth-child(3) > svg')
        Instagram.screenshot
        Instagram.click()
        time.sleep(2)
        driver.save_screenshot('screen_Instagram_Btn_Click.png')
        print("Verifique o screenshot 'screen_Instagram_Btn_Click.png'")   
        
    def test_footerSocialMedia_Twitter(self):
        open_home()
        Twitter = driver.find_element(By.CSS_SELECTOR,'#root > nav.sc-dItHI.fhchdd > main > div > button:nth-child(4) > svg')
        Twitter.screenshot
        Twitter.click()
        time.sleep(2)
        driver.save_screenshot('screen_Twitter_Btn_Click.png')
        print("Verifique o screenshot 'screen_Twitter_Btn_Click.png'")               
        
               
                
    
        