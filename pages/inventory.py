from selenium.webdriver.common.by import By
from selenium import webdriver
from locators.inventory import Locator

from pages.component import Component

class InventoryPage(Component):
    def siteTitle(self):
        return self.driver.find_element(By.XPATH, Locator.appLogoXPath).text

    def pageTitle(self):
        return self.driver.find_element(By.XPATH, Locator.pageTitleXPath).text