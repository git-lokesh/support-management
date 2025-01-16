import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('customer_support_tickets.csv')

print("First few rows of the dataset:")
print(df.head())

print("\nChecking for null values:")
print(df.isnull().sum())

print("\nData Types:")
print(df.dtypes)

print("\nSummary Statistics:")
print(df.describe())

print("\nChecking for duplicate rows:")
duplicates_count = df.duplicated().sum()
print(f"Number of duplicate rows: {duplicates_count}")

df_cleaned = df.drop_duplicates()
print("\nData after removing duplicates:")
print(df_cleaned.head())

df_cleaned = df_cleaned.dropna(subset=['Ticket Status'])

print("\nData after removing rows with missing 'Ticket Status':")
print(df_cleaned.isnull().sum())

if 'Ticket Type' in df_cleaned.columns:
    df_cleaned['Ticket Type'] = df_cleaned['Ticket Type'].str.strip().str.lower()

if 'Ticket Age' in df_cleaned.columns:
    threshold = 365
    df_cleaned = df_cleaned[df_cleaned['Ticket Age'] <= threshold]

print("\nCleaned Data Overview:")
print(df_cleaned.info())

ticket_type_counts = df_cleaned['Ticket Type'].value_counts()
print("\nMost occurring issues by Ticket Type:")
print(ticket_type_counts)

plt.figure(figsize=(12, 6))
df_cleaned['Ticket Type'].value_counts().plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Figure 1: Distribution of Ticket Types')
plt.xlabel('Ticket Type')
plt.ylabel('Count of Tickets')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

plt.figure(figsize=(8, 8))
plt.pie(ticket_type_counts, labels=ticket_type_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel', len(ticket_type_counts)))
plt.title('Figure 2: Ticket Type Distribution (Pie Chart)')
plt.show()
