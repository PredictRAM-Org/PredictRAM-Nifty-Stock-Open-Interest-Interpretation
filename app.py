import streamlit as st
import pandas as pd
import plotly.express as px

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

# Check if necessary columns are present
required_columns = ['ExpiryDate', 'Open Interest Change', 'Trend']
missing_columns = [col for col in required_columns if col not in selected_stock_data.columns]

if missing_columns:
    st.warning(f"Missing columns: {missing_columns}. Please check your data.")
else:
    # Display the trend values
    st.subheader(f"Trend values for {selected_stock}:")

    # Show stock symbol, date, and trend values
    trend_values_data = selected_stock_data[['ExpiryDate', 'Trend']].drop_duplicates()
    st.write(trend_values_data)

    # Create a bar chart for each trend value
    for trend_value in trend_values_data['Trend'].unique():
        trend_data = selected_stock_data[selected_stock_data['Trend'] == trend_value]

        try:
            fig = px.bar(
                trend_data,
                x='ExpiryDate',
                y='Open Interest Change',
                title=f"Open Interest Change for {selected_stock} - Trend: {trend_value}",
                labels={'Open Interest Change': 'Change in Open Interest'},
            )

            st.plotly_chart(fig)
        except ValueError as e:
            st.warning(f"Error creating chart: {e}")
