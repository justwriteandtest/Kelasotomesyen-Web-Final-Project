import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.login import LoginPage
from pages.inventory import InventoryPage

import data.login as loginData

from dotenv import load_dotenv
import os

load_dotenv(override = True)

def testLoginPositive(browser : webdriver.Chrome | webdriver.Edge | webdriver.Firefox | webdriver.Safari):
    with allure.step("Fill the Login Form"):
        login = LoginPage(browser)
        inventory = InventoryPage(browser)
        
        username = os.getenv("USERNAME")
        password = os.getenv("PASSWORD")    

        login.inputUsername(username)
        login.inputPassword(password)
        login.clickLoginButton()

    with allure.step("Check if the inventory page is displayed"):
        try:
            WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='app_logo']")))

            assert inventory.siteTitle() == "Swag Labs"
            assert inventory.pageTitle() == "Products"
        except Exception as e:
            assert False

@pytest.mark.parametrize("username, password, expectedMessage", loginData.negativeDataLogin)
def testLoginNegative(browser : webdriver.Chrome | webdriver.Edge | webdriver.Firefox | webdriver.Safari, username, password, expectedMessage):
    with allure.step("Fill the Login Form"):
        login = LoginPage(browser)

        login.inputUsername(username)
        login.inputPassword(password)
        login.clickLoginButton()

    with allure.step("Check the error message"):
        errorMessage = login.getErrorText()

    with allure.step(f"Error message shown: {errorMessage}"):
        assert errorMessage == expectedMessage