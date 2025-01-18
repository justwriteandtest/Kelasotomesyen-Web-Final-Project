from locators.details import Locator

from pages.component import Component

class ItemDetailsPage(Component):
    def addToCart(self):
        self.findElementByXPath(Locator.buttonAddToCartXPath).click()

    def removeFromCart(self):
        self.findElementByXPath(Locator.buttonRemoveFromCartXPath).click()

    def backToProducts(self):
        self.findElementByXPath(Locator.buttonBackXPath).click()