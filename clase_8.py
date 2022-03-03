import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

class usando_unittest(unittest.TestCase):

    def setUp(self):
        try:
            self.driver = webdriver.Chrome(ChromeDriverManager().install())
        except Exception as e:
            print(f'Ha ocurrido un error: {e}')

    def test_cambiar_ventana(self):
        driver = self.driver
        driver.get('http://www.google.com')
        time.sleep(3)
        aceptar = driver.find_element_by_id('L2AGLb')
        aceptar.click()
        time.sleep(3)
        driver.execute_script("window.open(' ');") # para abrir otra ventana
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[1])
        driver.get('http://stackoverflow.com')
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(10)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()