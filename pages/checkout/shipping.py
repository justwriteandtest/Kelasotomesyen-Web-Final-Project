from locators.checkout.shipping import Locator
from pages.component import Component

class ShippingPage(Component):
    def fillFirstName(self, firstName = ''):
        self.findElementByXPath(Locator.inputFirstNameXPath).send_keys(firstName)

    def fillLastName(self, lastName = ''):
        self.findElementByXPath(Locator.inputLastNameXPath).send_keys(lastName)

    def fillPostalCode(self, postalCode = ''):
        self.findElementByXPath(Locator.inputPostalCodeXPath).send_keys(postalCode)

    def continueCheckout(self):
        self.findElementByXPath(Locator.buttonContinueXPath).click()

    def cancelCheckout(self):
        self.findElementByXPath(Locator.buttonCancelXPath).click()