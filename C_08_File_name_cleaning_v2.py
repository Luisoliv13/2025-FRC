def clean_filename(raw_filename):
    """Check filename has not illegal characters and is not too long"""

    # assume filename is OK
    valid_filename = True
    error = ""

    while True:

        # replace spaces with underscores
        raw_filename = raw_filename.replace(" ", "_")

        # check for valid length
        if len(raw_filename) >= 20:
            valid_filename = False
            error = ("Oops - your product name / filename is too long.  \n"
                     "Please provide an alternate filename (<= 19 characters) \n"
                     "or press <enter> to default to FRC_yyyy_mm_ddd")

        # iterate through filename and check for invalid characters
        for letter in raw_filename:
            if letter.isalnum() is False and letter != "_":
                valid_filename = False
                error = ("I can't use the product name / proposed filename \n"
                         "as it has illegal characters.  Please \n"
                         "enter an alternate name for the first part \n"
                         "of the file or press <enter> to default to FRC_yyyy_mm_dd")
                break

        if valid_filename is False:
            print(error)
            raw_filename = input("\nPlease enter an alternate name for the start of the file: ")

            # reset valid_filename so that it new name can be checked.
            valid_filename = True

            # put in default filename if users press <enter>
            if raw_filename == "":
                raw_filename = "FRC"

        else:
            return raw_filename



while True:
    product_name = input("Product Name: ")
    clean_product_name = clean_filename(product_name)

    print(f"The original product name was {product_name}.  \n"
          f"The clean version is {clean_product_name}")
    print()
