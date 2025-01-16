from selenium.webdriver.common.by import By
from locators.cart import Locator
from pages.component import Component

class CartPage (Component):
    def continueShopping(self):
        self.driver.find_element(By.XPATH, Locator.buttonContinueShoppingXPath).click()

    def checkout(self):
        self.driver.find_element(By.XPATH, Locator.buttonCheckoutXPath).click()

    def removeItemFromCart(self, item: str):
        if item in Locator.buttonRemoveFromCart.keys():
            self.driver.find_element(By.XPATH, Locator.buttonRemoveFromCart[item]).click()
    
    def itemIsInCart(self, item: str) -> bool:
        try:
            self.driver.find_element(By.XPATH, Locator.buttonRemoveFromCart[item])

            return True
        except:
            return False