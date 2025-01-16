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