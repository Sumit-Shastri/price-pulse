"""
//////////////////////////////////////////////////////////////////////
//  Imports
//////////////////////////////////////////////////////////////////////
"""

from api import fetch_data
from bs4 import BeautifulSoup

"""
//////////////////////////////////////////////////////////////////////
//  Methods
//////////////////////////////////////////////////////////////////////
"""

"""
////////////////////////////////////////////////////////////////////
//  Method Name     : amazon_parser()
//  Input           : url           -->     link of product
//  Output          : Integer       -->     fetched real time price
//                                          of product
//  Description     : This function accept url of product , then 
//                    load the webpage and parse the price of
//                    product, And return it.
//  Author          : Sumit Shastri
//  Date            : 12/06/2026
////////////////////////////////////////////////////////////////////
"""

def amazon_parser(url):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Accept-Language": "en-IN,en;q=0.9",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://www.amazon.in/",
    }

    data = fetch_data(url, headers)

    #with open("debug.html", "w") as f:
    #    f.write(data)

    soup = BeautifulSoup(data, 'html.parser')

    # for debugging purpose
    #print(soup.prettify())

    #with open("amazon_site.html", "w") as f:
    #    f.write(soup.prettify())

    price_tag = soup.find(
        "span",
        class_="a-price-whole"
    )

    if price_tag is None:
        raise ValueError(
            "Could not find price on page"
        )

    price = price_tag.get_text()
    actual_price = int(price.replace(",", "").replace(".", ""))

    return actual_price
"""
//////////////////////////////////////////////////////////////////////
//  END
//////////////////////////////////////////////////////////////////////
"""