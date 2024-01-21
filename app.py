import streamlit as st
import pandas as pd

# Load the data from the Excel file
file_path = 'nifty_oi_data.xlsx'
df = pd.read_excel(file_path)

# Define the new market interpretation based on the given criteria
interpretation_dict = {
    ('Positive', 'Positive'): 'Strong bullish trend; new money entering market',
    ('Positive', 'Negative'): 'Potential bearish divergence; watch for reversal',
    ('Negative', 'Positive'): 'Strong bearish trend; aggressive selling',
    ('Negative', 'Negative'): 'Potential bullish divergence; watch for reversal',
    ('Positive', 'Below 1%'): 'Bullish sentiment; existing trend likely to continue',
    ('Negative', 'Below 1%'): 'Bearish sentiment; existing trend likely to continue',
    ('Positive', 'NoChange'): 'Bullish consolidation; potential for a breakout',
    ('Negative', 'NoChange'): 'Bearish consolidation; potential for a breakdown',
    ('NoChange', 'Positive'): 'Market indecision; potential for a breakout',
    ('NoChange', 'Negative'): 'Market indecision; potential for a breakout',
    ('NoChange', 'NoChange'): 'Lack of conviction; monitor other indicators',
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

# Get the Chge and Open Interest Change values for the selected stock
chge_percent = selected_data['Chge'].iloc[0]
open_interest_change = selected_data['Open Interest Change'].iloc[0]

# Get the market interpretation based on Chge and Open Interest Change
interpretation = interpretation_dict.get((chge_percent, open_interest_change), 'Not available')

# Display the market interpretation
st.write(f"Market Interpretation: {interpretation}")
