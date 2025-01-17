from selenium.webdriver.common.by import By
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

            print(f"Item added: {item}")
        else:
            print(f"Attempted to add {item}, but it was not on the inventory list.")
    
    def removeFromCart(self, item = ''):
        if item in Locator.buttonRemoveItemFromCart.keys():
            self.findElementByXPath(Locator.buttonRemoveItemFromCart[item]).click()

            print(f"Item added: {item}")
        else:
            print(f"Attempted to add {item}, but it was not on the inventory list.")

    def goToPage(self, item = '', method = OpenDetailsMethods.text):
        if item in Locator.imageItemLink.keys():
            match method:
                case OpenDetailsMethods.text:
                    self.findElementByXPath(Locator.textItemLink[item]).click()
                case OpenDetailsMethods.image:
                    self.findElementByXPath(Locator.imageItemLink[item]).click()

            print(f"Visited {item}'s details page.")
        else:
            print(f"Attempted to visit {item}'s details page, but it was not on the inventory list.")