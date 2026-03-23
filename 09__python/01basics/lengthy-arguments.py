# Variable lenght argument (Non keyword argument)
def order_food(min_order, *items):
    print("You have ordered: ", min_order)
    print(items)  # its a tuple
    for item in items:
        print(item)


order_food("Salad", "pizza", "burger", "biryani", "zinger")
