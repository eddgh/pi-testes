from utils import open_home
from utils.config_browser import *

class TestFooter:
        
    def test_footerCopyRightsTextIs(self):
        open_home()
        footerCopyRights = driver.find_element(By.XPATH, '//*[@id="root"]/nav[2]/main/p')
        esperado = '\u00A92023 Direitos reservados dhrentcar.com.br' # \u00A9 = ©️
        print('Esperado: ' + esperado)
        print('Encontrado: ' + footerCopyRights.text)
        assert esperado in footerCopyRights.text   
        
    # def teardown_class(self):
    #     driver.close()