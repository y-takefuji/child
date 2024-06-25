import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('data.csv')

# Convert 'Week Ending Date' to datetime
df['Week Ending Date'] = pd.to_datetime(df['Week Ending Date'])

# Filter data for 'Geographic aggregation' == "USA"
usa_data = df[df['Geographic aggregation'] == "USA"]

# Plot the data
plt.figure(figsize=(10,6))
plt.plot(usa_data['Week Ending Date'], usa_data['Number Hospitals Reporting Pediatric COVID-19 Admissions'])
plt.xlabel('Week Ending Date')
plt.ylabel('Number Hospitals Reporting Pediatric COVID-19 Admissions')
plt.title('Pediatric COVID-19 Admissions in USA')
plt.grid(True)
plt.savefig('pediatric.png',dpi=300)
plt.show()
