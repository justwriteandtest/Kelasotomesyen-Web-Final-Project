from const.inventory import ItemCodes
from const.cart import AddToCartMethods
from const.cart import RemoveFromCartMethods

endToEndData = [
    (
        {
            ItemCodes.itemBackpack: True,
            ItemCodes.itemBikeLight: True,
            ItemCodes.itemBoltTShirt: True,
            ItemCodes.itemFleeceJacket: True,
            ItemCodes.itemOnesie: True,
            ItemCodes.itemTestAllTheThingsTShirt: True,
        }, 
        {
            ItemCodes.itemBackpack: AddToCartMethods.detailsPage,
            ItemCodes.itemBikeLight: AddToCartMethods.inventoryPage,
            ItemCodes.itemBoltTShirt: AddToCartMethods.inventoryPage,
            ItemCodes.itemFleeceJacket: AddToCartMethods.detailsPage,
            ItemCodes.itemOnesie: AddToCartMethods.detailsPage,
            ItemCodes.itemTestAllTheThingsTShirt: AddToCartMethods.detailsPage,
        }, 
        {
            ItemCodes.itemBackpack: RemoveFromCartMethods.doNotRemove,
            ItemCodes.itemBikeLight: RemoveFromCartMethods.doNotRemove,
            ItemCodes.itemBoltTShirt: RemoveFromCartMethods.doNotRemove,
            ItemCodes.itemFleeceJacket: RemoveFromCartMethods.doNotRemove,
            ItemCodes.itemOnesie: RemoveFromCartMethods.doNotRemove,
            ItemCodes.itemTestAllTheThingsTShirt: RemoveFromCartMethods.doNotRemove,
        }, 
        "Michael",
        "Sanders",
        "12345"
    ),
    (
        {
            "": False,
        },{
            "": AddToCartMethods.doNotAdd,
        },{
            "": RemoveFromCartMethods.doNotRemove
        },
        "Emily",
        "Bateman",
        "234512"
    ),
    (
        {
            ItemCodes.itemBackpack: True,
            ItemCodes.itemBikeLight: True,
            ItemCodes.itemBoltTShirt: True,
            ItemCodes.itemFleeceJacket: False,
            ItemCodes.itemOnesie: False,
            ItemCodes.itemTestAllTheThingsTShirt: False,
        }, 
        {
            ItemCodes.itemBackpack: AddToCartMethods.detailsPage,
            ItemCodes.itemBikeLight: AddToCartMethods.inventoryPage,
            ItemCodes.itemBoltTShirt: AddToCartMethods.inventoryPage,
            ItemCodes.itemFleeceJacket: AddToCartMethods.detailsPage,
            ItemCodes.itemOnesie: AddToCartMethods.detailsPage,
            ItemCodes.itemTestAllTheThingsTShirt: AddToCartMethods.detailsPage,
        }, 
        {
            ItemCodes.itemBackpack: RemoveFromCartMethods.doNotRemove,
            ItemCodes.itemBikeLight: RemoveFromCartMethods.doNotRemove,
            ItemCodes.itemBoltTShirt: RemoveFromCartMethods.doNotRemove,
            ItemCodes.itemFleeceJacket: RemoveFromCartMethods.detailsPage,
            ItemCodes.itemOnesie: RemoveFromCartMethods.cartPage,
            ItemCodes.itemTestAllTheThingsTShirt: RemoveFromCartMethods.inventoryPage,
        }, 
        "John",
        "Paxton",
        "24231"
    ),
]