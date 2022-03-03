import cv2
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

class usando_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_toogle(self):
        driver = self.driver
        driver.get('http://www.iberia.com')
        driver.maximize_window()
        time.sleep(3)
        cookies = driver.find_element_by_id('onetrust-accept-btn-handler')
        cookies.click()
        time.sleep(3)


if __name__ == '__main__':
    unittest.main()