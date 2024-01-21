import streamlit as st
import pandas as pd

# Load the data from the Excel file
file_path = 'nifty_oi_data.xlsx'
df = pd.read_excel(file_path)

# Define the market interpretation based on the given criteria
interpretation_dict = {
    ('Positive', 'Increasing'): 'Strong bullish trend; new money entering market',
    ('Positive', 'Decreasing'): 'Potential bearish divergence; watch for reversal',
    ('Negative', 'Increasing'): 'Strong bearish trend; aggressive selling',
    ('Negative', 'Decreasing'): 'Potential bullish divergence; watch for reversal',
    ('Positive', 'Steady'): 'Bullish sentiment; existing trend likely to continue',
    ('Negative', 'Steady'): 'Bearish sentiment; existing trend likely to continue',
    ('Positive', 'No Change'): 'Bullish consolidation; potential for a breakout',
    ('Negative', 'No Change'): 'Bearish consolidation; potential for a breakdown',
    ('No Change', 'Increasing'): 'Market indecision; potential for a breakout',
    ('No Change', 'Decreasing'): 'Market indecision; potential for a breakout',
    ('No Change', 'No Change'): 'Lack of conviction; monitor other indicators',
}

# Create a Streamlit app
st.title('Nifty OI Data Analysis')

# Create a dropdown to select a stock symbol
selected_stock = st.selectbox('Select a stock symbol:', df['Symbol'].unique())

# Filter the data based on the selected stock
selected_data = df[df['Symbol'] == selected_stock]

# Display the selected stock's data
st.write(f"Data for {selected_stock}:")
st.write(selected_data)

# Get the Chge% and Open Interest Change values for the selected stock
chge_percent = selected_data.iloc[0]['Chge%']
open_interest_change = selected_data.iloc[0]['Open Int Chg']

# Get the market interpretation based on Chge% and Open Interest Change
interpretation = interpretation_dict.get((chge_percent, open_interest_change), 'Not available')

# Display the market interpretation
st.write(f"Market Interpretation: {interpretation}")
