class Locator:
    appLogoXPath = "//div[@class='app_logo']"
    pageTitleXPath = "//span[@class='title']"

    divInventoryClassXPath = ""
    buttonAddToCartClassXPath = "//button[@id[starts-with(., 'add-to-cart')]]"
    imageInventoryItemClassXPath = "//img[@class='inventory_item_img']" 
    textInventoryItemClassXPath = "//div[@class='inventory_item_name']"

    buttonAddToCartBackpackXPath = "//button[@id='add-to-cart-sauce-labs-backpack']"
    imageBackpackXPath = "//*[@id='item_4_img_link']"
    textBackpackXPath = "//*[@id='item_4_title_link']"

    buttonAddToCartBikeLightXPath = "//button[@id='add-to-cart-sauce-labs-bike-light']"
    imageBikeLightXPath = "//*[@id='item_0_img_link']"
    textBikeLightXPath = "//*[@id='item_0_title_link']"

    buttonAddToCartBoltTShirtXPath = "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"
    imageBoltTShirtXPath = "//*[@id='item_1_img_link']"
    textBoltTShirtXPath = "//*[@id='item_1_title_link']"
    
    buttonAddToCartJacketXPath = "//button[@id='add-to-cart-sauce-labs-fleece-jacket']"
    imageJacketXPath = "//*[@id='item_5_img_link']"
    textJacketXPath = "//*[@id='item_5_title_link']"

    buttonAddToCartOnesieXPath = "//button[@id='add-to-cart-sauce-labs-onesie']"    
    imageOnesieXPath = "//*[@id='item_2_img_link']"
    textOnesieXPath = "//*[@id='item_2_title_link']"
    
    buttonAddToCartRedTShirtXPath = "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']"
    imageRedTShirtXPath = "//*[@id='item_3_img_link']"
    textRedTShirtXPath = "//*[@id='item_3_title_link']"

    selectSortXPath = "//select[@class='product_sort_container']"
    selectSortValueAZ = "az"
    selectSortValueZA = "za"
    selectSortValueLoHi = "lohi"
    selectSortValueHiLo = "hilo"