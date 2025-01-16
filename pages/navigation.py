from selenium.webdriver.common.by import By
from locators.navigation import Locator
from pages.component import Component

class NavBar(Component):
    def goToCart(self):
        self.driver.find_element(By.XPATH, Locator.linkShoppingCartXPath).click()

    def openBurgerMenu(self):
        self.driver.find_element(By.XPATH, Locator.buttonOpenBurgerMenuXPath).click()

    def logOut(self):
        self.openBurgerMenu()
        self.driver.find_element(By.XPATH, Locator.linkLogoutXPath).click()

    def goToAboutPage(self):
        self.openBurgerMenu()
        self.driver.find_element(By.XPATH, Locator.linkAboutXPath).click()

    def goToInventoryPage(self):
        self.openBurgerMenu()
        self.driver.find_element(By.XPATH, Locator.linkInventoryXPath).click()

    def resetAppState(self):
        self.openBurgerMenu()
        self.driver.find_element(By.XPATH, Locator.linkResetXPath).click()