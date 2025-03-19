def clean_filename(product_name):
    """Check filename has not illegal characters and is not too long"""

    while True:

        # replace spaces with underscores
        product_name = product_name.replace(" ", "_")
        print(f"product name without spaces {product_name}")

        if product_name.isalnum() is True and len(product_name) < 20:
            print("we are ok")
            return product_name
        else:
            print("oops")
            product_name = input("Please enter an alternate name for the start of the file: ")



while True:
    product_name = input("Product Name: ")
    clean_product_name = clean_filename(product_name)

    print(f"The original product name was {product_name}.  The clean version is {clean_product_name}")
