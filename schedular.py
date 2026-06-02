from database import get_all_products
from database import add_price_history
from amazon_tracker import amazon_parser

def main():
        products = get_all_products()

        for product in products:

            product_id = product[0]
            product_url = product[2]

            try:

                product_price, product_name = amazon_parser(
                    product_url
                )

                add_price_history(
                    product_id,
                    product_price
                )

                print(
                    f"Updated {product_name}"
                )

            except Exception as e:

                print(
                    f"Failed for {product_url}"
                )

                print(e)

            product_price, product_name = amazon_parser(product_url)
            target_price = product[4]

            if product_price <= target_price:
                print(
                    f"ALERT! {product_name}"
                )

                print(
                    f"Current: ₹{product_price}"
                )

                print(
                    f"Target : ₹{target_price}"
                )

if __name__ == "__main__":
    main()