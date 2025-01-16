from selenium.webdriver.common.by import By
from locators.details import Locator

from pages.component import Component

class ItemDetailsPage(Component):
    def addToCart(self):
        self.driver.find_element(By.XPATH, Locator.buttonAddToCartXPath).click()

    def removeFromCart(self):
        self.driver.find_element(By.XPATH, Locator.buttonRemoveFromCartXPath).click()

    def backToProducts(self):
        self.driver.find_element(By.XPATH, Locator.buttonBackXPath).click()