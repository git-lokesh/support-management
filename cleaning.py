import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('customer_support_tickets.csv')

# Step 1: Data Cleaning

# Displaying the first few rows of the dataset
print("First few rows of the dataset:")
print(df.head())

# Step 2: Check for null values
print("\nChecking for null values:")
print(df.isnull().sum())

# Step 3: Data Type Information
print("\nData Types:")
print(df.dtypes)

# Step 4: Summary Statistics
print("\nSummary Statistics:")
print(df.describe())

# Step 5: Check for duplicates
print("\nChecking for duplicate rows:")
print(df.duplicated().sum())

# Step 6: Handling missing values (imputation or removal)
# Example: Dropping rows with missing 'Ticket Status'
df_cleaned = df.dropna(subset=['Ticket Status'])

# Step 7: Displaying cleaned data
print("\nCleaned Data (after dropping missing Ticket Status):")
print(df_cleaned.head())

# Step 8: Data Exploration - Basic statistics and counts
# Most occurring issues by Ticket Type
ticket_type_counts = df_cleaned['Ticket Type'].value_counts()
print("\nMost occurring issues by Ticket Type:")
print(ticket_type_counts)

# Step 9: Visualization
# 9.1 Ticket Type Distribution - Figure 1 (Bar Chart)
plt.figure(figsize=(12, 6))
df_cleaned['Ticket Type'].value_counts().plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Figure 1: Distribution of Ticket Types')
plt.xlabel('Ticket Type')
plt.ylabel('Count of Tickets')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

# 9.2 Most occurring issues by Ticket Type - Figure 2 (Pie Chart)
plt.figure(figsize=(8, 8))
plt.pie(ticket_type_counts, labels=ticket_type_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel', len(ticket_type_counts)))
plt.title('Figure 2: Ticket Type Distribution (Pie Chart)')
plt.show()