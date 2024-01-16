# -*- coding: utf-8 -*-
"""app_dashboard.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MscXyy178oY6aBD8Px4dbhxnDsgmCX96
"""

import pandas as pd
import streamlit as st
import plotly.express as px

# Load your dataset
url = 'https://raw.githubusercontent.com/045051Shalini/Dynamic-plots/main/customer_shopping_data.csv'
df = pd.read_csv(url)

# Sidebar filters
st.sidebar.title("Customer Shopping Insights Dashboard")

# Filter for Gender and Category Analysis
selected_gender_category = st.sidebar.selectbox('Select Gender for Category Analysis:', ['All'] + list(df['gender'].unique()), key='gender_category_selector')
selected_category = st.sidebar.selectbox('Select Category for Category Analysis:', ['All'] + list(df['category'].unique()), key='category_selector')

# Filter data based on selected gender and category
filtered_df_category = df[(df['gender'] == selected_gender_category) | (selected_gender_category == 'All')]
filtered_df_category = filtered_df_category[(filtered_df_category['category'] == selected_category) | (selected_category == 'All')]

# Objective 1: Gender and Age Analysis
fig1_category = px.histogram(
    filtered_df_category,
    x='age',
    color='payment_method',
    marginal='box',
    title='Gender and Age Analysis (Category)',
    labels={'age': 'Age', 'payment_method': 'Payment Method'},
    nbins=20
)

# Objective 2: Payment Method and Age Patterns
fig2_category = px.box(
    filtered_df_category,
    x='payment_method',
    y='age',
    color='payment_method',
    title='Payment Method and Age Patterns (Category)',
    labels={'age': 'Age', 'payment_method': 'Payment Method'}
)

# Objective 3: Category-Specific Analysis
fig3_category = px.histogram(
    filtered_df_category,
    x='age',
    color='category',
    marginal='box',
    title='Category-Specific Analysis',
    labels={'age': 'Age', 'category': 'Category'},
    nbins=20
)

# Display the charts
st.plotly_chart(fig1_category)
st.plotly_chart(fig2_category)
st.plotly_chart(fig3_category)


# Filter for Gender and Payment Method Analysis
selected_gender_payment = st.sidebar.selectbox('Select Gender for Payment Method Analysis:', ['All'] + list(df['gender'].unique()), key='gender_payment_selector')
selected_payment_method = st.sidebar.selectbox('Select Payment Method for Payment Method Analysis:', ['All'] + list(df['payment_method'].unique()), key='payment_method_selector')

# Filter data based on selected gender and payment method
filtered_df_payment = df[(df['gender'] == selected_gender_payment) | (selected_gender_payment == 'All')]
filtered_df_payment = filtered_df_payment[(filtered_df_payment['payment_method'] == selected_payment_method) | (selected_payment_method == 'All')]

# Objective 1: Gender Distribution
fig1_payment = px.pie(
    filtered_df_payment,
    names='gender',
    title='Gender Distribution (Payment Method)',
    labels={'gender': 'Gender'},
)

# Objective 2: Payment Method and Gender Patterns
fig2_payment = px.pie(
    filtered_df_payment,
    names='shopping_mall',
    color='payment_method',
    title='Payment Method and Gender Patterns',
    labels={'shopping_mall': 'Shopping Mall'},
)

# Objective 3: Category-Specific Gender Analysis
fig3_payment = px.pie(
    filtered_df_payment,
    names='shopping_mall',
    color='category',
    title='Category-Specific Gender Analysis',
    labels={'shopping_mall': 'Shopping Mall'},
)

# Display the charts
st.plotly_chart(fig1_payment)
st.plotly_chart(fig2_payment)
st.plotly_chart(fig3_payment)


# Filter data based on selected parameters
selected_date = st.sidebar.select_slider('Select Date:', options=pd.to_datetime(df['invoice_date']).dt.date.unique(), key='date_selector_spending')
selected_gender = st.sidebar.selectbox('Select Gender:', ['All'] + list(df['gender'].unique()), key='gender_selector_spending')
selected_price_range = st.sidebar.slider('Select Price Range:', df['price'].min(), df['price'].max(), (df['price'].min(), df['price'].max()), key='price_range_selector_spending')
selected_category_spending = st.sidebar.selectbox('Select Category:', ['All'] + list(df['category'].unique()), key='category_selector_spending')

# Filter data based on selected parameters
filtered_df_spending = df[(pd.to_datetime(df['invoice_date']).dt.date == selected_date) | (selected_date == 'All')]
filtered_df_spending = filtered_df_spending[(filtered_df_spending['gender'] == selected_gender) | (selected_gender == 'All')]
filtered_df_spending = filtered_df_spending[(filtered_df_spending['price'].between(selected_price_range[0], selected_price_range[1]))]
filtered_df_spending = filtered_df_spending[(filtered_df_spending['category'] == selected_category_spending) | (selected_category_spending == 'All')]

# Objective 1: Temporal Money Spent Analysis
fig1_spending = px.bar(
    filtered_df_spending.groupby(['invoice_date', 'age']).sum().reset_index(),
    x='invoice_date',
    y='price',
    color='age',
    title='Temporal Money Spent Analysis',
    labels={'invoice_date': 'Invoice Date', 'price': 'Total Money Spent', 'age': 'Age'},
)

# Objective 2: Price and Age Patterns
fig2_spending = px.scatter(
    filtered_df_spending,
    x='age',
    y='price',
    color='age',
    title='Price and Age Patterns',
    labels={'age': 'Age', 'price': 'Total Money Spent'},
)

# Objective 3: Category-Specific Spending Analysis
fig3_spending = px.bar(
    filtered_df_spending.groupby(['category', 'age']).sum().reset_index(),
    x='category',
    y='price',
    color='age',
    title='Category-Specific Spending Analysis',
    labels={'category': 'Category', 'price': 'Total Money Spent', 'age': 'Age'},
)

# Display the charts
st.plotly_chart(fig1_spending)
st.plotly_chart(fig2_spending)
st.plotly_chart(fig3_spending)


# Filter data based on selected category
selected_category_quantity = st.sidebar.selectbox('Select Category:', ['All'] + list(df['category'].unique()), key='category_selector_quantity')

# Filter data based on selected category
filtered_df_quantity = df[(df['category'] == selected_category_quantity) | (selected_category_quantity == 'All')]

# Objective: Category-Specific Cumulative Quantity Analysis
fig_quantity = px.line(
    filtered_df_quantity.groupby(['invoice_date']).sum().reset_index(),
    x='invoice_date',
    y='quantity',
    title=f'Category-Specific Cumulative Quantity Analysis - {selected_category_quantity}',
    labels={'invoice_date': 'Invoice Date', 'quantity': 'Cumulative Quantity'},
)

# Display the chart
st.plotly_chart(fig_quantity)
