from selenium.webdriver.common.by import By
from locators.login import Locator

from pages.component import Component

class LoginPage (Component):
    def inputUsername(self, username): 
        self.driver.find_element(By.ID, Locator.inputUsernameID).send_keys(username)

    def inputPassword(self, password):
        self.driver.find_element(By.ID, Locator.inputPasswordID).send_keys(password)
        
    def clickLoginButton(self):
        self.driver.find_element(By.ID, Locator.btnLoginID).click()

    def getErrorText(self):
        return self.findElementByXPath(Locator.textErrorXPath).text