import streamlit as st
import pandas as pd

# Load the data
file_path = 'nifty_oi_data.xlsx'
df = pd.read_excel(file_path)

# Sidebar
st.sidebar.title("Nifty OI Analysis")
selected_stock = st.sidebar.selectbox("Select Stock", df['Symbol'].unique())

# Filter data based on selected stock
selected_stock_data = df[df['Symbol'] == selected_stock]

# Main content
st.title(f"Trend Analysis for {selected_stock}")

# Display the selected stock data
st.write(selected_stock_data)

# Display the trend for the selected stock
st.subheader("Trend:")
st.write(selected_stock_data['Trend'].iloc[0])
