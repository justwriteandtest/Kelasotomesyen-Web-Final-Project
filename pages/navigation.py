from selenium.webdriver.common.by import By
from locators.navigation import Locator
from pages.component import Component

class NavBar(Component):
    def goToCart(self):
        self.findElementByXPath(Locator.linkShoppingCartXPath).click()

    def openBurgerMenu(self):
        self.findElementByXPath(Locator.buttonOpenBurgerMenuXPath).click()

    def logOut(self):
        self.openBurgerMenu()
        self.findElementByXPath(Locator.linkLogoutXPath).click()

    def goToAboutPage(self):
        self.openBurgerMenu()
        self.findElementByXPath(Locator.linkAboutXPath).click()

    def goToInventoryPage(self):
        self.openBurgerMenu()
        self.findElementByXPath(Locator.linkInventoryXPath).click()

    def resetAppState(self):
        self.openBurgerMenu()
        self.findElementByXPath(Locator.linkResetXPath).click()