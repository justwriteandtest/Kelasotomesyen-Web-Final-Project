from const.inventory import ItemCodes

class Locator:
    appLogoXPath = "//div[@class='app_logo']"
    pageTitleXPath = "//span[@class='title']"

    buttonAddItemToCart = {
        ItemCodes.itemBackpack: "//button[@id='add-to-cart-sauce-labs-backpack']",
        ItemCodes.itemBikeLight: "//button[@id='add-to-cart-sauce-labs-bike-light']",
        ItemCodes.itemBoltTShirt: "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']",
        ItemCodes.itemFleeceJacket: "//button[@id='add-to-cart-sauce-labs-fleece-jacket']",
        ItemCodes.itemOnesie: "//button[@id='add-to-cart-sauce-labs-onesie']",
        ItemCodes.itemTestAllTheThingsTShirt: "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']",
    }

    buttonRemoveItemFromCart = {
        ItemCodes.itemBackpack: "//button[@id='remove-sauce-labs-backpack']",
        ItemCodes.itemBikeLight: "//button[@id='remove-sauce-labs-bike-light']",
        ItemCodes.itemBoltTShirt: "//button[@id='remove-sauce-labs-bolt-t-shirt']",
        ItemCodes.itemFleeceJacket: "//button[@id='remove-sauce-labs-fleece-jacket']",
        ItemCodes.itemOnesie: "//button[@id='remove-sauce-labs-onesie']",
        ItemCodes.itemTestAllTheThingsTShirt: "//button[@id='remove-test.allthethings()-t-shirt-(red)']",
    }

    imageItemLink = {
        ItemCodes.itemBackpack: "//a[@id='item_4_img_link']",
        ItemCodes.itemBikeLight: "//a[@id='item_0_img_link']",
        ItemCodes.itemBoltTShirt: "//a[@id='item_1_img_link']",
        ItemCodes.itemFleeceJacket: "//a[@id='item_5_img_link']",
        ItemCodes.itemOnesie: "//a[@id='item_2_img_link']",
        ItemCodes.itemTestAllTheThingsTShirt: "//a[@id='item_3_img_link']",
    }

    textItemLink = {
        ItemCodes.itemBackpack: "//a[@id='item_4_title_link']",
        ItemCodes.itemBikeLight: "//a[@id='item_0_title_link']",
        ItemCodes.itemBoltTShirt: "//a[@id='item_1_title_link']",
        ItemCodes.itemFleeceJacket: "//a[@id='item_5_title_link']",
        ItemCodes.itemOnesie: "//a[@id='item_2_title_link']",
        ItemCodes.itemTestAllTheThingsTShirt: "//a[@id='item_3_title_link']",
    }

    selectSortXPath = "//select[@class='product_sort_container']"
    selectSortValueAZ = "az"
    selectSortValueZA = "za"
    selectSortValueLoHi = "lohi"
    selectSortValueHiLo = "hilo"