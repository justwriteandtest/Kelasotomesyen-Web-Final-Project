from const.inventory import ItemCodes

class Locator:
    buttonContinueShoppingXPath = "//button[@id='continue-shopping']"
    buttonCheckoutXPath = "//button[@id='checkout']"

    buttonRemoveFromCart = {
        ItemCodes.itemBackpack : "//button[@id='remove-sauce-labs-backpack']",
        ItemCodes.itemBikeLight : "//button[@id='remove-sauce-labs-bike-light']",
        ItemCodes.itemBoltTShirt : "//button[@id='remove-sauce-labs-bolt-t-shirt']",
        ItemCodes.itemFleeceJacket : "//button[@id='remove-sauce-labs-fleece-jacket']",
        ItemCodes.itemTestAllTheThingsTShirt : "//button[@id='remove-test.allthethings()-t-shirt-(red)']",
        ItemCodes.itemOnesie : "//button[@id='remove-sauce-labs-onesie']",
    }

    textItemLinkXPath = {
        ItemCodes.itemBackpack: "//a[@id='item_4_title_link']",
        ItemCodes.itemBikeLight: "//a[@id='item_0_title_link']",
        ItemCodes.itemBoltTShirt: "//a[@id='item_1_title_link']",
        ItemCodes.itemFleeceJacket: "//a[@id='item_5_title_link']",
        ItemCodes.itemOnesie: "//a[@id='item_2_title_link']",
        ItemCodes.itemTestAllTheThingsTShirt: "//a[@id='item_3_title_link']",
    }

    textItemPriceXPath = "{}/../div[@class='item_pricebar']/div[@data-test='inventory-item-price']"
    textItemQtyXPath = "{}/../../div[@class='cart_quantity']"