# Alex Villanueva

# this program is designed to read through a csv file containing product data line by line, then that data is added to an inventory dictionary with a product id as the key so that it can display the data neatly, allow shipping to NH, VT, and ME, and update the stock as orders are put through.. giving the customer a shipping cost and grand total at the end 

#ALGORITHM

# define a fx called 'read_inventory' with one param: 'filename'.
    # create an empty dictionary called 'inventory'.
    # try to open the file specified by 'filename':
        # initialize 'line_number' variable to 1.
        # read the first line and remove the newline character.
        # while the line is not empty:
            # split the line into components split by commas.
            # if there are at least 6 elements in 'product_data':
                # extract 'product_id', 'style', 'color', 'size', 'price', and 'stock'.
                # clean up 'style', 'color', and 'size' using 'cleanup' function.
                # store the product details in the 'inventory' dictionary with 'product_id' as the key.
            # increment 'line_number' by 1.
            # read the next line and remove the newline character.
    # if the file is not found, print an error message.
    # return the 'inventory' dictionary.

    # define a fx called 'cleanup' with one param 'w' which is the corresponding string for each product_data index called with cleanup up above.
    # if 'w' is not empty and the last character is a punctuation mark (.,!,?):
        # remove the last character from 'w'.
    # convert 'w' to lowercase and return it.

    # define a fx called 'get_quantity_index' with one param 'quantity'. this is used to break up the different 'categories' of quantity.
    # if quantity is 1, return 0.
    # if quantity is between 2 and 5, return 1.
    # if quantity is between 6 and 10, return 2.
    # if quantity is greater than 10, return 3.

    # define a fx called 'calculate_shipping_cost' with params 'state' and 'total_quantity'.
        # create a dictionary called 'shipping_charges' for each state with corresponding shipping costs based on the quantity indexes 0-3.
        # set 'shipping_index' to the result of 'get_quantity_index(total_quantity)'.
        # return the shipping cost based on 'state' and 'shipping_index'.

    # define a fx called 'process_order' with one param 'inventory'.
    # prompt the user to enter their name.
    # set 'valid_states' to a set containing 'ME', 'VT', 'NH'.
    # prompt the user to enter their state.
    # while the entered state is not in 'valid_states':
        # print "Invalid State. Program is ending."
        # return from the function.

    # initialize 'total_quantity' to 0 and 'total_cost' to 0.0.
    # set 'order_active' to True.

    # while 'order_active' is True:
        # prompt the user to enter a product ID or 'quit' to exit.
        # if the input is 'quit', set 'order_active' to False.
        # else:
        # if the product ID is not in 'inventory':
            # print "Invalid product. {product_id} not found."
        # else:
            # retrieve product details from 'inventory' using the product id.
            # display the product information (style, color, size, price, stock).

            # prompt the user to enter the quantity.
            # if the quantity is greater than stock:
            # print "Stock is not sufficient."
            # else:
            # update 'total_quantity' by adding quantity.
            # reduce stock in 'inventory' by quantity.
            # calculate the cost for the quantity and add it to 'total_cost'.
            # print "Cost: $" followed by the calculated cost to 2 decimals.

    # calculate shipping cost using 'calculate_shipping_cost(state, total_quantity)'.
    # compute grand total as the sum of 'total_cost' and 'shipping_cost'.
    # print "Shipping cost: $" followed by 'shipping_cost'.
    # print "Grand Total: $" followed by 'grand_total'.

    # define the 'main' fx.
    # set 'filename' to "Shirts2.csv".
    # call 'read_inventory' with 'filename' to load the inventory.
    # call 'process_order' with the loaded inventory.



def read_inventory(filename):
    inventory = {}
    try:
        with open(filename, "r") as file:
            line_number = 1 
            line = file.readline().rstrip('\n')
            while line != '':
                product_data = line.strip().split(",")
                if len(product_data) >= 6:
                    product_id = product_data[0].strip()
                    style = cleanup(product_data[1].strip())
                    color = cleanup(product_data[2].strip())
                    size = cleanup(product_data[3].strip())
                    price = float(product_data[4].strip())
                    stock = int(product_data[5].strip())
                    # Store the product details in the inventory dictionary
                    inventory[product_id] = [style, color, size, price, stock]
                line_number += 1
                line = file.readline().rstrip('\n')  # Read the next line
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    return inventory


def cleanup(w):
    # Remove trailing punctuation (i just included the cleanup fx for practice of the lecture material you showed in the code demo although it's not necessary for this program)
    if w and w[-1] in ['.', ',', '!', '?']:
        w = w[:-1]
    return w.lower()


def get_quantity_index(quantity):
    if quantity == 1:
        return 0
    elif 2 <= quantity <= 5:
        return 1
    elif 6 <= quantity <= 10:
        return 2
    else:
        return 3 


def calculate_shipping_cost(state, total_quantity):
    shipping_charges = {
        "ME": [5.00, 7.50, 10.00, 12.75],
        "VT": [4.50, 7.00, 11.75, 12.50],
        "NH": [3.75, 5.50, 10.25, 11.75],
    }

    shipping_index = get_quantity_index(total_quantity)
    return shipping_charges[state][shipping_index]


def process_order(inventory):
    print()
    customer_name = input("Enter customer name: ")
    # Loop until a valid state is entered
    valid_states = {"ME", "VT", "NH"}
    state = input("Enter state (ME, VT, NH): ").strip().upper() #to make up for whitespace and not be case-sensitive
    print()
    if state not in valid_states: #exit the program if states that aren't VT, NH, or ME are entered
        print("Invalid State. Program is ending.")
        return

    # Set total_quantity and total_cost to 0.
    total_quantity = 0
    total_cost = 0.0 

    # Set order_active flag to True (it will turn false when the user decides to end the order)
    order_active = True

    while order_active:
        product_id = input("Enter product id (quit to end): ").strip()

        if product_id.lower() == "quit":
            order_active = False
        else:
            if product_id not in inventory:
                print(f"Invalid product. {product_id} not found.")
                print()
            else:
                # Retrieve product details
                product_details = inventory[product_id]
                style, color, size, price, stock = product_details

                # Display product information
                print()
                print("-" * 60)
                print(
                    f"{'Style':<15}{'Color':<10}{'Size':<10}{'Unit Price':<15}{'Stock':<10}"
                )
                print(f"{style:<15}{color:<10}{size:<10}{price:<15.2f}{stock:<10}")
                print("-" * 60)
                # Ask for quantity
                print()
                quantity = int(input("Enter quantity: "))
                if quantity <= stock:
                    # Update total quantity and stock
                    total_quantity += quantity
                    stock -= quantity
                    inventory[product_id][4] = stock  # Update stock in the dictionary

                    # Calculate cost
                    cost = quantity * price
                    total_cost += cost
                    print()
                    print(f"Cost: ${cost:.2f}")
                    print()
                else:
                    print()
                    print("Stock is not sufficient.")

    # Calculate shipping cost
    shipping_cost = calculate_shipping_cost(state, total_quantity)

    # Compute grand total
    grand_total = total_cost + shipping_cost
    print()
    print(f"Shipping cost: ${shipping_cost:.2f}")
    print(f"Grand Total: ${grand_total:.2f}")


def main():
    # the filename is specified instead of how it's normally asked for according to the specs of this assignment
    filename = "Shirts2.csv" 
    inventory = read_inventory(filename) 
    process_order(inventory)  # Process the customer's order


# Run the main function
if __name__ == "__main__":
    main()
