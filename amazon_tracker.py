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

def amazon_parser(url, target):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Accept-Language": "en-IN,en;q=0.9",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://www.amazon.in/",
    }

    data = fetch_data(url, headers)
    soup = BeautifulSoup(data, 'html.parser')

    # for debugging purpose
    #print(soup.prettify())

    #with open("amazon_site.html", "w") as f:
    #    f.write(soup.prettify())

    price = (soup.find("span", class_="a-price-whole")).get_text()
    actual_price = int(price.replace(",", "").replace(".", ""))

    return actual_price
"""
//////////////////////////////////////////////////////////////////////
//  END
//////////////////////////////////////////////////////////////////////
"""