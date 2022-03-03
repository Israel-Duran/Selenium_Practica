import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

class usando_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_pagina_giguiente(self):
        driver = self.driver
        driver.get('http://www.gmail.com')
        time.sleep(3)
        driver.get('http://www.google.com')
        time.sleep(3)
        driver.get('http://www.youtube.com')
        time.sleep(3)
        driver.back()
        time.sleep(3)
        driver.back()   #para navegar entre paginas, ir hacia atras
        time.sleep(3)
        driver.forward()
        time.sleep(3)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()