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

    def test_usando_opencv(self):
        driver = self.driver
        driver.get('http://www.google.com')
        driver.maximize_window()
        time.sleep(3)
        aceptar = driver.find_element_by_id('L2AGLb')
        aceptar.click()
        driver.save_screenshot('imagen_2.png')
        time.sleep(3)

    def test_comparando_imagenes(self):
        imagen_1 = cv2.imread('imagenes_1.imagen.png')
        imagen_2 = cv2.imread('imagen_2.png')
        diferencia = cv2.absdiff(imagen_1, imagen_2)
        imagen_gris = cv2.ctvColor(diferencia, cv2.COLOR_BGR2GRAY)
        contours,_ = cv2.findContours(imagen_gris,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

        for x in contours:
            if cv2.contourArea(x) >= 20:
                posicion_x, posicion_y, ancho,alto = cv2.boundingRect()
                cv2.rectangle(imagen_1, (posicion_x, posicion_y, (posicion_x+ancho, posicion_y+alto, (0,0,0,255),2)))

        while(1):
            cv2.imshow('Imagen1', imagen_1)
            cv2.imshow('Imagen2', imagen_2)
            cv2.imshow('Diferencias detectadas', diferencia)
            teclado = cv2.waitKey(5) & 0xFF
            if teclado == 27:
                break
            cv2.destroyWindow()

if __name__ == '__main__':
    unittest.main()