from selenium.webdriver.common.by import By
from selenium import webdriver
from locators.login import Locator

class LoginPage:
    def __init__(self, driver : webdriver.Chrome | webdriver.Firefox | webdriver.Edge | webdriver.Safari):
        self.driver = driver

    def inputUsername(self, username): 
        self.driver.find_element(By.ID, Locator.inputUsernameID).send_keys(username)

    def inputPassword(self, password):
        self.driver.find_element(By.ID, Locator.inputPasswordID).send_keys(password)
        
    def clickLoginButton(self):
        self.driver.find_element(By.ID, Locator.btnLoginID).click()

    def getErrorText(self):
        return self.driver.find_element(By.XPATH, Locator.textErrorXPath).text