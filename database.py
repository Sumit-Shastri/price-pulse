import sqlite3

DB_NAME = "price_pulse.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

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