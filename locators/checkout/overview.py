from const.inventory import ItemCodes

class Locator:
    buttonCancelXPath = "//button[@id='cancel']"
    buttonFinishXPath = "//button[@id='finish']"

    textItemLinkXPath = {
        ItemCodes.itemBackpack: "//a[@id='item_4_title_link']",
        ItemCodes.itemBikeLight: "//a[@id='item_0_title_link']",
        ItemCodes.itemBoltTShirt: "//a[@id='item_1_title_link']",
        ItemCodes.itemFleeceJacket: "//a[@id='item_5_title_link']",
        ItemCodes.itemOnesie: "//a[@id='item_2_title_link']",
        ItemCodes.itemTestAllTheThingsTShirt: "//a[@id='item_3_title_link']",
    }

    # Also usable in cart page
    textItemPriceXPath = "{}/../div[@class='item_pricebar']/div[@data-test='inventory-item-price']"
    textItemQtyXPath = "{}/../../div[@class='cart_quantity']"