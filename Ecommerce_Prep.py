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


orders["on_time"] = orders["order_estimated_delivery_date"] > orders["order_delivered_customer_date"]
orders["estimated_time_to_deliver"] = orders["order_estimated_delivery_date"]  - orders["order_purchase_timestamp"] 
orders["estimated_days_to_deliver"] = (orders["order_estimated_delivery_date"]  - orders["order_purchase_timestamp"] ).dt.days

orders["delivery_time_category"] = pd.qcut(orders["estimated_days_to_deliver"], 5, labels=["Very Short", "Short", "Normal", "Long","Very Long"])

orders.to_csv("orders_dataset_new.csv")
