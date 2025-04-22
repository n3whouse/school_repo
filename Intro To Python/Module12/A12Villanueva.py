# Alex Villanueva

# this snow globe shipping calculator helps figure the total cost of packaging and shipping differently sized snow globes. users can choose from three different snow globe sizes, input custom shipping box dimensions (so long as they're larger than the snow globe), and automatically calculates snow globes' base cost -- along with shipping box, packing material, and plastic wrap costs as constants. it ensures the snow globes are packaged properly (box size > snow globe size) with data validation and then spits out a detailed summary

# NOTE: my last two submissions i was trying to write the algorithm beforehand in the same fashion as your Code Demos, and i think writing per function pseudo is the cleaner and less confusing way to do it so i don't get lost in the reeds when i go to write my code and do things backwards. writing the whole algorithm out doesn't help me as much as taking it fx by fx

from box import Box

# first we establish constants for wrap, box, and packing costs
PACKING_COST = 0.0023  # per in^3
PLASTIC_WRAP_COST = 0.0008  # per in^2
BOX_COST = 5.00  # each

# then we initialize a dictionary to hold the keys (1,2,3) and each value is actually one nested dictionary per key, each containing a tuple for shipping dimensions and floating-integer shipping prices
SHIPPING_OPTIONS = {
    1: {"dimensions": (4, 4, 3), "price": 5.99},
    2: {"dimensions": (6, 6, 5), "price": 9.99},
    3: {"dimensions": (10, 6, 8), "price": 13.99},
}


# display_menu, well.. displays menu. each accesses the SHIPPING OPTIONS dictionary by the choice key and then the "price" key in the corresponding nested dictionary to make the code dynamic
def display_menu():
    print()
    print("Snow Globe Options: ")
    print(f"1. Dimensions 4x4x3 - ${SHIPPING_OPTIONS[1]['price']}")
    print(f"2. Dimensions 6x6x5 for ${SHIPPING_OPTIONS[2]['price']}")
    print(f"3. Dimensions 10x6x8 for ${SHIPPING_OPTIONS[3]['price']}")
    print()


# handles snow globe choice with data validation; fx returns user input value. first, choice is initialized holding default 0 value. then, since choice's default is < 1, the while loop begins. the try asks for usr input. IF input = 1-3, the loop conditions have been met and the loop stops. if not, "invalid choice" error is printed. if a non-integer is entered, we move to the except logic, print our custom ValueError, reset choice to default 0, and return it.
def handle_snow_globe_choice():
    choice = 0
    while not 1 <= choice <= 3:
        try:
            choice = int(input("Enter your choice of snow globe (1-3): "))
            if not 1 <= choice <= 3:
                print("Invalid choice. Please choose either 1, 2, or 3.")
        except ValueError:
            print("Please enter a valid integer")
            choice = 0
    return choice


# pretty self explanatory: we're taking in the globe based on user choice, initializing a default 0 value and a Boolean 'valid' flag, activating the loop on execution. the loop goes to the try, takes in dimension (cubic) and checks if the cubic dimension is big enough to fit the chosen globe's length, width, and height. if it does, the loop's conditions are fulfilled and the dimension is returned. IF dimension is not valid, throw a "too small" error and activate the loop again, and same with ValueError in except
def get_shipping_dimension(snow_globe):
    dimension = 0
    valid = False
    while not valid:
        try:
            dimension = int(input("Enter shipping box dimension: "))

            valid = (
                dimension >= snow_globe.get_length()
                and dimension >= snow_globe.get_width()
                and dimension >= snow_globe.get_height()
            )
            if not valid:
                print("Shipping box too small")
                valid = False
        except ValueError:
            print("Please enter a valid integer.")
            valid = False
    return dimension


# BEGIN MAIN
def main():
    print("\nSnow Globe Shipping Calculator")  # calculator title
    print("=" * 30)  # nice double line to make it look good

    # display the menu, get the choice, and craft the Box object. the value returned by handle_snow_globe_choice is saved as choice. then we go into SHIPPING OPTIONS at the user entered (1-3) key, save the corresponding nested dictionary as globe data, and then construct a Box and pass the value of the "dimensions" key of globe_data and save it as the snow globe. the "price" key of the same nested dictionary is accessed and saved as the globe price.
    display_menu()
    choice = handle_snow_globe_choice()
    globe_data = SHIPPING_OPTIONS[choice]
    snow_globe = Box(*globe_data["dimensions"])
    globe_price = globe_data["price"]

    # now that the dimensions and price are worked out, calculate the shipping dimensions of the selected globe, along with the value o
    shipping_dimension = get_shipping_dimension(snow_globe)
    shipping_box = Box(shipping_dimension, shipping_dimension, shipping_dimension)

    # cost calculators -- get the  remaining volume in the box by finding diff between box volume and globe volume, calculate that * the packing cost constant and assign it to a variable packing_cost, and find the wrap cost my multiplying the constant value for it by the shipping_box surface_area (method). once all of these have been accounted for, put them together + the BOX_COST to get total cost.
    packing_volume = shipping_box.volume() - snow_globe.volume()
    packing_cost = packing_volume * PACKING_COST
    wrap_cost = shipping_box.surface_area() * PLASTIC_WRAP_COST
    total_cost = BOX_COST + packing_cost + wrap_cost + globe_price

    # now all the costs, dimensions, and prices are calculated; the choice is assigned and the last step is displaying the results in an order summary
    print()
    print("Order Summary: ")
    print("=" * 50)
    print(f"{'Item':<20}{'Dimensions':<15}{'Cost':>10}")
    print(
        "-" * 50
    )  # for some dynamic lines to make this look like a real program and separate title and headers from data
    print(
        f"{'Snow Globe':<20}{f'{snow_globe.get_length()}x{snow_globe.get_width()}x{snow_globe.get_height()}':<15} ${globe_price:>9.2f}"
    )
    print(
        f"{'Shipping Box':<20}{f'{shipping_box.get_length()}x{shipping_box.get_width()}x{shipping_box.get_height()}':<15} ${BOX_COST:>9.2f}"
    )
    print(f"{'Packing Materials':<20}{'':<15} ${packing_cost:>9.2f}")
    print(f"{'Plastic Wrap':<20}{'':<15} ${wrap_cost:>9.2f}")
    print("-" * 50)
    print(f"{'Total:':<20}{'':<15} ${total_cost:>9.2f}")


if __name__ == "__main__":
    main()
