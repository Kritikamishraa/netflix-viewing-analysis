import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv('netflix_viewing_data.csv')

# 1️⃣ Basic info
print(df.head())
print(df.describe(include='all'))

# 2️⃣ Convert date and derive new columns
df['WatchDate'] = pd.to_datetime(df['WatchDate'])
df['Month'] = df['WatchDate'].dt.month

# 3️⃣ Total viewing duration by Genre
genre_duration = df.groupby('Genre')['DurationMinutes'].sum().reset_index()
print("\nTotal duration by genre:\n", genre_duration)

# 4️⃣ Most watched title
title_views = df['Title'].value_counts().reset_index()
title_views.columns = ['Title', 'WatchCount']
print("\nMost watched titles:\n", title_views)

# 5️⃣ Device usage stats
device_usage = df['Device'].value_counts().reset_index()
device_usage.columns = ['Device', 'UsageCount']
print("\nDevice usage stats:\n", device_usage)

# 6️⃣ NumPy stats on duration
mean_duration = np.mean(df['DurationMinutes'])
std_duration = np.std(df['DurationMinutes'])
max_duration = np.max(df['DurationMinutes'])
print(f"\nDuration stats -> Mean: {mean_duration}, Std: {std_duration}, Max: {max_duration}")

# 7️⃣ Filter long sessions
long_sessions = df[df['DurationMinutes'] > mean_duration]
print("\nLong viewing sessions:\n", long_sessions[['UserID', 'Title', 'DurationMinutes']])

# 8️⃣ Monthly viewing trend
monthly_duration = df.groupby('Month')['DurationMinutes'].sum().reset_index()
print("\nMonthly viewing trend:\n", monthly_duration)
