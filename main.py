"""
//////////////////////////////////////////////////////////////////////
//  Imports
//////////////////////////////////////////////////////////////////////
"""
import requests
from amazon_tracker import amazon_parser

"""
//////////////////////////////////////////////////////////////////////
//  Main
//////////////////////////////////////////////////////////////////////
"""

print("**********************************")
print("---   Welcome to price-pulse  ---")
print("**********************************")

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

        if ecommerce_website == 1:
            print("===  Amazon  ===")
            try:
                amazon_parser(url, target)
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
        print("Feature coming soon.")

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