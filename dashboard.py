import streamlit as st
import pandas as pd
import plotly.express as px
import os

@st.cache_data
def load_data():
    csv_path = os.path.join(os.path.dirname(__file__), 'expenses.csv')
    if os.path.exists('csv_path'):
        df = pd.read_csv('csv_path')
        df['date'] = pd.to_datetime(df['date'])
        return df
    return pd.DataFrame()

st.title("💰 Expense Dashboard")

df = load_data()

if df.empty:
    st.warning("No data found. Run the CLI first to add expenses!")
    st.stop()


col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Spent", f"${df['amount'].sum():.2f}")
with col2:
    st.metric("Total Transactions", len(df))
with col3:
    st.metric("Average Expense", f"${df['amount'].mean():.2f}")

# Charts
st.subheader("Spending by Category")
category_data = df.groupby('category')['amount'].sum().reset_index()
bar_chart = px.bar(category_data, x='category', y='amount', 
                   title="Total by Category")
st.plotly_chart(bar_chart)

# Pie chart
pie_chart = px.pie(category_data, values='amount', names='category',
                   title="Expense Distribution")
st.plotly_chart(pie_chart)

# Time series
st.subheader("Expenses Over Time")
daily_expenses = df.groupby('date')['amount'].sum().reset_index()
line_chart = px.line(daily_expenses, x='date', y='amount',
                     title="Daily Spending")
st.plotly_chart(line_chart)

# Data table
st.subheader("Recent Expenses")
st.dataframe(df.sort_values('date', ascending=False).head(10))
