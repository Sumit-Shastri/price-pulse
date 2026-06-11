import sqlite3

DB_NAME = "price_pulse.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

"""
////////////////////////////////////////////////////////////////////
//  Method Name     : initialize_database()
//  Input           : None
//  Output          : None
//  Description     : When this function is called, it connects to
//                    the database and creates 2 tables if they 
//                    not exist :
//
//                    (i) products
//                          id              --> Unique id (int)
//                          product_name    --> alias (string)
//                          product_url     --> ecommerce url (url)
//                          website         --> ecommerce brand (string)
//                          target_price    --> price to track (int)
//                          created_at      --> real current time (date and time)
//
//                    (ii) price_history
//                          id              --> id (int)
//                          product_id      --> unique id (int)
//                          product_price   --> price of product (string)
//                          difference      --> product_price - target_price (float)
//                          checked_at      --> record of updating row (date and time)
//
//  Author          : Sumit Shastri
//  Date            : 12/06/2026
////////////////////////////////////////////////////////////////////
"""

def initialize_database():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT NOT NULL,
        product_url TEXT NOT NULL,
        website TEXT NOT NULL,
        target_price INTEGER NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS price_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id INTEGER NOT NULL,
        product_price INTEGER NOT NULL,
        difference INTEGER NOT NULL,
        checked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(product_id)
        REFERENCES products(id)
    )
    """)

    conn.commit()
    conn.close()

"""
////////////////////////////////////////////////////////////////////
//  Method Name     : add_product()
//  Input           : product_name
//                    product_url
//                    website
//                    target_price
//  Output          : Integer (product_id)
//  Description     : This function accepts product_name, product_url
//                    , website, target_price. Connects to the database, 
//                    checks if product already exists in 'products' table
//                    , if not , then it inserts the accepted arguments to 
//                    to the 'products' table by generating a new product_id
//                    for that product.
//  Author          : Sumit Shastri
//  Date            : 12/06/2026
////////////////////////////////////////////////////////////////////
"""

def add_product(
                    product_name,
                    product_url,
                    website,
                    target_price
                ):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT id
    FROM products
    WHERE product_url = ?
                   """, (product_url,))

    if cursor.fetchone():

        conn.close()

        raise ValueError("This product is already being tracked.")

    cursor.execute("""
    INSERT INTO products
   (
       product_name,
       product_url,
       website,
       target_price
   )
    VALUES (?, ?, ?, ?)""",
                   (
                       product_name,
                       product_url,
                       website,
                       target_price
                   ))

    product_id = cursor.lastrowid

    conn.commit()
    conn.close()

    return product_id

"""
////////////////////////////////////////////////////////////////////
//  Method Name     : add_price_history()
//  Input           : product_id
//                    product_price
//  Output          : None
//  Description     : This function accepts product_id and product_price
                      then connects to database and fetch target_price
                      from 'products' table.Then calculates the difference
                      (product_price - target_price) and update it into the 
                      'price_history' table by inserting product_id, product
                      _name, difference.
//  Author          : Sumit Shastri
//  Date            : 12/06/2026
////////////////////////////////////////////////////////////////////
"""

def add_price_history(
                        product_id,
                        product_price
                     ):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT target_price
    FROM products
    WHERE id = ?
                   """, (product_id,))

    result = cursor.fetchone()

    if result is None:
        conn.close()

        raise ValueError("Product not found")

    target_price = result[0]

    difference = (product_price - target_price)

    cursor.execute("""
    INSERT INTO price_history
    (
        product_id,
        product_price,
        difference
    )
    VALUES (?, ?, ?)
                   """, (
        product_id,
        product_price,
        difference
    ))

    conn.commit()
    conn.close()

"""
////////////////////////////////////////////////////////////////////
//  Method Name     : get_product_by_url()
//  Input           : url           -->     link of product
//  Output          : products ( dictionary of given )
//                    id 
//                    product_name 
//                    product_url 
//                    website 
//                    target_price 
//                    created_at
//  Description     : This function accest url of product and
//                    match it in products table of database,
//                    then returns the matched product url details
//                    like id, product_name etc.
//  Author          : Sumit Shastri
//  Date            : 12/06/2026
////////////////////////////////////////////////////////////////////
"""
def get_product_by_url(url):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM products
    WHERE product_url = ?""",
                   (url,))


    product = cursor.fetchone()
    conn.close()

    return product

def get_all_products():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM products""")

    products = cursor.fetchall()
    conn.close()

    return products