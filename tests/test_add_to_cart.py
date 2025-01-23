import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

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
    login = LoginPage(browser)
    inventory = InventoryPage(browser)
    navbar = NavBar(browser)
    cart = CartPage(browser)
    details = ItemDetailsPage(browser)
    
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

    cartCheck = {}

    for item in itemList.keys():
        print(f"Adding {item} to cart...")

        match addToCartMethod[item]:
            case AddToCartMethods.detailsPage:
                inventory.goToPage(item)
                print(f"Entering {item}'s description page...")

                details.addToCart()
                print(f"Adding {item} to the cart...")

                details.backToProducts()
                print(f"Returning to 'Products' page...")
            
            case AddToCartMethods.inventoryPage:
                inventory.addToCart(item)
                print(f"Adding {item} to cart from inventory page...")
            
            case _:
                pass
        
        cartCheck[item] = False

    for item in itemList.keys():
        match removeFromCartMethod[item]:
            case RemoveFromCartMethods.detailsPage:
                print(f"Removing {item} from cart...")

                inventory.goToPage(item)
                print(f"Entering {item}'s description page.")

                details.removeFromCart()
                print(f"Clicked 'Remove from Cart' button on {item}'s page'.")

                details.backToProducts()
                print("Returning to 'Products' page.")

            case RemoveFromCartMethods.inventoryPage:
                print(f"Removing {item} from cart...")
                inventory.removeFromCart(item)
                print(f"Clicked 'Remove from Cart' button on {item}'s card.")

            case RemoveFromCartMethods.cartPage:
                print(f"Removing {item} from cart...")

                navbar.goToCart()
                print(f"Entering cart page and searching for {item}'s card...")

                cart.removeItemFromCart(item)
                print(f"Clicked 'Remove from Cart' button on {item}'s card.")
                
                cart.continueShopping()
                print("Returning to 'Products' page.")
            
            case _:
                pass        

    navbar.goToCart()

    for item in itemList:
        cartCheck[item] = cart.itemIsInCart(item)

    print(cartCheck)
    print(itemList)

    assert cartCheck == itemList

    print("Assertion Successful")