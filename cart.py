def add_to_cart(cart, product):
    cart.append(product)
    return cart

cart = []
print(add_to_cart(cart, "Laptop"))
