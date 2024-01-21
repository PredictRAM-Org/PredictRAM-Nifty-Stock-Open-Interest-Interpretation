import streamlit as st
import pandas as pd

# Load data from Excel file
excel_file = 'nifty_oi_data.xlsx'
try:
    df = pd.read_excel(excel_file)
except FileNotFoundError:
    st.error(f"Error: File '{excel_file}' not found. Please check the file path.")
    st.stop()

# Sidebar to select stocks
selected_stocks = st.sidebar.multiselect('Select Stocks', df['Symbol'].unique())

# Filter data based on selected stocks
filtered_df = df[df['Symbol'].isin(selected_stocks)]

# Check if 'Expiry Date' column exists
if 'Expiry Date' not in filtered_df.columns:
    st.error("Error: 'Expiry Date' column not found in the selected data. Please check the data structure.")
    st.stop()

# Line chart to display trend
st.line_chart(filtered_df.set_index('ExpiryDate')['Open Interest'])

# Display the selected data
st.write("Selected Data:")
st.write(filtered_df)
