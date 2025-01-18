from locators.cart import Locator
from pages.component import Component

class CartPage (Component):
    def continueShopping(self):
        self.findElementByXPath(Locator.buttonContinueShoppingXPath).click()

    def checkout(self):
        self.findElementByXPath(Locator.buttonCheckoutXPath).click()

    def removeItemFromCart(self, item: str):
        if item in Locator.buttonRemoveFromCart.keys():
            self.findElementByXPath(Locator.buttonRemoveFromCart[item]).click()
    
    def itemIsInCart(self, item: str) -> bool:
        try:
            self.findElementByXPath(Locator.buttonRemoveFromCart[item])

            return True
        except:
            return False