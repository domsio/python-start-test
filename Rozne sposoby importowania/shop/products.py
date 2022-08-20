products = {
    "chleb": {
        "quantity": 100,
        "price": 3.5
    },
    "jabłka": {
        "quantity": 50,
        "price": 3.2
    },
    "maslo": {
        "quantity": 70,
        "price": 5.1
    },
    "jajko": {
        "quantity": 220,
        "price": 0.5
    },
}


def update_product_quantity(product_name, ordered_quantity):
    products[product_name]["quantity"] -= ordered_quantity
