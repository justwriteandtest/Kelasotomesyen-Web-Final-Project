from locators.inventory import Locator

from pages.component import Component

from const.inventory import OpenDetailsMethods

class InventoryPage(Component):
    def siteTitle(self):
        return self.findElementByXPath(Locator.appLogoXPath).text

    def pageTitle(self):
        return self.findElementByXPath(Locator.pageTitleXPath).text
    
    def addToCart(self, item = ''):
        if item in Locator.buttonAddItemToCart.keys():
            self.findElementByXPath(Locator.buttonAddItemToCart[item]).click()
        else:
            pass
    
    def removeFromCart(self, item = ''):
        if item in Locator.buttonRemoveItemFromCart.keys():
            self.findElementByXPath(Locator.buttonRemoveItemFromCart[item]).click()
        else:
            pass

    def goToPage(self, item = '', method = OpenDetailsMethods.text):
        if item in Locator.imageItemLink.keys():
            match method:
                case OpenDetailsMethods.text:
                    self.findElementByXPath(Locator.textItemLink[item]).click()
                case OpenDetailsMethods.image:
                    self.findElementByXPath(Locator.imageItemLink[item]).click()
        else:
            pass