import streamlit as st
import pandas as pd

# Load data from Excel file
excel_file = 'nifty_oi_data.xlsx'
try:
    df = pd.read_excel(excel_file)
except FileNotFoundError:
    st.error(f"Error: File '{excel_file}' not found. Please check the file path.")
    st.stop()

# Sidebar to select a single stock from dropdown
selected_stock = st.sidebar.selectbox('Select Stock', df['Symbol'].unique())

# Filter data based on selected stock
filtered_df = df[df['Symbol'] == selected_stock]

# Check if 'Expiry Date' column exists
if 'ExpiryDate' not in filtered_df.columns:
    st.error("Error: 'Expiry Date' column not found in the selected data. Please check the data structure.")
    st.stop()

# Line chart to display trend
st.line_chart(filtered_df.set_index('ExpiryDate')['Open Interest'])

# Display the selected data
st.write(f"Trend for {selected_stock}:")
st.write(filtered_df)
