from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BrowserControllerX:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def navigate(self, url):
        self.driver.get(url)

    def click(self, element_xpath):
        try:
            element = WebDriverWait(self.driver, 50).until(
                EC.presence_of_element_located((By.XPATH, element_xpath))
            )
            element.click()
        except Exception as e:
            print(f"Error al dar click: {e.args}")

    def wait_and_click(self, xpath):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            element.click()
        except:
            print(f"Error: No se pudo hacer clic en {xpath}")
    def fill_input(self, element_xpath, text):
        try:
            input_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, element_xpath))
            )
            input_field.clear()
            input_field.send_keys(text)
        except Exception as e:
            print(f"Error al llenar el campo de entrada: {e}")


    def click_name (self, element_xpath_name):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, f"//*[text()='{element_xpath_name}']"))
            )
            element.click()
        except:
            print(f"Error: No se pudo hacer clic en {element}")
    def quit(self):
        self.driver.quit()