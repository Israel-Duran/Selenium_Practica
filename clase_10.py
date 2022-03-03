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
        driver.get('http://www.google.com')

        try:
            elemento = WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.NAME, 'q'))   #Explicit Wait

        except Exception as e:
            print(f'Ha ocurrido un error: {e}')
        finally:
            driver.quit()

if __name__ == '__main__':
    unittest.main()