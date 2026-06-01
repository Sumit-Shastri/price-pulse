"""
//////////////////////////////////////////////////////////////////////
//  Imports
//////////////////////////////////////////////////////////////////////
"""

import os
from datetime import datetime
import pandas

"""
//////////////////////////////////////////////////////////////////////
//  Method name     : product_price_tracker()
//  input           : product_name         
//                    product_price
//                    target
//                    difference
//  output          : csv file having columns : 1. srno
//                                              2. date
//                                              3. day
//                                              4. time
//                                              5. product price
//                                              6. difference from target price
//                                              7. target price
// description      : This method accepts current product price from
//                    price fetcher methods (eg. amazon_tracker) and
//                    generates a csv file for the particular product
//                    ,which has above given fields.This csv file can 
//                    later used for price tracking and data visualization.
// Author           : Sumit Shastri
// Date             : 01/06/2026
//////////////////////////////////////////////////////////////////////
"""

def product_price_tracker(product_name,
                          product_price,
                          target = None
                         ):
    filename = f"{product_name}.csv"

    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d")
    current_day = now.strftime("%A")
    current_time = now.strftime("%H:%M:%S")

    # If File doesnt exists
    if not os.path.exists(filename):

        if target is None:
            raise ValueError("Target price is required.")

        difference = product_price - target

        df = pandas.DataFrame([{
            "srno" : 1,
            "date" : current_date,
            "day" : current_day,
            "time" : current_time,
            "product_price" : product_price,
            "difference" : difference,
            "target" : target
        }])

        df.to_csv(filename, index = False)

        print(f"{filename} created successfully .")

    # File already exists

    else:

        df = pandas.read_csv(filename)

        target = df.iloc[0]['target']
        difference = product_price - target

        new_row = {
            "srno" : len(df) + 1,
            "date" : current_date,
            "day" : current_day,
            "time" : current_time,
            "product_price" : product_price,
            "difference" : difference,
            "target" : target
        }

        df.loc[len(df)] = new_row
        df.to_csv(filename, index = False)

        print(f"New entry added to {filename}.")

"""
//////////////////////////////////////////////////////////////////////
//  END
//////////////////////////////////////////////////////////////////////
"""