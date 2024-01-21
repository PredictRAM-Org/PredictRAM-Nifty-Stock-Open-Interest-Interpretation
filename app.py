import streamlit as st
import pandas as pd

# Load data from Excel file
excel_file = 'nifty_oi_data.xlsx'
df = pd.read_excel(excel_file)

# Sidebar to select stocks
selected_stocks = st.sidebar.multiselect('Select Stocks', df['Symbol'].unique())

# Filter data based on selected stocks
filtered_df = df[df['Symbol'].isin(selected_stocks)]

# Line chart to display trend
st.line_chart(filtered_df.set_index('Date')['Open Interest'])

# Display the selected data
st.write("Selected Data:")
st.write(filtered_df)
