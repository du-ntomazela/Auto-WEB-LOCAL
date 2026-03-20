from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import TIMEOUT

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, TIMEOUT)

    def acessar(self, url):
        self.driver.get(url)

    def preencher_usuario(self, usuario):
        campo = self.wait.until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        campo.send_keys(usuario)

    def preencher_senha(self, senha):
        campo = self.driver.find_element(By.ID, "password")
        campo.send_keys(senha)

    def clicar_login(self):
        botao = self.driver.find_element(By.ID, "login")
        botao.click()