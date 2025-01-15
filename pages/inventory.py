from selenium.webdriver.common.by import By
from selenium import webdriver
from locators.inventory import Locator

class InventoryPage:
    def __init__(self, driver : webdriver.Chrome | webdriver.Firefox | webdriver.Edge | webdriver.Safari):
        self.driver = driver

    def siteTitle(self):
        return self.driver.find_element(By.XPATH, Locator.appLogoXPath).text

    def pageTitle(self):
        return self.driver.find_element(By.XPATH, Locator.pageTitleXPath).text