import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import allure

from pages.login import LoginPage
from pages.inventory import InventoryPage
from pages.navigation import NavBar
from pages.cart import CartPage
from pages.details import ItemDetailsPage

from data.inventory import addToCartList

from const.cart import AddToCartMethods
from const.cart import RemoveFromCartMethods

from dotenv import load_dotenv
import os

load_dotenv(override = True)

@pytest.mark.parametrize("itemList, addToCartMethod, removeFromCartMethod", addToCartList)
def testAddToCart(browser : webdriver.Chrome | webdriver.Edge | webdriver.Firefox | webdriver.Safari, itemList, addToCartMethod, removeFromCartMethod):
    with allure.step("Prepare the page classes"):
        login = LoginPage(browser)
        inventory = InventoryPage(browser)
        navbar = NavBar(browser)
        cart = CartPage(browser)
        details = ItemDetailsPage(browser)
    
    with allure.step("Log In"):
        username = os.getenv("USERNAME")
        password = os.getenv("PASSWORD")    

        login.inputUsername(username)
        login.inputPassword(password)
        login.clickLoginButton()

        try:
            WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='app_logo']")))

            assert inventory.siteTitle() == "Swag Labs"
            assert inventory.pageTitle() == "Products"
        except Exception as e:
            assert False

    cartCheck = {}

    with allure.step("Add products to cart"):
        for item in itemList.keys():
            match addToCartMethod[item]:
                case AddToCartMethods.detailsPage:
                    with allure.step(f"Add {item} to cart from its details page"):
                        inventory.goToPage(item)
                        details.addToCart()
                        details.backToProducts()

                case AddToCartMethods.inventoryPage:
                    with allure.step(f"Add {item} to cart from inventory page"):
                        inventory.addToCart(item)

                case _:
                    pass
            
            cartCheck[item] = False

    with allure.step("Remove items from cart"):
        for item in itemList.keys():
            match removeFromCartMethod[item]:
                case RemoveFromCartMethods.detailsPage:
                    with allure.step(f"Remove {item} from cart through its details page"):
                        inventory.goToPage(item)
                        details.removeFromCart()
                        details.backToProducts()

                case RemoveFromCartMethods.inventoryPage:
                    with allure.step(f"Remove {item} from cart through inventory page"):
                        inventory.removeFromCart(item)

                case RemoveFromCartMethods.cartPage:
                    with allure.step(f"Remove {item} from cart through cart page"):
                        navbar.goToCart()
                        cart.removeItemFromCart(item)                    
                        cart.continueShopping()
                    
                case _:
                    pass        

    with allure.step("Check if the cart contains the expected items"):
        navbar.goToCart()

        for item in itemList:
            cartCheck[item] = cart.itemIsInCart(item)

        assert cartCheck == itemList