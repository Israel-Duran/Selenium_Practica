import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

class usando_exlisit_way(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_explisit_wait(self):
        driver = self.driver
        driver.implicitly_wait(5)   #es el equivalente al time.sleep pero este deja de contar el tiempo cuando encuetra el elemento
        driver.get('http://www.google.com')
        myDynamicElement = driver.find_element_by_name('q')

if __name__ == '__main__':
    unittest.main()