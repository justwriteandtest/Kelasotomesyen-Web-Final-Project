from locators.checkout.overview import Locator
from pages.component import Component

class OverviewPage(Component):
    def finishCheckout(self):
        self.findElementByXPath(Locator.buttonFinishXPath).click()

    def cancelCheckout(self):
        self.findElementByXPath(Locator.buttonCancelXPath).click()