
import sqlite3
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend for matplotlib

import matplotlib.pyplot as plt
# Connect to the database
conn = sqlite3.connect('sales_data.db')

# Write SQL query
query = '''
SELECT 
    product, 
    SUM(quantity) AS total_qty, 
    SUM(quantity * price) AS revenue 
FROM 
    sales 
GROUP BY 
    product
'''

# Load query result into pandas
df = pd.read_sql_query(query, conn)

# Print the DataFrame
print(df)

conn.close()
# Plot a bar chart of revenue by product
df.plot(kind='bar', x='product', y='revenue', legend=False)
plt.title("Revenue by Product")
plt.ylabel("Revenue")
plt.xlabel("Product")
plt.tight_layout()
plt.savefig("sales_chart.png")  # Optional
plt.show()