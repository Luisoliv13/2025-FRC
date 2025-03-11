
def yes_no_check(question):
    """Checks that users enter yes / no / y / n"""

    while True:

        response = input(question).lower()

        if response == "y" or response == "yes":
            return "yes"
        elif response == "n" or response == "no":
            return "no"

        print(f"Please answer yes / no (y / n)")


# Main routine goes here

# Loop for testing purposes
while True:
    want_instructions = yes_no_check("Do you want to see the instructions? ")
    print(f"You chose {want_instructions}")
