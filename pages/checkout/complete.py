from locators.checkout.complete import Locator
from pages.component import Component

class CompletePage(Component):
    def returnToHome(self):
        self.findElementByXPath(Locator.buttonBackHome).click()