# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 18:43:07 2022

@author: arezz
"""

import pandas as pd
pd.set_option('display.max_columns', 500)
orders = pd.read_csv("orders_dataset.csv")

orders


orders.info()

dates = ["order_purchase_timestamp", "order_approved_at","order_delivered_carrier_date","order_delivered_customer_date","order_estimated_delivery_date"]

orders[dates] = pd.to_datetime(orders[dates].stack()).unstack()


orders["On Time"] = orders["order_estimated_delivery_date"] > orders["order_delivered_customer_date"]
orders["Estimated Time to Deliver"] = orders["order_estimated_delivery_date"]  - orders["order_purchase_timestamp"] 
orders["Estimated Days to Deliver"] = (orders["order_estimated_delivery_date"]  - orders["order_purchase_timestamp"] ).dt.days

orders["Estimated Days to Deliver"].plot.hist(bins=50)

order

orders.head()
