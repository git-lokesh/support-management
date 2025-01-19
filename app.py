import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load and preprocess the dataset
df = pd.read_csv('customer_support_tickets.csv')
df_cleaned = df.drop_duplicates().dropna(subset=['Ticket Status'])

if 'Ticket Type' in df_cleaned.columns:
    df_cleaned['Ticket Type'] = df_cleaned['Ticket Type'].str.strip().str.lower()

if 'Ticket Age' in df_cleaned.columns:
    threshold = 365
    df_cleaned = df_cleaned[df_cleaned['Ticket Age'] <= threshold]

# Streamlit App
st.set_page_config(page_title="Customer Support Dashboard", layout="wide")

# Title and Description
st.title("Customer Support Ticket Analysis")
st.write("""
This application visualizes data from customer support tickets, including the distribution of ticket types and their proportions. 
Explore the charts below for insights into the most common issues and their frequency.
""")

# Display raw data
with st.expander("View Raw Data"):
    st.write(df_cleaned)

# Generate Bar Chart
st.subheader("Distribution of Ticket Types (Bar Chart)")
fig_bar, ax_bar = plt.subplots(figsize=(12, 6))
df_cleaned['Ticket Type'].value_counts().plot(kind='bar', color='skyblue', edgecolor='black', ax=ax_bar)
ax_bar.set_title('Distribution of Ticket Types')
ax_bar.set_xlabel('Ticket Type')
ax_bar.set_ylabel('Count of Tickets')
ax_bar.set_xticklabels(ax_bar.get_xticklabels(), rotation=45)
ax_bar.grid(axis='y')
st.pyplot(fig_bar)

# Generate Pie Chart
st.subheader("Ticket Type Distribution (Pie Chart)")
ticket_type_counts = df_cleaned['Ticket Type'].value_counts()
fig_pie, ax_pie = plt.subplots(figsize=(8, 8))
ax_pie.pie(ticket_type_counts, labels=ticket_type_counts.index, autopct='%1.1f%%', startangle=140,
           colors=sns.color_palette('pastel', len(ticket_type_counts)))
ax_pie.set_title('Ticket Type Distribution')
st.pyplot(fig_pie)
