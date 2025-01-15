import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.login import LoginPage
from pages.inventory import InventoryPage

from dotenv import load_dotenv
import os

load_dotenv(override = True)

def testAddToCart(browser : webdriver.Chrome | webdriver.Edge | webdriver.Firefox | webdriver.Safari):
    login = LoginPage(browser)
    inventory = InventoryPage(browser)
    
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")    

    login.inputUsername(username)
    login.inputPassword(password)
    login.clickLoginButton()

    print("Logging in...")

    try:
        WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='app_logo']")))

        print(f"Site title: {inventory.siteTitle()}")
        print(f"Page title: {inventory.pageTitle()}")

        assert inventory.siteTitle() == "Swag Labs"
        assert inventory.pageTitle() == "Products"

        print("Login successful.")
    except Exception as e:
        print("Login failed.")

        print(e)

        assert False