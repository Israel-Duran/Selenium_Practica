import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

class usando_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_buscar(self):
        driver = self.driver
        driver.get('http://www.google.com')
        time.sleep(1)
        aceptar = driver.find_element_by_id('L2AGLb')
        aceptar.click()
        time.sleep(2)
        self.assertIn('Google', driver.title)
        elemento = driver.find_element_by_name('q')
        elemento.send_keys('Selenium')
        elemento.send_keys(Keys.RETURN)
        time.sleep(5)
        assert 'Nose encontró el elemento:' not in driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()