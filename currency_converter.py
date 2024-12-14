# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 03:12:58 2024

@author: aoa
"""

import requests

def convert_usd_to_inr(amount_in_usd):
    # Replace 'YOUR_API_KEY' with your actual API key
    api_url = "https://api.currencyfreaks.com/v2.0/rates/latest?apikey=c05dad7d1d474d43b92b949259f0c2d1"
    
    try:
        response = requests.get(api_url)
        data = response.json()
        
        # Get the conversion rate from USD to INR
        usd_to_inr_rate = float(data['rates']['INR'])
        
        # Convert the amount
        amount_in_inr = amount_in_usd * usd_to_inr_rate
        return amount_in_inr
    
    except Exception as e:
        print("Error:", e)
        return None

# Example Usage
usd_amount = float(input("Enter the USD amount: "))  # Replace with the amount in USD
inr_amount = convert_usd_to_inr(usd_amount)
if inr_amount:
    print(f"${usd_amount} USD is approximately ₹{inr_amount:.2f} INR.")
