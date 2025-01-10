import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('customer_support_tickets.csv')

# Convert date columns to datetime format
date_columns = ["Date of Purchase", "First Response Time", "Time to Resolution"]
for col in date_columns:
    df[col] = pd.to_datetime(df[col], errors='coerce')  # 'coerce' will replace errors with NaT

# Step 1: Group tickets by different time periods
# 1.1 Grouping by Day of Purchase
df['Purchase Day'] = df['Date of Purchase'].dt.day

# 1.2 Grouping by Week of Purchase
df['Purchase Week'] = df['Date of Purchase'].dt.isocalendar().week  # Using isocalendar to avoid 'week' error

# 1.3 Grouping by Month of Purchase
df['Purchase Month'] = df['Date of Purchase'].dt.month

# Step 2: Count the most occurring issues in specific time periods

# 2.1 Count tickets by day
tickets_per_day = df.groupby('Purchase Day')['Ticket ID'].count().reset_index()
tickets_per_day.columns = ['Day', 'Ticket Count']

# 2.2 Count tickets by week
tickets_per_week = df.groupby('Purchase Week')['Ticket ID'].count().reset_index()
tickets_per_week.columns = ['Week', 'Ticket Count']

# 2.3 Count tickets by month
tickets_per_month = df.groupby('Purchase Month')['Ticket ID'].count().reset_index()
tickets_per_month.columns = ['Month', 'Ticket Count']

# Step 3: Visualizations - Most occurring issues in specific time periods

# 3.1 Most occurring issues per day - Figure 1
plt.figure(figsize=(12, 6))
sns.barplot(x='Day', y='Ticket Count', data=tickets_per_day, palette='viridis')
plt.title('Figure 1: Most Occurring Issues per Day')
plt.xlabel('Day of Purchase')
plt.ylabel('Ticket Count')
plt.show()

# 3.2 Most occurring issues per week - Figure 1
plt.figure(figsize=(12, 6))
sns.barplot(x='Week', y='Ticket Count', data=tickets_per_week, palette='mako')
plt.title('Figure 1: Most Occurring Issues per Week')
plt.xlabel('Week of Purchase')
plt.ylabel('Ticket Count')
plt.show()

# 3.3 Most occurring issues per month - Figure 1
plt.figure(figsize=(12, 6))
sns.barplot(x='Month', y='Ticket Count', data=tickets_per_month, palette='coolwarm')
plt.title('Figure 1: Most Occurring Issues per Month')
plt.xlabel('Month of Purchase')
plt.ylabel('Ticket Count')
plt.show()
