import streamlit as st
from itables.streamlit import interactive_table
import pandas as pd
import requests
from datetime import datetime, timedelta

# Define today's date range in UTC
today = datetime.utcnow().date()
period_from = f"{today}T00:00Z"
period_to = f"{today + timedelta(days=1)}T00:00Z"

# API endpoint with specified date range
url = f"https://api.octopus.energy/v1/products/AGILE-18-02-21/electricity-tariffs/E-1R-AGILE-18-02-21-B/standard-unit-rates/?period_from={period_from}&period_to={period_to}"

# Fetching data
response = requests.get(url)
data = response.json()

# Extracting today's prices into a DataFrame
prices_today = [(entry['valid_from'], entry['value_inc_vat']) for entry in data['results']]
df = pd.DataFrame(prices_today, columns=["Time", "Price (p/kWh)"])

# Display the interactive table
st.title("Today's Agile Tariff Prices")
interactive_table(df)
