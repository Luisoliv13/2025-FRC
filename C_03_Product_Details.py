def num_check(question, num_type="float"):
    """Checks that response is a float / integer more than zero"""

    if num_type == "float":
        error = "Please enter a number more than 0."
    else:
        error = "Please enter an integer more than 0."

    while True:
        try:

            if num_type == "float":
                response = float(input(question))
            else:
                response = int(input(question))

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


def not_blank(question):
    """Checks user response is not blank"""
    while True:
        response = input(question)

        if response != "":
            return response
        else:
            print("Sorry, this can't be blank.")


# Main Routine goes here

# Loop for testing purposes
while True:
    product_name = not_blank("Product Name: ")
    quantity_made = num_check("Quantity being made: ", "integer")
    print(f"You are making {quantity_made} {product_name}")
    print()
