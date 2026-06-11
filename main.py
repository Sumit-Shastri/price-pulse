"""
//////////////////////////////////////////////////////////////////////
//  Imports
//////////////////////////////////////////////////////////////////////
"""

import requests
from amazon_tracker import amazon_parser
from database import initialize_database
from database import add_product
from database import add_price_history
from database import get_product_by_url
from database import get_all_products

"""
//////////////////////////////////////////////////////////////////////
//  Main
//////////////////////////////////////////////////////////////////////
"""

initialize_database()                                       # generates database

print("**********************************")
print("---   Welcome to price-pulse  ---")
print("**********************************\n")

while True:

    menu = """
1. Track product
2. My Watchlist
3. Exit

choose : """

    # Exception handle for choice
    while True:
        try:
            choice = int(input(menu))
            break
        except ValueError:
            print("-----------------------------------")
            print("Error : Excepted number for choice.")
            print("Usage --> e.g  Choose : 2")
            print("-----------------------------------\n")

    if choice == 1:

        print("----------------------------------------------------------------")

        while True:
            try:
                ecommerce_website = int(input("""\nPlease provide which ecommerce site it is ?
                
1. Amazon
2. Flipkart
3. Myntra
4. Meesho
5. Ajio

choose : """))
                break
            except ValueError:
                print("Error : Expected number for choice")

        print("----------------------------------------------------------------\n")
        url = input("Enter the product url : ")
        print("----------------------------------------------------------------\n")

        while True:
            try:
                target = int(input("Enter your target price : "))
                break
            except ValueError:
                print("Target price must be number, eg. 500000")

        print("----------------------------------------------------------------\n")

        while True:
            alias_product_name = input("Enter alias for your product : ")

            if alias_product_name == "":
                print("Name cannot be empty.")
                print("Usage eg. : Fastrack watch 1\n")
            else:
                break

        if ecommerce_website == 1:
            print("===  Amazon  ===")
            try:
                product_price = amazon_parser(url)

                existing_product = get_product_by_url(url)

                if existing_product:

                    product_id = existing_product[0]

                    add_price_history(
                        product_id,
                        product_price
                    )

                else:

                    product_id = add_product(
                        alias_product_name,
                        url,
                        "Amazon",
                        target
                    )

                    add_price_history(
                        product_id,
                        product_price
                    )

                    tracked_products = get_all_products()
                    print("Products in your list : ")
                    for product in tracked_products:
                        print(product)

                print("\n******************************************")
                print(f"Product name : {product_name}")
                print(f"Product price : {product_price}")
                print(f"Your target price : {target}")
                print(f"Current difference : {product_price - target}")
                print("******************************************\n")

            except requests.exceptions.MissingSchema:
                print("Something wrong with the url , try again")
                continue

        elif ecommerce_website == 2:
            print("===  Flipkart ===")
            print("Feature coming soon")

        elif ecommerce_website == 3:
            print("===  Myntra  ===")
            print("Feature coming soon")

        elif ecommerce_website == 4:
            print("===  Meesho  ===")
            print("Feature coming soon")

        elif ecommerce_website == 5:
            print("===  Ajio  ===")
            print("Feature coming soon")

        else:
            print("Incorrect choice try again")

    elif choice == 2:
        print("===  Watchlist  ===\n")
        get_all_products()


    elif choice == 3:
        print("Exiting...")
        break

    else:
        print("Invalid choice.")
"""
//////////////////////////////////////////////////////////////////////
//  END
//////////////////////////////////////////////////////////////////////
"""